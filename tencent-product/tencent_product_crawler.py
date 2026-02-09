#!/usr/bin/env python3
"""
腾讯云产品详情页爬虫
从腾讯云产品目录 API 获取产品列表，爬取产品详情页并转换为 Markdown
支持点击 tab 获取完整的产品架构内容
"""

import json
import subprocess
import time
import re
import os
import requests
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Set, Tuple


# 配置
OUTPUT_DIR = Path(__file__).parent / 'products'
METADATA_FILE = OUTPUT_DIR / 'crawl_metadata.json'
RATE_LIMIT_SECONDS = 2.5
PRODUCT_API_URL = 'https://qcloudimg.tencent-cloud.cn/scripts/qccomponents/v2/full-nav-tree.json'
PRODUCT_URL_PREFIX = 'https://cloud.tencent.com/product/'


def run_browser_command(cmd: str, timeout: int = 60) -> str:
    """运行 agent-browser 命令"""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=timeout
        )
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return ""
    except Exception as e:
        print(f"  [错误] {e}")
        return ""


def open_url(url: str, wait_ms: int = 4000) -> bool:
    """打开URL"""
    output = run_browser_command(f'agent-browser open "{url}" --wait {wait_ms}', timeout=60)
    return '✓' in output


def get_page_content() -> str:
    """获取页面快照"""
    return run_browser_command('agent-browser snapshot 2>/dev/null', timeout=30)


def get_page_images() -> List[str]:
    """获取页面上的所有图片URL"""
    js_cmd = '''agent-browser eval "Array.from(document.images).map(img => img.src).filter(s => s && !s.includes('data:')).join('\\n')" 2>/dev/null'''
    output = run_browser_command(js_cmd, timeout=15)
    if output:
        output = output.strip().strip('"').replace('\\n', '\n')
        images = [url.strip() for url in output.split('\n') if url.strip()]
        return images
    return []


def get_architecture_tabs() -> List[str]:
    """获取产品架构部分的 tab 名称列表"""
    # 获取产品架构区域的 tab（使用 .tl-tabs__item-cont 选择器，排除 FAQ tab）
    js_cmd = '''agent-browser eval "
        const tabContents = Array.from(document.querySelectorAll('.tl-tabs__item-cont'));
        // 找到产品架构相关的 tabs（前几个，在 FAQ 之前）
        const archTabs = [];
        for (const tab of tabContents) {
            const text = tab.textContent.trim();
            // FAQ 相关的 tab 停止
            if (text.includes('问题') || text.includes('FAQ')) break;
            archTabs.push(text);
        }
        archTabs.join('|||')
    " 2>/dev/null'''
    output = run_browser_command(js_cmd, timeout=15)
    if output:
        output = output.strip().strip('"')
        if output:
            return [t.strip() for t in output.split('|||') if t.strip()]
    return []


def click_tab_by_index(index: int) -> bool:
    """点击指定索引的 tab（使用 .tl-tabs__item-cont）"""
    js_cmd = f'''agent-browser eval "
        const tabContents = Array.from(document.querySelectorAll('.tl-tabs__item-cont'));
        if (tabContents[{index}]) {{
            tabContents[{index}].click();
            'clicked'
        }} else {{
            'not found'
        }}
    " 2>/dev/null'''
    output = run_browser_command(js_cmd, timeout=15)
    return 'clicked' in output


def get_tab_panel_content(index: int) -> Tuple[str, List[str]]:
    """获取指定索引的 tab panel 的文字内容和图片"""
    # 改进：获取第一个 tabs 容器内的 panel
    js_cmd = f'''agent-browser eval "
        const container = document.querySelector('.tl-tabs');
        if (container) {{
            const panels = container.querySelectorAll('.tl-tabs__panel');
            const panel = panels[{index}];
            if (panel) {{
                const text = panel.innerText || '';
                const imgs = Array.from(panel.querySelectorAll('img')).map(i => i.src).filter(s => s && !s.includes('data:'));
                JSON.stringify({{text: text, images: imgs}})
            }} else {{
                '{{}}'
            }}
        }} else {{
            '{{}}'
        }}
    " 2>/dev/null'''
    output = run_browser_command(js_cmd, timeout=15)
    try:
        output = output.strip()
        if output.startswith('"') and output.endswith('"'):
            output = output[1:-1]
        output = output.replace('\\n', '\n').replace('\\"', '"')
        data = json.loads(output)
        return data.get('text', ''), data.get('images', [])
    except:
        return '', []


def filter_product_images(images: List[str]) -> List[str]:
    """
    智能过滤图片，只保留有价值的图片（架构图、产品截图等）
    """
    result = []
    valid_extensions = ['.png', '.jpg', '.jpeg', '.webp']

    for url in images:
        url_lower = url.lower()

        # 过滤非图片 URL
        if '/product/' in url_lower and 'qcloudimg' not in url_lower:
            continue

        # 过滤 gif/apng（保留 svg，产品架构图常用 svg）
        if any(ext in url_lower for ext in ['.gif', '.apng']):
            continue

        # 必须来自腾讯云 CDN 或有有效图片扩展名
        is_cdn = 'qcloudimg' in url_lower or 'tencent-cloud.cn' in url_lower
        has_valid_ext = any(ext in url_lower for ext in valid_extensions)
        if not is_cdn and not has_valid_ext:
            continue

        # 过滤通用图标
        skip_patterns = [
            '/image/document',
            '/icon/',
            'favicon',
            'logo',
        ]
        if any(p in url_lower for p in skip_patterns):
            continue

        # 尝试从 URL 解析尺寸
        size_match = re.search(r'[_-](\d{2,4})[x_-](\d{2,4})\.\w+$', url)
        if size_match:
            width = int(size_match.group(1))
            height = int(size_match.group(2))
            if width < 200 and height < 200:
                continue

        result.append(url)

    return list(dict.fromkeys(result))


