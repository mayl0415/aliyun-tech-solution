#!/usr/bin/env python3
"""
阿里云产品详情页爬虫 v2
改进的内容提取逻辑，提取更完整的页面信息
"""

import json
import subprocess
import time
import re
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List


# 配置
OUTPUT_DIR = Path(__file__).parent / 'products_v2'
METADATA_FILE = OUTPUT_DIR / 'crawl_metadata.json'
RATE_LIMIT_SECONDS = 2.5


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
        # 清理输出（去掉引号和转义）
        output = output.strip().strip('"').replace('\\n', '\n')
        images = [url.strip() for url in output.split('\n') if url.strip()]
        return images
    return []


def filter_product_images(images: List[str]) -> List[str]:
    """
    智能过滤图片，只保留有价值的图片（架构图、产品截图等）
    过滤掉：gif、小图标、logo、合作伙伴图片等
    """
    result = []

    for url in images:
        # 1. 过滤gif动画
        if '.gif' in url.lower():
            continue

        # 2. 过滤svg图标
        if '.svg' in url.lower():
            continue

        # 3. 过滤apng动画
        if '.apng' in url.lower():
            continue

        # 4. 尝试从URL末尾提取尺寸信息
        # 阿里云CDN格式: xxx-宽度-高度.扩展名 或 tps-宽度-高度.扩展名
        # 例如: TB1cOlBoLzO3e4jSZFxXXaP_FXa-2054-1452.png
        # 或: O1CN01vBbQLH1XUcOADg2M5_!!6000000002927-2-tps-460-544.png
        size_match = re.search(r'-(\d{2,4})-(\d{2,4})\.\w+$', url)
        if size_match:
            width = int(size_match.group(1))
            height = int(size_match.group(2))

            # 过滤太小的图片（图标、logo等）
            # 合作伙伴logo通常是 220x90, 440x180 等扁平尺寸
            # 小图标通常是 112x112, 60x60, 36x36 等正方形小尺寸
            # 保留条件：宽度>=450 或 高度>=350（宽松条件，保留窄但高的架构图）
            if width < 450 and height < 350:
                continue

            # 过滤宽高比极端的图片（通常是banner或logo条）
            # 正常的架构图/截图宽高比在 0.2 到 5 之间
            ratio = width / height
            if ratio > 5 or ratio < 0.2:
                continue

            result.append(url)
        else:
            # 无法解析尺寸的图片，保留（可能是有价值的图）
            result.append(url)

    # 去重
    return list(dict.fromkeys(result))


