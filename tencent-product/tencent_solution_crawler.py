#!/usr/bin/env python3
"""
腾讯云解决方案爬虫
从腾讯云产品目录 API 获取解决方案列表，爬取解决方案详情页并转换为 Markdown
支持点击 tab 获取完整内容
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
OUTPUT_DIR = Path(__file__).parent / 'solutions'
METADATA_FILE = OUTPUT_DIR / 'crawl_metadata.json'
RATE_LIMIT_SECONDS = 2.5
API_URL = 'https://qcloudimg.tencent-cloud.cn/scripts/qccomponents/v2/full-nav-tree.json'
SOLUTION_URL_PREFIX = 'https://cloud.tencent.com/solution/'


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


def get_main_content_html() -> str:
    """获取页面主内容区的 HTML"""
    js_cmd = '''agent-browser eval '
        // 腾讯云页面主内容选择器
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


def fetch_solution_catalog() -> List[Dict]:
    """从 API 获取解决方案目录"""
    print("正在获取解决方案目录...")
    try:
        resp = requests.get(API_URL, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, list) and len(data) > 1:
            second_item = data[1]
            if 'tree' in second_item:
                return second_item['tree']
        return data
    except Exception as e:
        print(f"获取解决方案目录失败: {e}")
        return []


def extract_solutions_from_tree(tree: List[Dict]) -> List[Dict]:
    """递归遍历目录树，提取所有解决方案"""
    solutions = []
    seen_links: Set[str] = set()

    def traverse(nodes: List[Dict], l1: str, l2: str):
        for node in nodes:
            node_type = node.get('type', '')
            dict_type = node.get('dictType', '')
            link = node.get('link', '')
            title = node.get('title', '')
            children = node.get('children', [])

            if (node_type == 'entry' and
                dict_type == 'solution' and
                link and
                link.startswith(SOLUTION_URL_PREFIX) and
                link not in seen_links):

                seen_links.add(link)
                solutions.append({
                    'title': title,
                    'slug': link.replace(SOLUTION_URL_PREFIX, '').strip('/'),
                    'url': link,
                    'desc': node.get('desc', ''),
                    'description': node.get('description', ''),
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

    traverse(tree, '', '')
    return solutions


def filter_images(images: List[str]) -> List[str]:
    """智能过滤图片，只保留有价值的图片"""
    result = []
    valid_extensions = ['.png', '.jpg', '.jpeg', '.webp']

    for url in images:
        url_lower = url.lower()

        # 过滤非图片 URL
        if '/product/' in url_lower and 'qcloudimg' not in url_lower:
            continue

        # 过滤 gif/apng
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


def load_crawl_metadata() -> Dict:
    """加载爬取元数据"""
    if METADATA_FILE.exists():
        with open(METADATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'crawled_urls': [], 'last_crawl': None, 'total_solutions': 0, 'errors': []}


def save_crawl_metadata(metadata: Dict):
    """保存爬取元数据"""
    METADATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(METADATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)


def crawl_solution(solution: Dict, output_dir: Path) -> Optional[Path]:
    """爬取单个解决方案"""
    url = solution.get('url', '')
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

    # 使用页面标题或目录中的标题
    title = page_title or solution.get('title', '')

    # 去除内容开头的重复标题
    if title:
        content = re.sub(rf'^#\s*{re.escape(title)}\s*\n+', '', content, count=1)

    # 生成 Markdown
    markdown = f"""---
title: "{title}"
slug: "{solution.get('slug', '')}"
url: {url}
category_l1: "{solution.get('category_l1', '')}"
category_l2: "{solution.get('category_l2', '')}"
crawled_at: {datetime.now().isoformat()}
---

# {title}

{content}
"""

    # 确定保存路径
    category = get_category_dir(solution.get('category_l1', ''))
    cat_dir = output_dir / category
    cat_dir.mkdir(parents=True, exist_ok=True)

    # 生成文件名
    name = solution.get('title', '') or solution.get('slug', '') or 'unknown'
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
    parser = argparse.ArgumentParser(description='腾讯云解决方案爬虫')
    parser.add_argument('--limit', type=int, default=0, help='限制爬取数量')
    parser.add_argument('--skip-crawled', action='store_true', help='跳过已爬取的解决方案')
    parser.add_argument('--category', type=str, help='只爬取指定分类')
    parser.add_argument('--url', type=str, help='爬取单个URL')
    parser.add_argument('--list-only', action='store_true', help='只列出解决方案，不爬取')
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(exist_ok=True)

    # 单个 URL 模式
    if args.url:
        print(f"爬取单个URL: {args.url}")
        solution = {
            'url': args.url,
            'title': '',
            'slug': '',
            'desc': '',
            'description': '',
            'category_l1': '测试',
            'category_l2': '',
        }
        filepath = crawl_solution(solution, OUTPUT_DIR)
        if filepath:
            print(f"保存到: {filepath}")
            with open(filepath) as f:
                print("\n" + "="*50)
                print(f.read())
        return

    # 获取解决方案目录
    catalog = fetch_solution_catalog()
    if not catalog:
        print("无法获取解决方案目录，退出")
        return

    # 提取解决方案列表
    solutions = extract_solutions_from_tree(catalog)
    print(f"从目录提取到 {len(solutions)} 个解决方案")

    # 保存解决方案列表
    solutions_list_file = OUTPUT_DIR / 'solutions_list.json'
    with open(solutions_list_file, 'w', encoding='utf-8') as f:
        json.dump({'solutions': solutions, 'count': len(solutions)}, f, ensure_ascii=False, indent=2)

    if args.list_only:
        print("\n解决方案列表:")
        for i, s in enumerate(solutions, 1):
            print(f"  {i}. [{s.get('category_l1', '')} > {s.get('category_l2', '')}] {s.get('title', '')} - {s.get('url', '')}")
        return

    # 加载元数据
    metadata = load_crawl_metadata()
    crawled_urls = set(metadata.get('crawled_urls', []))

    print(f"已爬取数: {len(crawled_urls)}")

    # 过滤
    if args.category:
        solutions = [s for s in solutions if s.get('category_l1') == args.category or s.get('category_l2') == args.category]
        print(f"筛选分类 '{args.category}': {len(solutions)} 个解决方案")

    if args.skip_crawled:
        solutions = [s for s in solutions if s.get('url') not in crawled_urls]
        print(f"跳过已爬取: 剩余 {len(solutions)} 个解决方案")

    if args.limit > 0:
        solutions = solutions[:args.limit]
        print(f"限制数量: {len(solutions)} 个解决方案")

    if not solutions:
        print("没有需要爬取的解决方案")
        return

    print(f"\n开始爬取...")
    success_count = 0
    error_count = 0

    for i, solution in enumerate(solutions, 1):
        url = solution.get('url', '')
        name = solution.get('title', '')
        print(f"[{i}/{len(solutions)}] {name}")

        try:
            filepath = crawl_solution(solution, OUTPUT_DIR)
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
        metadata['total_solutions'] = len(solutions)
        save_crawl_metadata(metadata)

        time.sleep(RATE_LIMIT_SECONDS)

    print(f"\n爬取完成! 成功: {success_count}, 失败: {error_count}")


if __name__ == '__main__':
    main()