def fetch_product_catalog() -> List[Dict]:
    """从 API 获取产品目录"""
    print("正在获取产品目录...")
    try:
        resp = requests.get(PRODUCT_API_URL, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, list) and len(data) > 0:
            first_item = data[0]
            if 'tree' in first_item:
                return first_item['tree']
        return data
    except Exception as e:
        print(f"获取产品目录失败: {e}")
        return []


def extract_products_from_tree(tree: List[Dict], category_l1: str = '', category_l2: str = '') -> List[Dict]:
    """递归遍历目录树，提取所有产品"""
    products = []
    seen_links: Set[str] = set()

    def traverse(nodes: List[Dict], l1: str, l2: str):
        for node in nodes:
            node_type = node.get('type', '')
            dict_type = node.get('dictType', '')
            link = node.get('link', '')
            title = node.get('title', '')
            children = node.get('children', [])

            if (node_type == 'entry' and
                dict_type == 'product' and
                link and
                link.startswith(PRODUCT_URL_PREFIX) and
                link not in seen_links):

                seen_links.add(link)
                products.append({
                    'title': title,
                    'slug': node.get('slug', ''),
                    'url': link,
                    'desc': node.get('desc', ''),
                    'description': node.get('description', ''),
                    'tag': node.get('tag', ''),
                    'category_l1': l1,
                    'category_l2': l2,
                })

            if children:
                new_l1 = l1
                new_l2 = l2
                if node_type == 'dir' and title:
                    if not l1:
                        new_l1 = title
                    elif not l2:
                        new_l2 = title
                traverse(children, new_l1, new_l2)

    traverse(tree, category_l1, category_l2)
    return products


def parse_product_page(snapshot: str, url: str, images: List[str] = None) -> Dict:
    """解析腾讯云产品页面"""
    result = {
        'url': url,
        'title': '',
        'intro': '',
        'sections': [],
        'images': images or []
    }

    lines = snapshot.split('\n')
    footer_keywords = ['contentinfo', '页脚', '关于腾讯云', '法律声明', '联系我们']
    promo_keywords = ['相关产品', '推荐阅读', '热门推荐', '为什么选择', '立即购买',
                      '免费试用', '立即开通', '了解更多', '查看详情']

    in_footer = False
    current_section = None
    section_content = []
    seen_content = set()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if any(kw in line for kw in footer_keywords):
            in_footer = True
            continue

        if in_footer:
            continue

        if any(kw in line for kw in promo_keywords):
            continue

        # 提取一级标题
        h1_match = re.search(r'heading "([^"]+)" \[ref=[^\]]+\] \[level=1\]', line)
        if h1_match:
            title = h1_match.group(1)
            if not result['title'] and len(title) < 100:
                result['title'] = title.split('\n')[0].strip()
            continue

        # 提取二级标题
        h2_match = re.search(r'heading "([^"]+)" \[ref=[^\]]+\] \[level=2\]', line)
        if h2_match:
            section_title = h2_match.group(1)
            if any(kw in section_title for kw in promo_keywords):
                in_footer = True
                continue
            if current_section and section_content:
                result['sections'].append({
                    'title': current_section,
                    'content': '\n'.join(section_content)
                })
            current_section = section_title
            section_content = []
            continue

        # 提取三级标题
        h3_match = re.search(r'heading "([^"]+)" \[ref=[^\]]+\] \[level=3\]', line)
        if h3_match:
            text = h3_match.group(1)
            if current_section and not in_footer:
                section_content.append(f"### {text}")
            continue

        # 提取text内容
        text_match = re.search(r'- text: (.+)$', line)
        if text_match:
            text = text_match.group(1).strip()
            if text and len(text) > 10:
                skip = ['登录', '注册', '控制台', '立即购买', '免费试用', '查看更多',
                       '立即开通', '我要咨询', '快速入门', '帮助文档']
                if any(s in text for s in skip):
                    continue
                text_key = text[:50]
                if text_key in seen_content:
                    continue
                seen_content.add(text_key)

                if not result['intro'] and not current_section:
                    result['intro'] = text
                elif current_section:
                    section_content.append(text)
            continue

        # 提取paragraph内容
        para_match = re.search(r'paragraph: (.+)$', line)
        if para_match:
            text = para_match.group(1).strip()
            if text and len(text) > 15:
                if current_section:
                    section_content.append(text)
            continue

        # 提取gridcell内容
        grid_match = re.search(r'gridcell "([^"]+)"', line)
        if grid_match:
            text = grid_match.group(1)
            if len(text) > 20:
                text = re.sub(r'\s+', ' ', text).strip()
                text = re.sub(r'\s*(立即查看|立即咨询|查看更多|了解更多)\s*$', '', text)
                text_key = text[:50]
                if current_section and text and text_key not in seen_content:
                    seen_content.add(text_key)
                    section_content.append(f"- {text}")
            continue

    if current_section and section_content:
        result['sections'].append({
            'title': current_section,
            'content': '\n'.join(section_content)
        })

    return result


def scroll_to_tabs():
    """滚动到第一个 tabs 区域"""
    js_cmd = '''agent-browser eval "
        const tabs = document.querySelector('.tl-tabs');
        if (tabs) {
            tabs.scrollIntoView({behavior: 'instant', block: 'center'});
            'scrolled'
        } else {
            'no tabs'
        }
    " 2>/dev/null'''
    output = run_browser_command(js_cmd, timeout=15)
    return 'scrolled' in output