def parse_product_page_v2(snapshot: str, url: str, images: List[str] = None) -> Dict:
    """
    改进的页面解析逻辑
    提取：标题、简介、产品架构、核心功能、行业方案、客户案例等
    """
    result = {
        'url': url,
        'title': '',
        'intro': '',
        'sections': [],
        'features': [],
        'solutions': [],
        'cases': [],
        'images': images or []
    }

    lines = snapshot.split('\n')

    # 页脚开始标记 - 跳过页脚后的内容
    footer_keywords = ['contentinfo', '页尾', '为什么选择阿里云', '关注阿里云', '法律声明']
    # 推荐模块标记（二级标题形式的推荐模块，在页面底部出现）
    # 注意：只有完全匹配或以"大模型"开头的才算页脚
    promo_section_keywords = ['解决方案', '权益', '定价', '云市场', '伙伴', '了解阿里云']
    # 三级标题形式的页脚标记
    promo_h3_keywords = ['大模型', '产品', '服务']
    # 推荐内容关键词
    promo_keywords = ['大模型服务平台百炼', 'AI 体验馆', '通义大模型', '通义千问',
                      'DeepSeek', 'Dify', '快速部署', '微调', '通义万相', '通义灵码',
                      '云服务器38元', '补贴', '免费试用', 'tokens', '直降', '立减']
    # UI文本过滤
    ui_keywords = ['继续滚动', '上一个页面', '下一个页面', '点击查看', '立即查看', '立即咨询']

    in_footer = False
    current_section = None
    section_content = []
    seen_content = set()  # 用于去重

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 检测是否进入页脚
        if any(kw in line for kw in footer_keywords):
            in_footer = True
            continue

        if in_footer:
            continue

        # 跳过推荐模块
        if any(kw in line for kw in promo_keywords):
            continue

        # 提取一级标题（产品名）
        h1_match = re.search(r'heading "([^"]+)" \[ref=[^\]]+\] \[level=1\]', line)
        if h1_match:
            title = h1_match.group(1)
            # 清理标题中的装饰文字
            if not result['title'] and len(title) < 100:
                result['title'] = title.split('\n')[0].strip()
            continue

        # 提取二级标题（章节）
        h2_match = re.search(r'heading "([^"]+)" \[ref=[^\]]+\] \[level=2\]', line)
        if h2_match:
            section_title = h2_match.group(1)
            # 检查是否是推荐模块的标题
            if any(kw == section_title or section_title.startswith(kw) for kw in promo_section_keywords):
                in_footer = True  # 进入页脚推荐模块，停止提取
                continue
            # 保存上一个章节
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
            # 检查是否是页脚推荐模块的标题
            if text in promo_h3_keywords:
                # 保存当前章节并停止
                if current_section and section_content:
                    result['sections'].append({
                        'title': current_section,
                        'content': '\n'.join(section_content)
                    })
                in_footer = True
                current_section = None
                section_content = []
                continue
            if current_section and not in_footer:
                section_content.append(f"### {text}")
            continue

        # 提取text内容（主要信息）
        text_match = re.search(r'- text: (.+)$', line)
        if text_match:
            text = text_match.group(1).strip()
            if text and len(text) > 10:
                # 过滤UI文本和推荐内容
                skip = ['登录', '注册', '控制台', '立即购买', '免费试用', '查看更多',
                       '立即咨询', '我要咨询', '进入控制台', '页脚导航']
                skip.extend(ui_keywords)
                skip.extend(promo_keywords)
                if any(s in text for s in skip):
                    continue
                # 去重
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
                skip = ['商品优势', '商品功能', '应用场景', '资源包']
                if not any(s in text for s in skip):
                    if current_section:
                        section_content.append(text)
            continue

        # 提取gridcell内容（通常是产品特性或方案卡片）
        grid_match = re.search(r'gridcell "([^"]+)"', line)
        if grid_match:
            text = grid_match.group(1)
            if len(text) > 20:
                # 清理文本
                text = re.sub(r'\s+', ' ', text).strip()
                # 移除UI文本
                text = re.sub(r'\s*(立即查看|立即咨询|查看更多|了解更多)\s*$', '', text)
                # 去重
                text_key = text[:50]  # 用前50字符作为去重key
                if current_section and text and text_key not in seen_content:
                    seen_content.add(text_key)
                    section_content.append(f"- {text}")
            continue

        # 跳过row - gridcell已经包含了这些内容
        row_match = re.search(r'row "([^"]+)"', line)
        if row_match:
            continue

        # 提取listitem中的内容
        listitem_match = re.search(r'listitem:\s*$', line)
        if listitem_match and current_section:
            # 下一行可能有内容
            continue

    # 保存最后一个章节
    if current_section and section_content:
        result['sections'].append({
            'title': current_section,
            'content': '\n'.join(section_content)
        })

    return result


def generate_markdown_v2(product: Dict, page_content: Dict) -> str:
    """生成改进版Markdown"""
    # 使用页面标题或数据库标题
    title = page_content.get('title') or product.get('short_title') or product.get('title', '')

    md = f"""---
title: "{product.get('title', '').replace('"', '\\"')}"
short_title: "{product.get('short_title', '').replace('"', '\\"')}"
url: {product.get('url', '')}
category_l1: "{product.get('category_l1', '')}"
category_l2: "{product.get('category_l2', '')}"
keywords: "{product.get('keywords', '')}"
crawled_at: {datetime.now().isoformat()}
---

# {title}

"""

    # 产品简介
    intro = page_content.get('intro') or product.get('description', '')
    if intro:
        md += f"""## 产品简介

{intro}

"""

    # 产品图标
    if product.get('image'):
        md += f"""## 产品图标

![产品图标]({product.get('image')})

"""

    # 产品图片（架构图等）- 已在parse阶段过滤
    images = page_content.get('images', [])
    if images:
        md += "## 产品图片\n\n"
        for i, img_url in enumerate(images[:8], 1):  # 最多8张
            md += f"![图片{i}]({img_url})\n\n"

    # 需要排除的页脚章节
    footer_sections = ['大模型', '产品', '解决方案', '权益', '定价', '云市场', '伙伴', '服务', '了解阿里云']

    # 各个章节
    for section in page_content.get('sections', []):
        section_title = section.get('title', '')
        section_content = section.get('content', '')

        # 跳过页脚章节
        if section_title in footer_sections:
            continue

        # 清理内容中的页脚推荐
        if section_content:
            # 检查内容中是否有页脚标记（### 大模型 等）
            for footer_marker in footer_sections:
                marker_pos = section_content.find(f'### {footer_marker}')
                if marker_pos >= 0:
                    section_content = section_content[:marker_pos].strip()

        if section_title and section_content:
            md += f"""## {section_title}

{section_content}

"""

    return md