def get_section_content(section_name: str) -> Tuple[str, List[str]]:
    """
    获取指定 h2 section 的内容（用于非 tabs 区域，如产品架构）
    返回: (text_content, [image_urls])
    """
    js_cmd = f'''agent-browser eval "
        const h2s = Array.from(document.querySelectorAll('h2'));
        const targetH2 = h2s.find(h => h.textContent.includes('{section_name}'));
        if (targetH2) {{
            let content = [];
            let images = [];
            let parent = targetH2.closest('section') || targetH2.closest('[class*=\\"banner\\"]') || targetH2.parentElement;
            let next = parent.nextElementSibling;
            while (next) {{
                const nextH2 = next.querySelector('h2');
                if (nextH2) break;
                const text = next.innerText.trim();
                if (text && text.length > 10) content.push(text);
                const imgs = next.querySelectorAll('img');
                imgs.forEach(img => {{ if (img.src && !img.src.includes('data:')) images.push(img.src); }});
                next = next.nextElementSibling;
            }}
            JSON.stringify({{text: content.join('\\\\n'), images: images}})
        }} else {{
            JSON.stringify({{text: '', images: []}})
        }}
    " 2>/dev/null'''
    output = run_browser_command(js_cmd, timeout=15)
    try:
        output = output.strip()
        if output.startswith('"') and output.endswith('"'):
            output = output[1:-1]
        output = output.replace('\\n', '\n').replace('\\"', '"').replace('\\\\n', '\n')
        data = json.loads(output)
        return data.get('text', ''), data.get('images', [])
    except:
        return '', []


def get_product_intro() -> str:
    """获取产品简介（hero 区域的描述段落）"""
    js_cmd = '''agent-browser eval '
        var hero = document.querySelector(".tpm-prod-hero, [class*=hero]");
        if (hero) {
            var p = hero.querySelector("p");
            if (p && p.innerText.length > 30) {
                p.innerText.trim();
            } else {
                "";
            }
        } else {
            var allP = Array.from(document.querySelectorAll("p"));
            for (var i = 0; i < allP.length; i++) {
                if (allP[i].innerText.length > 50) {
                    allP[i].innerText.trim();
                    break;
                }
            }
        }
    ' 2>/dev/null'''
    output = run_browser_command(js_cmd, timeout=15)
    if output:
        output = output.strip().strip('"')
        if output and len(output) > 20:
            return output
    return ''


def get_all_sections() -> List[Dict]:
    """
    获取页面所有 h2 section 的内容
    返回: [{'title': 'h2标题', 'content': '内容', 'images': [...]}]
    """
    js_cmd = '''agent-browser eval '
        var result = [];
        var h2s = Array.from(document.querySelectorAll("h2"));
        for (var i = 0; i < h2s.length; i++) {
            var h2 = h2s[i];
            var title = h2.textContent.trim();
            if (!title || title.length > 50) continue;

            var header = h2.closest("header, .tpm-section__hd");
            var section = header ? header.parentElement : h2.parentElement.parentElement;
            if (!section) continue;
            if (section.querySelector(".tl-tabs")) continue;

            var content = [];
            var images = [];
            var h3s = section.querySelectorAll("h3");

            for (var j = 0; j < h3s.length; j++) {
                var h3 = h3s[j];
                var h3Title = h3.textContent.trim();
                var parent = h3.parentElement;
                var h3Text = parent.innerText.replace(h3Title, "").trim();
                if (h3Title && h3Text && h3Text.length > 10) {
                    content.push("### " + h3Title + "\\n" + h3Text);
                }
            }

            if (h3s.length === 0) {
                var sectionText = section.innerText.replace(title, "").trim();
                if (sectionText && sectionText.length > 20) {
                    content.push(sectionText);
                }
            }

            var imgs = section.querySelectorAll("img");
            for (var k = 0; k < imgs.length; k++) {
                if (imgs[k].src && imgs[k].src.indexOf("data:") < 0) {
                    images.push(imgs[k].src);
                }
            }

            if (content.length > 0) {
                result.push({title: title, content: content.join("\\n\\n"), images: images});
            }
        }
        JSON.stringify(result)
    ' 2>/dev/null'''
    output = run_browser_command(js_cmd, timeout=20)
    try:
        output = output.strip()
        # 输出格式是 '"[...]"'，先用 json.loads 解码外层字符串
        if output.startswith('"'):
            output = json.loads(output)
        return json.loads(output)
    except Exception as e:
        print(f"  [警告] sections 解析失败: {e}")
        return []


def get_product_features() -> List[Dict[str, str]]:
    """
    获取产品特性（h2:产品特性 后的 h3 + text 结构）
    返回: [{'title': '特性名', 'content': '描述'}, ...]
    """
    js_cmd = '''agent-browser eval "
        const h2s = Array.from(document.querySelectorAll('h2'));
        const featH2 = h2s.find(h => h.textContent.includes('产品特性'));
        if (!featH2) {
            JSON.stringify([]);
        } else {
            const result = [];
            // 找到下一个 h2 之前的所有 h3
            let parent = featH2.closest('section') || featH2.closest('[class*=\\"banner\\"]') || featH2.parentElement;
            let current = parent.nextElementSibling;
            while (current) {
                const nextH2 = current.querySelector('h2');
                if (nextH2) break;
                const h3 = current.querySelector('h3');
                if (h3) {
                    const title = h3.textContent.trim();
                    // 获取 h3 后面的文本
                    let text = '';
                    let sibling = h3.nextElementSibling;
                    while (sibling && sibling.tagName !== 'H3') {
                        if (sibling.innerText) text += sibling.innerText.trim() + ' ';
                        sibling = sibling.nextElementSibling;
                    }
                    // 如果没有 sibling，试着从 parent 获取
                    if (!text) {
                        const parentText = current.innerText.replace(title, '').trim();
                        text = parentText;
                    }
                    if (title && text) result.push({title: title, content: text.trim()});
                } else {
                    // 可能直接是 h3 元素
                    if (current.tagName === 'H3') {
                        const title = current.textContent.trim();
                        const nextEl = current.nextElementSibling;
                        if (nextEl && nextEl.innerText) {
                            result.push({title: title, content: nextEl.innerText.trim()});
                        }
                    }
                }
                current = current.nextElementSibling;
            }
            JSON.stringify(result);
        }
    " 2>/dev/null'''
    output = run_browser_command(js_cmd, timeout=15)
    try:
        output = output.strip()
        if output.startswith('"') and output.endswith('"'):
            output = output[1:-1]
        output = output.replace('\\n', '\n').replace('\\"', '"')
        return json.loads(output)
    except:
        return []


def get_tabs_by_section(section_keyword: str) -> Tuple[int, List[str]]:
    """
    根据 section 关键词找到对应的 tabs 容器
    返回: (container_index, [tab_names])
    """
    js_cmd = f'''agent-browser eval "
        const allTabs = document.querySelectorAll('.tl-tabs');
        let result = {{idx: -1, tabs: []}};
        allTabs.forEach((container, idx) => {{
            // 找这个 tabs 前面的 h2
            let prev = container.previousElementSibling;
            while (prev) {{
                const h2 = prev.querySelector && prev.querySelector('h2');
                const h2Text = h2 ? h2.textContent : (prev.tagName === 'H2' ? prev.textContent : '');
                if (h2Text && h2Text.includes('{section_keyword}')) {{
                    const items = container.querySelectorAll('.tl-tabs__item-cont');
                    result = {{idx: idx, tabs: Array.from(items).map(i => i.textContent.trim())}};
                    break;
                }}
                prev = prev.previousElementSibling;
            }}
        }});
        JSON.stringify(result)
    " 2>/dev/null'''
    output = run_browser_command(js_cmd, timeout=15)
    try:
        output = output.strip()
        if output.startswith('"') and output.endswith('"'):
            output = output[1:-1]
        output = output.replace('\\n', '\n').replace('\\"', '"')
        data = json.loads(output)
        return data.get('idx', -1), data.get('tabs', [])
    except:
        return -1, []


def click_tab_in_container(container_idx: int, tab_idx: int) -> bool:
    """点击指定容器中的指定 tab"""
    js_cmd = f'''agent-browser eval "
        const allTabs = document.querySelectorAll('.tl-tabs');
        if (allTabs[{container_idx}]) {{
            const items = allTabs[{container_idx}].querySelectorAll('.tl-tabs__item-cont');
            if (items[{tab_idx}]) {{
                items[{tab_idx}].scrollIntoView({{behavior: 'instant', block: 'center'}});
                items[{tab_idx}].click();
                'clicked'
            }} else {{
                'tab not found'
            }}
        }} else {{
            'container not found'
        }}
    " 2>/dev/null'''
    output = run_browser_command(js_cmd, timeout=15)
    return 'clicked' in output


def get_panel_in_container(container_idx: int, panel_idx: int) -> Tuple[str, List[str]]:
    """获取指定容器中指定 panel 的内容"""
    js_cmd = f'''agent-browser eval "
        const allTabs = document.querySelectorAll('.tl-tabs');
        if (allTabs[{container_idx}]) {{
            const panels = allTabs[{container_idx}].querySelectorAll('.tl-tabs__panel');
            const panel = panels[{panel_idx}];
            if (panel) {{
                const text = panel.innerText || '';
                const imgs = Array.from(panel.querySelectorAll('img')).map(i => i.src).filter(s => s && !s.includes('data:'));
                JSON.stringify({{text: text, images: imgs}})
            }} else {{
                JSON.stringify({{text: '', images: []}})
            }}
        }} else {{
            JSON.stringify({{text: '', images: []}})
        }}
    " 2>/dev/null'''
    output = run_browser_command(js_cmd, timeout=15)
    try:
        output = output.strip()
        if output.startswith('"') and output.endswith('"'):
            output = output[1:-1]
        output = output.replace('\\n', '\n').replace('\\"', '"')
        data = json.loads(output)
        return data.get('text', ''), data.get('images', [])
    except:
        return '', []