def load_crawl_metadata() -> Dict:
    """加载爬取元数据"""
    if METADATA_FILE.exists():
        with open(METADATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'crawled_urls': [], 'last_crawl': None, 'errors': []}


def save_crawl_metadata(metadata: Dict):
    """保存爬取元数据"""
    with open(METADATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)


def load_products_database() -> List[Dict]:
    """加载产品数据库"""
    # 优先使用包含分类信息的数据库
    db_path = Path(__file__).parent.parent / 'aliyun' / 'products_database.json'
    if db_path.exists():
        with open(db_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('products', [])

    # 备用：本地产品列表
    local_path = Path(__file__).parent / 'products_list.json'
    if local_path.exists():
        with open(local_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('products', [])

    return []


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


def crawl_product(product: Dict, output_dir: Path) -> Optional[Path]:
    """爬取单个产品"""
    url = product.get('url', '')
    if not url:
        return None

    if not open_url(url, wait_ms=4000):
        print(f"  [错误] 无法打开页面")
        return None

    time.sleep(1.5)

    snapshot = get_page_content()
    if not snapshot:
        print(f"  [警告] 页面内容为空")
        return None

    # 获取页面图片并过滤
    images = get_page_images()
    filtered_images = filter_product_images(images)

    # 解析页面
    page_content = parse_product_page_v2(snapshot, url, filtered_images)

    # 生成Markdown
    markdown = generate_markdown_v2(product, page_content)

    # 确定保存路径
    category = get_category_dir(product.get('category_l1', ''))
    cat_dir = output_dir / category
    cat_dir.mkdir(parents=True, exist_ok=True)

    # 生成文件名
    name = product.get('short_title', '') or product.get('title', '') or 'unknown'
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
    parser = argparse.ArgumentParser(description='阿里云产品详情爬虫 v2')
    parser.add_argument('--limit', type=int, default=0, help='限制爬取数量')
    parser.add_argument('--skip-crawled', action='store_true', help='跳过已爬取的产品')
    parser.add_argument('--category', type=str, help='只爬取指定分类')
    parser.add_argument('--url', type=str, help='爬取单个URL')
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(exist_ok=True)

    # 单个URL模式
    if args.url:
        print(f"爬取单个URL: {args.url}")
        # 创建临时产品数据
        product = {
            'url': args.url,
            'title': '',
            'short_title': '',
            'description': '',
            'category_l1': '测试',
            'keywords': ''
        }
        filepath = crawl_product(product, OUTPUT_DIR)
        if filepath:
            print(f"保存到: {filepath}")
            # 显示文件内容
            with open(filepath) as f:
                print("\n" + "="*50)
                print(f.read())
        return

    # 批量模式
    products = load_products_database()
    metadata = load_crawl_metadata()
    crawled_urls = set(metadata.get('crawled_urls', []))

    print(f"产品总数: {len(products)}")
    print(f"已爬取数: {len(crawled_urls)}")

    if args.category:
        products = [p for p in products if p.get('category_l1') == args.category]
        print(f"筛选分类 '{args.category}': {len(products)} 个产品")

    if args.skip_crawled:
        products = [p for p in products if p.get('url') not in crawled_urls]
        print(f"跳过已爬取: 剩余 {len(products)} 个产品")

    if args.limit > 0:
        products = products[:args.limit]
        print(f"限制数量: {len(products)} 个产品")

    print(f"\n开始爬取...")
    success_count = 0
    error_count = 0

    for i, product in enumerate(products, 1):
        url = product.get('url', '')
        name = product.get('short_title', '') or product.get('title', '')
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

        metadata['crawled_urls'] = list(crawled_urls)
        metadata['last_crawl'] = datetime.now().isoformat()
        save_crawl_metadata(metadata)

        time.sleep(RATE_LIMIT_SECONDS)

    print(f"\n爬取完成! 成功: {success_count}, 失败: {error_count}")


if __name__ == '__main__':
    main()