def crawl_all_tabs() -> List[Dict]:
    """
    遍历页面所有 tabs 容器，点击每个 tab 获取内容
    返回: [{'section': 'h2标题', 'tabs': [{'name': 'tab名', 'text': '内容', 'images': [...]}]}]
    """
    # 先获取所有 tabs 容器信息
    js_cmd = '''agent-browser eval "
        const allTabs = document.querySelectorAll('.tl-tabs');
        const result = [];
        allTabs.forEach((container, idx) => {
            // 找 tabs 前面的 h2 标题
            let section = '';
            let prev = container.previousElementSibling;
            for (let i = 0; i < 5 && prev; i++) {
                const h2 = prev.querySelector && prev.querySelector('h2');
                if (h2) { section = h2.textContent.trim(); break; }
                if (prev.tagName === 'H2') { section = prev.textContent.trim(); break; }
                prev = prev.previousElementSibling;
            }
            const items = container.querySelectorAll('.tl-tabs__item-cont');
            const tabNames = Array.from(items).map(i => i.textContent.trim());
            result.push({idx: idx, section: section, tabNames: tabNames});
        });
        JSON.stringify(result)
    " 2>/dev/null'''
    output = run_browser_command(js_cmd, timeout=15)

    try:
        output = output.strip()
        if output.startswith('"') and output.endswith('"'):
            output = output[1:-1]
        output = output.replace('\\n', '\n').replace('\\"', '"')
        containers = json.loads(output)
    except:
        return []

    if not containers:
        return []

    result = []
    for container in containers:
        idx = container['idx']
        section = container['section']
        tab_names = container['tabNames']

        if not tab_names:
            continue

        print(f"  {section or f'Tabs区域{idx}'}: {len(tab_names)} 个 tab")

        tabs_data = []
        for i, tab_name in enumerate(tab_names):
            # 点击 tab
            if click_tab_in_container(idx, i):
                time.sleep(0.6)
                text, images = get_panel_in_container(idx, i)
                images = filter_product_images(images)
                if text or images:
                    tabs_data.append({
                        'name': tab_name,
                        'text': text.strip(),
                        'images': images
                    })
                    print(f"    - {tab_name}: {len(text)}字, {len(images)}张图")

        if tabs_data:
            result.append({
                'section': section,
                'tabs': tabs_data
            })

    return result


def crawl_section_tabs(section_keyword: str) -> Dict[str, Tuple[str, List[str]]]:
    """
    爬取指定 section 下的所有 tabs 内容
    返回: {tab_name: (text_content, [image_urls])}
    """
    result = {}
    container_idx, tabs = get_tabs_by_section(section_keyword)

    if container_idx < 0 or not tabs:
        return result

    print(f"  发现 {section_keyword} 区域 {len(tabs)} 个 tab: {', '.join(tabs[:5])}...")

    for i, tab_name in enumerate(tabs):
        # 点击 tab 触发内容加载
        if click_tab_in_container(container_idx, i):
            time.sleep(0.8)  # 等待内容加载
            text, images = get_panel_in_container(container_idx, i)
            filtered_images = filter_product_images(images)
            if text or filtered_images:
                result[tab_name] = (text.strip(), filtered_images)
                print(f"    - {tab_name}: {len(text)}字, {len(filtered_images)}张图")

    return result


def crawl_architecture_tabs() -> Dict[str, Tuple[str, List[str]]]:
    """
    爬取产品架构部分的所有 tab 内容
    返回: {tab_name: (text_content, [image_urls])}
    """
    result = {}
    tabs = get_architecture_tabs()

    if not tabs:
        return result

    print(f"  发现 {len(tabs)} 个架构 tab: {', '.join(tabs)}")

    # 滚动到 tabs 区域以触发懒加载
    scroll_to_tabs()
    time.sleep(1)

    for i, tab_name in enumerate(tabs):
        # 点击 tab 触发内容加载
        if click_tab_by_index(i):
            time.sleep(1)  # 等待内容加载
            text, images = get_tab_panel_content(i)
            filtered_images = filter_product_images(images)
            result[tab_name] = (text, filtered_images)
            print(f"    - {tab_name}: {len(text)}字, {len(filtered_images)}张图")
        else:
            print(f"    - {tab_name}: 点击失败")

    return result


def generate_markdown_v2(product: Dict, page_content: Dict, sections: List[Dict] = None,
                         all_tabs: List[Dict] = None) -> str:
    """生成 Markdown 文件（简化版）"""
    title = page_content.get('title') or product.get('title', '')

    md = f"""---
title: "{product.get('title', '').replace('"', '\\"')}"
slug: "{product.get('slug', '')}"
url: {product.get('url', '')}
category_l1: "{product.get('category_l1', '')}"
category_l2: "{product.get('category_l2', '')}"
crawled_at: {datetime.now().isoformat()}
---

# {title}

"""

    # 产品简介
    intro = page_content.get('intro', '')
    if intro:
        md += f"## 产品简介\n\n{intro}\n\n"

    # 所有非 tabs 的 section 内容
    if sections:
        for section in sections:
            section_title = section.get('title', '')
            section_content = section.get('content', '')
            section_images = section.get('images', [])
            if section_title:
                md += f"## {section_title}\n\n"
                if section_content:
                    md += f"{section_content}\n\n"
                for i, img in enumerate(filter_product_images(section_images), 1):
                    md += f"![{section_title}图{i}]({img})\n\n"

    # 所有 tabs 内容
    if all_tabs:
        for container in all_tabs:
            section = container.get('section', '')
            tabs = container.get('tabs', [])
            if section:
                md += f"## {section}\n\n"
            for tab in tabs:
                tab_name = tab.get('name', '')
                text = tab.get('text', '')
                images = tab.get('images', [])
                if tab_name:
                    md += f"### {tab_name}\n\n"
                if text:
                    lines = [l.strip() for l in text.split('\n') if len(l.strip()) > 3]
                    if lines:
                        md += '\n'.join(lines) + '\n\n'
                for i, img in enumerate(images, 1):
                    md += f"![{tab_name}图{i}]({img})\n\n"

    return md


def generate_markdown(product: Dict, page_content: Dict, features: List[Dict] = None,
                      scene_tabs: Dict = None, arch_text: str = '', arch_images: List[str] = None) -> str:
    """生成 Markdown 文件"""
    title = page_content.get('title') or product.get('title', '')

    md = f"""---
title: "{product.get('title', '').replace('"', '\\"')}"
slug: "{product.get('slug', '')}"
url: {product.get('url', '')}
category_l1: "{product.get('category_l1', '')}"
category_l2: "{product.get('category_l2', '')}"
desc: "{product.get('desc', '').replace('"', '\\"')}"
tag: "{product.get('tag', '')}"
crawled_at: {datetime.now().isoformat()}
---

# {title}

"""

    # 产品简介
    intro = page_content.get('intro') or product.get('description', '') or product.get('desc', '')
    if intro:
        md += f"""## 产品简介

{intro}

"""

    # 产品图片（非架构图，限制数量）
    images = page_content.get('images', [])
    if images:
        md += "## 产品图片\n\n"
        for i, img_url in enumerate(images[:5], 1):
            md += f"![图片{i}]({img_url})\n\n"

    # 各个章节（跳过应用场景、产品架构、产品特性，单独处理）
    skip_sections = ['相关产品', '推荐阅读', '热门推荐', '产品架构', '应用场景', '产品特性']
    for section in page_content.get('sections', []):
        section_title = section.get('title', '')
        section_content = section.get('content', '')

        if section_title in skip_sections:
            continue

        if section_title and section_content:
            md += f"""## {section_title}

{section_content}

"""

    # 产品特性
    if features:
        md += "## 产品特性\n\n"
        for feat in features:
            feat_title = feat.get('title', '')
            feat_content = feat.get('content', '')
            if feat_title and feat_content:
                md += f"### {feat_title}\n\n{feat_content}\n\n"

    # 应用场景（带 tab 内容）
    if scene_tabs:
        md += "## 应用场景\n\n"
        for tab_name, (text, images) in scene_tabs.items():
            md += f"### {tab_name}\n\n"
            if text:
                # 清理文本
                text = text.strip()
                lines = [l.strip() for l in text.split('\n') if len(l.strip()) > 5]
                if lines:
                    md += '\n'.join(lines) + '\n\n'
            if images:
                for i, img_url in enumerate(images, 1):
                    md += f"![{tab_name}场景图{i}]({img_url})\n\n"

    # 产品架构（独立区域）
    if arch_text or arch_images:
        md += "## 产品架构\n\n"
        if arch_text:
            lines = [l.strip() for l in arch_text.split('\n') if len(l.strip()) > 5]
            if lines:
                md += '\n'.join(lines) + '\n\n'
        if arch_images:
            for i, img_url in enumerate(arch_images, 1):
                md += f"![产品架构图{i}]({img_url})\n\n"

    return md


def load_crawl_metadata() -> Dict:
    """加载爬取元数据"""
    if METADATA_FILE.exists():
        with open(METADATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'crawled_urls': [], 'last_crawl': None, 'total_products': 0, 'errors': []}


def save_crawl_metadata(metadata: Dict):
    """保存爬取元数据"""
    METADATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(METADATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)


def sanitize_filename(name: str) -> str:
    """生成安全的文件名"""
    safe = re.sub(r'[<>:"/\\|?*\r\n]', '', name)
    safe = re.sub(r'\s+', ' ', safe).strip()
    return safe[:60]


def get_category_dir(category: str) -> str:
    """生成分类目录名"""
    if not category or category.strip() == '':
        return '其他'
    return sanitize_filename(category)


def click_all_tabs_and_get_html() -> Tuple[str, str]:
    """点击所有 tabs 触发加载，然后获取页面标题和 HTML"""
    # 点击所有 tabs 触发懒加载
    run_browser_command('agent-browser eval "document.querySelectorAll(\'.tl-tabs__item-cont\').forEach(function(t){t.click()})" 2>/dev/null', timeout=15)
    time.sleep(1.5)

    # 获取标题
    title_output = run_browser_command('agent-browser eval "document.querySelector(\'h1\') ? document.querySelector(\'h1\').innerText : \'\'" 2>/dev/null', timeout=10)
    title = ''
    if title_output:
        title = title_output.strip().strip('"')

    # 获取完整 HTML
    output = run_browser_command('agent-browser eval "document.documentElement.outerHTML" 2>/dev/null', timeout=30)
    html = ''
    if output:
        output = output.strip()
        if output.startswith('"'):
            try:
                html = json.loads(output)
            except:
                html = output[1:-1].replace('\\n', '\n').replace('\\"', '"') if output.endswith('"') else output
        else:
            html = output
    return title, html


def snapshot_to_markdown(snapshot: str) -> str:
    """将 agent-browser snapshot 转为 markdown"""
    lines = []
    skip_keywords = ['登录', '注册', '控制台', '备案', '文档', '最新活动', '产品', '解决方案',
                     '定价', '云市场', '开发者', '客户支持', '合作与生态', '了解腾讯云',
                     '中国站', '搜索', '热词', '页面导航', '回到顶部', '联系销售']

    in_content = False
    for line in snapshot.split('\n'):
        line = line.strip()
        if not line:
            continue

        # 跳过导航相关
        if any(kw in line for kw in skip_keywords):
            continue

        # 提取标题
        heading_match = re.search(r'heading "([^"]+)".*\[level=(\d)\]', line)
        if heading_match:
            text = heading_match.group(1)
            level = int(heading_match.group(2))
            if text and len(text) < 100:
                lines.append(f"{'#' * level} {text}\n")
                in_content = True
            continue

        # 提取段落
        para_match = re.search(r'paragraph: (.+)$', line)
        if para_match:
            text = para_match.group(1).strip()
            if text and len(text) > 10:
                lines.append(f"{text}\n")
            continue

        # 提取文本
        text_match = re.search(r'- text: (.+)$', line)
        if text_match:
            text = text_match.group(1).strip()
            if text and len(text) > 15:
                lines.append(f"{text}\n")
            continue

        # 提取图片
        img_match = re.search(r'- img(?:\s+"([^"]*)")?\s*$', line)
        if img_match:
            alt = img_match.group(1) or ''
            continue
        img_src_match = re.search(r'/url: (https://[^\s]+\.(png|jpg|jpeg|svg|webp))', line, re.I)
        if img_src_match:
            src = img_src_match.group(1)
            lines.append(f"![图片]({src})\n")
            continue

        # 提取链接文本
        link_match = re.search(r'link "([^"]+)"', line)
        if link_match:
            text = link_match.group(1)
            if len(text) > 20 and not any(kw in text for kw in skip_keywords):
                lines.append(f"{text}\n")
            continue

    return '\n'.join(lines)


def html_to_markdown(html: str, base_url: str = '') -> str:
    """将 HTML 转换为 Markdown"""
    from markdownify import markdownify as md
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, 'html.parser')

    # 移除无用元素
    for tag in soup.find_all(['script', 'style', 'noscript', 'iframe']):
        tag.decompose()

    # 移除导航、页头、页脚、侧边栏等
    for selector in ['nav', 'header', 'footer', '.tpm-topbar', '.tpm-footer',
                     '.qc-header', '.qc-footer', '[class*="-nav"]', '[class*="topbar"]',
                     '[class*="sidebar"]', '[class*="breadcrumb"]', '[class*="back-top"]',
                     '[class*="page-nav"]', '[class*="anchor"]', '[class*="float"]',
                     '[class*="fixed"]', '[class*="sticky"]', 'aside']:
        for tag in soup.select(selector):
            tag.decompose()

    # 转换相对 URL 为绝对 URL
    if base_url:
        for img in soup.find_all('img'):
            src = img.get('src', '')
            if src and not src.startswith(('http://', 'https://', 'data:')):
                img['src'] = base_url.rstrip('/') + '/' + src.lstrip('/')

    # 转换为 Markdown
    markdown = md(str(soup), heading_style='ATX', bullets='-')

    # 清理：找到第一个 h1 或 h2，删除之前的内容
    lines = markdown.split('\n')
    start_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('# ') or line.startswith('## '):
            start_idx = i
            break
    lines = lines[start_idx:]

    # 清理无用内容
    skip_patterns = ['页面导航', '回到顶部', '返回顶部', '联系销售', '在线咨询',
                     '非常不满意', '非常满意', '您对当前页面', '立即购买', '立即选购',
                     '立即开通', '免费试用', '免费体验', '查看详情', '了解更多',
                     '元/年', '元/月', '入门体验', '观看视频']
    skip_link_patterns = ['buy.cloud.tencent.com', 'console.cloud.tencent.com',
                          'javascript:', 'act/pro', '/act/']

    cleaned = []
    prev_empty = False
    skip_section = False

    for line in lines:
        stripped = line.strip()

        # 跳过页面导航区块
        if '页面导航' in line:
            skip_section = True
            continue
        if skip_section:
            if line.startswith('#'):
                skip_section = False
            else:
                continue

        # 跳过特定内容
        if any(p in stripped for p in skip_patterns):
            continue

        # 跳过营销链接
        if stripped.startswith('[') and any(p in stripped for p in skip_link_patterns):
            continue

        # 跳过纯链接行（如 [xxx](url) 格式且内容很短）
        if stripped.startswith('[') and stripped.endswith(')') and len(stripped) < 50:
            continue

        # 跳过只有短横线的列表项
        if stripped == '-':
            continue

        # 跳过 #### 标题（太细碎）
        if stripped.startswith('#### '):
            continue

        is_empty = not stripped
        if is_empty and prev_empty:
            continue

        cleaned.append(line)
        prev_empty = is_empty

    return '\n'.join(cleaned)


def get_main_content_html() -> str:
    """获取页面主内容区的 HTML"""
    js_cmd = '''agent-browser eval '
        // 腾讯云产品页主内容选择器
        var selectors = [
            "#app-root",
            ".product-detail-page",
            ".portal-wrap",
            "[class*=product]",
            "[class*=content]"
        ];
        var main = null;
        for (var i = 0; i < selectors.length; i++) {
            main = document.querySelector(selectors[i]);
            if (main && main.innerHTML.length > 1000) break;
        }
        if (!main || main.innerHTML.length < 500) {
            main = document.body;
        }
        // 克隆节点以便清理
        var clone = main.cloneNode(true);
        // 移除导航、页头、页脚等
        var removeSelectors = ["nav", "header", "footer", ".pls-nav", ".pls-topbar",
            ".pls-floatbar", "[id*=topnav]", "[id*=floatbar]", "[class*=topbar]",
            "[class*=sidebar]", "[class*=breadcrumb]", "[class*=back-top]",
            "[class*=page-nav]", "[class*=anchor]", "[class*=float]",
            "[class*=fixed]", "[class*=sticky]", "script", "style", "noscript", "iframe"];
        removeSelectors.forEach(function(sel) {
            clone.querySelectorAll(sel).forEach(function(el) { el.remove(); });
        });
        clone.innerHTML
    ' 2>/dev/null'''
    output = run_browser_command(js_cmd, timeout=30)
    if output:
        output = output.strip()
        if output.startswith('"'):
            try:
                return json.loads(output)
            except:
                return output[1:-1].replace('\\n', '\n').replace('\\"', '"') if output.endswith('"') else output
    return ''


def crawl_product(product: Dict, output_dir: Path) -> Optional[Path]:
    """爬取单个产品"""
    url = product.get('url', '')
    if not url:
        return None

    if not open_url(url, wait_ms=5000):
        print(f"  [错误] 无法打开页面")
        return None

    time.sleep(1)

    # 点击所有 tabs 触发懒加载
    run_browser_command('agent-browser eval "document.querySelectorAll(\'.tl-tabs__item-cont\').forEach(function(t){t.click()})" 2>/dev/null', timeout=15)
    time.sleep(1.5)

    # 获取页面标题
    title_output = run_browser_command('agent-browser eval "document.querySelector(\'h1\') ? document.querySelector(\'h1\').innerText.trim() : \'\'" 2>/dev/null', timeout=10)
    page_title = ''
    if title_output:
        page_title = title_output.strip().strip('"')

    # 获取主内容区 HTML
    html = get_main_content_html()
    if not html or len(html) < 200:
        print(f"  [警告] 页面内容为空")
        return None

    # 转换为 Markdown
    content = html_to_markdown(html, url)

    # 使用页面标题或产品目录中的标题
    title = page_title or product.get('title', '')

    # 去除内容开头的重复标题
    if title:
        content = re.sub(rf'^#\s*{re.escape(title)}\s*\n+', '', content, count=1)

    # 生成 Markdown
    markdown = f"""---
title: "{title}"
url: {url}
category: "{product.get('category_l1', '')}"
crawled_at: {datetime.now().isoformat()}
---

# {title}

{content}
"""

    # 确定保存路径
    category = get_category_dir(product.get('category_l1', ''))
    cat_dir = output_dir / category
    cat_dir.mkdir(parents=True, exist_ok=True)

    # 生成文件名
    name = product.get('title', '') or product.get('slug', '') or 'unknown'
    safe_name = sanitize_filename(name)
    filepath = cat_dir / f"{safe_name}.md"

    # 处理重名
    counter = 1
    while filepath.exists():
        filepath = cat_dir / f"{safe_name}_{counter}.md"
        counter += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown)

    return filepath


def main():
    """主函数"""
    import argparse
    parser = argparse.ArgumentParser(description='腾讯云产品详情爬虫')
    parser.add_argument('--limit', type=int, default=0, help='限制爬取数量')
    parser.add_argument('--skip-crawled', action='store_true', help='跳过已爬取的产品')
    parser.add_argument('--category', type=str, help='只爬取指定分类')
    parser.add_argument('--url', type=str, help='爬取单个URL')
    parser.add_argument('--list-only', action='store_true', help='只列出产品，不爬取')
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(exist_ok=True)

    # 单个 URL 模式
    if args.url:
        print(f"爬取单个URL: {args.url}")
        product = {
            'url': args.url,
            'title': '',
            'slug': '',
            'desc': '',
            'description': '',
            'category_l1': '测试',
            'category_l2': '',
        }
        filepath = crawl_product(product, OUTPUT_DIR)
        if filepath:
            print(f"保存到: {filepath}")
            with open(filepath) as f:
                print("\n" + "="*50)
                print(f.read())
        return

    # 获取产品目录
    catalog = fetch_product_catalog()
    if not catalog:
        print("无法获取产品目录，退出")
        return

    # 提取产品列表
    products = extract_products_from_tree(catalog)
    print(f"从目录提取到 {len(products)} 个产品")

    # 保存产品列表
    products_list_file = OUTPUT_DIR / 'products_list.json'
    with open(products_list_file, 'w', encoding='utf-8') as f:
        json.dump({'products': products, 'count': len(products)}, f, ensure_ascii=False, indent=2)

    if args.list_only:
        print("\n产品列表:")
        for i, p in enumerate(products, 1):
            print(f"  {i}. [{p.get('category_l1', '')}] {p.get('title', '')} - {p.get('url', '')}")
        return

    # 加载元数据
    metadata = load_crawl_metadata()
    crawled_urls = set(metadata.get('crawled_urls', []))

    print(f"已爬取数: {len(crawled_urls)}")

    # 过滤
    if args.category:
        products = [p for p in products if p.get('category_l1') == args.category]
        print(f"筛选分类 '{args.category}': {len(products)} 个产品")

    if args.skip_crawled:
        products = [p for p in products if p.get('url') not in crawled_urls]
        print(f"跳过已爬取: 剩余 {len(products)} 个产品")

    if args.limit > 0:
        products = products[:args.limit]
        print(f"限制数量: {len(products)} 个产品")

    if not products:
        print("没有需要爬取的产品")
        return

    print(f"\n开始爬取...")
    success_count = 0
    error_count = 0

    for i, product in enumerate(products, 1):
        url = product.get('url', '')
        name = product.get('title', '')
        print(f"[{i}/{len(products)}] {name}")

        try:
            filepath = crawl_product(product, OUTPUT_DIR)
            if filepath:
                print(f"  ✓ 保存: {filepath.relative_to(OUTPUT_DIR)}")
                crawled_urls.add(url)
                success_count += 1
            else:
                error_count += 1
        except Exception as e:
            print(f"  ✗ 异常: {e}")
            error_count += 1

        # 保存进度
        metadata['crawled_urls'] = list(crawled_urls)
        metadata['last_crawl'] = datetime.now().isoformat()
        metadata['total_products'] = len(products)
        save_crawl_metadata(metadata)

        time.sleep(RATE_LIMIT_SECONDS)

    print(f"\n爬取完成! 成功: {success_count}, 失败: {error_count}")


if __name__ == '__main__':
    main()
