#!/usr/bin/env python3
"""
华为云产品架构爬虫
爬取华为云产品详情页，主要获取架构图和产品描述
使用 requests + BeautifulSoup 直接抓取
"""

import json
import time
import re
import logging
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Tuple

# 配置
OUTPUT_DIR = Path(__file__).parent / 'products'
METADATA_FILE = OUTPUT_DIR / 'crawl_metadata.json'
LOG_FILE = Path(__file__).parent / 'crawl.log'
RATE_LIMIT_SECONDS = 2.5

# 产品列表 API
PRODUCTS_API = 'https://portal.huaweicloud.com/rest/cbc/portaldocdataservice/v1/books/items?appId=CHINA-ZH_CN'

# 文档中心 URL 模板
DOC_CENTER_URL = 'https://support.huaweicloud.com/progressive_knowledge/{code}.html'

# 请求 headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def fetch_page(url: str) -> Optional[str]:
    """获取页面 HTML"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        return response.text
    except Exception as e:
        logger.error(f"获取页面失败 {url}: {e}")
        return None


def fetch_products_list() -> List[Dict]:
    """从 API 获取产品列表"""
    try:
        response = requests.get(PRODUCTS_API, headers=HEADERS, timeout=30)
        response.raise_for_status()
        data = response.json()

        products = []
        for category in data.get('data', []):
            category_name = category.get('name', '')
            category_code = category.get('code', '')

            for product in category.get('products', []):
                products.append({
                    'code': product.get('code', ''),
                    'title': product.get('title', ''),
                    'uri': product.get('uri', ''),
                    'description': product.get('description', ''),
                    'category': category_name,
                    'category_code': category_code
                })

        return products
    except Exception as e:
        logger.error(f"获取产品列表失败: {e}")
        return []


def check_url_exists(url: str) -> bool:
    """检查 URL 是否存在"""
    try:
        response = requests.head(url, headers=HEADERS, timeout=10, allow_redirects=True)
        return response.status_code == 200
    except:
        return False


def find_intro_link_from_doc_center(html: str) -> Optional[str]:
    """
    从文档中心页面查找"了解 -> 什么是xxx"链接
    """
    soup = BeautifulSoup(html, 'html.parser')

    # 方法1: 查找包含"什么是"的链接
    for link in soup.find_all('a', href=True):
        text = link.get_text(strip=True)
        if '什么是' in text:
            href = link['href']
            if href.startswith('http'):
                return href
            elif href.startswith('/'):
                return f"https://support.huaweicloud.com{href}"

    # 方法2: 查找"了解"区域下的第一个链接
    learn_sections = soup.find_all(class_='step-subtitle')
    for section in learn_sections:
        if '了解' in section.get_text():
            parent = section.find_parent(class_='step-item')
            if parent:
                link = parent.find('a', href=True)
                if link:
                    href = link['href']
                    if href.startswith('http'):
                        return href
                    elif href.startswith('/'):
                        return f"https://support.huaweicloud.com{href}"

    return None


def find_intro_link_from_leftmenu(code: str) -> Optional[str]:
    """
    从左侧菜单接口获取"什么是xxx"或"产品介绍"链接
    接口: https://support.huaweicloud.com/{code}/v3_support_leftmenu_fragment.html
    """
    url = f'https://support.huaweicloud.com/{code}/v3_support_leftmenu_fragment.html'
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        if response.status_code != 200:
            return None

        html = response.text

        # 优先查找"什么是"链接
        match = re.search(r'href=["\']([^"\']+)["\'][^>]*>[^<]*什么是[^<]*</a>', html)
        if match:
            href = match.group(1)
            if href.startswith('http'):
                return href
            elif href.startswith('/'):
                return f"https://support.huaweicloud.com{href}"

        # 其次查找"产品介绍"链接（排除 javascript:）
        match = re.search(r'href=["\']([^"\']+)["\'][^>]*>产品介绍</a>', html)
        if match:
            href = match.group(1)
            if href.startswith('http') and 'javascript' not in href:
                return href
            elif href.startswith('/'):
                return f"https://support.huaweicloud.com{href}"

        # 查找 productdesc 链接
        match = re.search(r'href=["\']([^"\']*productdesc[^"\']+)["\']', html)
        if match:
            href = match.group(1)
            if href.startswith('http'):
                return href
            elif href.startswith('/'):
                return f"https://support.huaweicloud.com{href}"

    except Exception as e:
        logger.debug(f"获取左侧菜单失败 {code}: {e}")

    return None


def extract_images(soup: BeautifulSoup, base_url: str) -> List[str]:
    """提取页面中的图片"""
    images = []

    for img in soup.find_all('img', src=True):
        src = img['src']

        # 跳过小图标和装饰图
        if any(skip in src.lower() for skip in ['icon', 'logo', 'avatar', 'favicon', 'sprite', '.gif', '.svg']):
            continue

        # 转换相对路径为绝对路径
        if src.startswith('//'):
            src = 'https:' + src
        elif src.startswith('/'):
            from urllib.parse import urlparse
            parsed = urlparse(base_url)
            src = f"{parsed.scheme}://{parsed.netloc}{src}"
        elif not src.startswith('http'):
            continue

        # 跳过 data URI
        if src.startswith('data:'):
            continue

        images.append(src)

    return list(dict.fromkeys(images))  # 去重


def parse_product_page(html: str, url: str) -> Dict:
    """解析产品详情页"""
    soup = BeautifulSoup(html, 'html.parser')

    result = {
        'url': url,
        'title': '',
        'content': '',
        'images': []
    }

    # 提取标题
    title_tag = soup.find('h1') or soup.find('title')
    if title_tag:
        result['title'] = title_tag.get_text(strip=True)
        # 清理标题中的后缀
        result['title'] = re.sub(r'[-_|].*华为云.*$', '', result['title']).strip()

    # 查找主内容区域
    content_area = (
        soup.find('div', class_='content-detail') or
        soup.find('div', class_='doc-content') or
        soup.find('article') or
        soup.find('main') or
        soup.find('div', id='content')
    )

    if content_area:
        # 移除不需要的元素
        for elem in content_area.find_all(['script', 'style', 'nav', 'header', 'footer', 'aside']):
            elem.decompose()

        # 移除导航、面包屑、分享、反馈等区域
        remove_classes = [
            'nav', 'feedback', 'breadcrumb', 'sidebar', 'toc',
            'share', 'social', 'copy-link', 'doc-nav', 'doc-header',
            'page-header', 'doc-footer', 'related-doc'
        ]
        for class_name in remove_classes:
            for elem in content_area.find_all(class_=re.compile(class_name, re.I)):
                elem.decompose()

        # 移除特定 ID 的元素
        remove_ids = ['breadcrumb', 'share', 'docHeader', 'docFooter']
        for elem_id in remove_ids:
            elem = content_area.find(id=elem_id)
            if elem:
                elem.decompose()

        # 移除包含特定文字的链接区域（面包屑导航）
        for elem in content_area.find_all('a'):
            if elem.get('href') == '/index.html':
                parent = elem.find_parent('p') or elem.find_parent('div')
                if parent and len(parent.get_text()) < 200:
                    parent.decompose()
                    break

        # 提取图片
        result['images'] = extract_images(content_area, url)

        # 转换为 Markdown
        content_html = str(content_area)
        result['content'] = md(content_html, heading_style='ATX', strip=['script', 'style'])

        # 清理 Markdown
        content = result['content']

        # 移除开头的面包屑和日期信息
        lines = content.split('\n')
        clean_lines = []
        skip_header = True
        for line in lines:
            # 跳过开头的面包屑、日期、分享等
            if skip_header:
                if any(skip in line for skip in [
                    '文档首页', '/index.html', '更新时间：', '查看PDF',
                    '分享', '微博', '微信', '复制链接', '链接复制成功',
                    'GMT+08:00'
                ]):
                    continue
                if line.strip().startswith('[') and ']/' in line:
                    continue
                if line.strip() == '' or line.strip() == '*':
                    continue
                # 遇到实际内容，停止跳过
                if line.strip().startswith('#') or len(line.strip()) > 20:
                    skip_header = False
            if not skip_header:
                clean_lines.append(line)

        content = '\n'.join(clean_lines)

        # 移除多余空行
        content = re.sub(r'\n{3,}', '\n\n', content)

        # 移除页脚内容
        footer_markers = ['意见反馈', '文档反馈', '上一篇', '下一篇', '父主题', '相关文档']
        for marker in footer_markers:
            pos = content.find(marker)
            if pos > 0:
                content = content[:pos]

        result['content'] = content.strip()

    return result


def generate_markdown(product: Dict, page_content: Dict) -> str:
    """生成 Markdown 文件"""
    title = page_content.get('title') or product.get('title', '')

    md_text = f"""---
title: "{title.replace('"', '\\"')}"
code: "{product.get('code', '')}"
category: "{product.get('category', '')}"
source_url: "{page_content.get('url', '')}"
crawled_at: "{datetime.now().isoformat()}"
---

# {title}

"""

    # 产品简介（来自 API）
    if product.get('description'):
        md_text += f"""## 产品简介

{product.get('description')}

"""

    # 架构图
    images = page_content.get('images', [])
    if images:
        md_text += "## 产品图片\n\n"
        for i, img_url in enumerate(images[:10], 1):  # 最多10张
            md_text += f"![图片{i}]({img_url})\n\n"

    # 页面内容
    content = page_content.get('content', '')
    if content:
        md_text += f"""## 详细说明

{content}
"""

    return md_text


def load_crawl_metadata() -> Dict:
    """加载爬取元数据"""
    if METADATA_FILE.exists():
        with open(METADATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        'crawled_products': [],
        'failed_products': [],
        'last_crawl': None,
        'stats': {'success': 0, 'failed': 0}
    }


def save_crawl_metadata(metadata: Dict):
    """保存爬取元数据"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(METADATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)


def sanitize_filename(name: str) -> str:
    """生成安全的文件名"""
    safe = re.sub(r'[<>:"/\\|?*\r\n]', '', name)
    safe = re.sub(r'\s+', '_', safe).strip()
    return safe[:60]


def crawl_product(product: Dict) -> Tuple[bool, str, Optional[Path]]:
    """
    爬取单个产品
    返回: (是否成功, 消息, 文件路径)
    """
    code = product.get('code', '')
    title = product.get('title', '')

    if not code:
        return False, "产品代码为空", None

    target_url = None

    # 步骤1: 尝试访问文档中心，查找产品介绍链接
    doc_center_url = DOC_CENTER_URL.format(code=code)
    logger.info(f"  尝试文档中心: {doc_center_url}")

    doc_html = fetch_page(doc_center_url)
    if doc_html and 'Security Verification' not in doc_html:
        intro_link = find_intro_link_from_doc_center(doc_html)
        if intro_link:
            target_url = intro_link
            logger.info(f"  找到产品介绍: {intro_link}")

    # 步骤2: 如果没找到，尝试从左侧菜单接口获取
    if not target_url:
        logger.info(f"  尝试左侧菜单接口...")
        intro_link = find_intro_link_from_leftmenu(code)
        if intro_link:
            target_url = intro_link
            logger.info(f"  从左侧菜单找到: {intro_link}")

    # 步骤3: 如果还没找到，使用 API 返回的 uri
    if not target_url:
        uri = product.get('uri', '')
        if uri:
            # 尝试从 uri 构建产品描述页面 URL
            match = re.search(r'support\.huaweicloud\.com/([^/]+)/', uri)
            if match:
                product_code = match.group(1)
                # 尝试产品描述首页
                productdesc_url = f"https://support.huaweicloud.com/productdesc-{product_code}/"
                if check_url_exists(productdesc_url):
                    target_url = productdesc_url
                    logger.info(f"  使用产品描述页: {target_url}")

            if not target_url:
                target_url = uri
                logger.info(f"  使用备用链接: {target_url}")

    if not target_url:
        return False, "未找到产品详情页", None

    # 步骤3: 获取产品详情页
    html = fetch_page(target_url)
    if not html:
        return False, f"无法获取页面: {target_url}", None

    # 检查是否被安全验证阻止
    if 'Security Verification' in html or 'EdgeOne' in html:
        return False, f"页面被安全验证阻止: {target_url}", None

    # 解析页面
    page_content = parse_product_page(html, target_url)

    if not page_content.get('content') and not page_content.get('images'):
        return False, "页面内容为空", None

    # 生成 Markdown
    md_content = generate_markdown(product, page_content)

    # 保存文件
    category = sanitize_filename(product.get('category', '其他'))
    cat_dir = OUTPUT_DIR / category
    cat_dir.mkdir(parents=True, exist_ok=True)

    # 使用 title 作为文件名，code 作为后缀确保唯一性
    file_title = sanitize_filename(title) if title else code
    filename = f"{file_title}_{code}.md"
    filepath = cat_dir / filename

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)

    return True, f"保存到 {filepath.relative_to(OUTPUT_DIR)}", filepath


def main():
    """主函数"""
    import argparse
    parser = argparse.ArgumentParser(description='华为云产品架构爬虫')
    parser.add_argument('--limit', type=int, default=0, help='限制爬取数量')
    parser.add_argument('--skip-crawled', action='store_true', help='跳过已爬取的产品')
    parser.add_argument('--category', type=str, help='只爬取指定分类')
    parser.add_argument('--code', type=str, help='爬取指定产品代码')
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    logger.info("=" * 60)
    logger.info("华为云产品架构爬虫启动")
    logger.info("=" * 60)

    # 获取产品列表
    logger.info("正在获取产品列表...")
    products = fetch_products_list()

    if not products:
        logger.error("获取产品列表失败，退出")
        return

    logger.info(f"获取到 {len(products)} 个产品")

    # 保存产品列表
    products_file = OUTPUT_DIR / 'products_list.json'
    with open(products_file, 'w', encoding='utf-8') as f:
        json.dump({'products': products, 'fetched_at': datetime.now().isoformat()}, f, ensure_ascii=False, indent=2)

    # 加载元数据
    metadata = load_crawl_metadata()
    crawled_codes = set(metadata.get('crawled_products', []))

    logger.info(f"已爬取: {len(crawled_codes)} 个产品")

    # 单个产品模式
    if args.code:
        products = [p for p in products if p.get('code') == args.code]
        if not products:
            logger.error(f"未找到产品代码: {args.code}")
            return

    # 分类过滤
    if args.category:
        products = [p for p in products if p.get('category') == args.category]
        logger.info(f"筛选分类 '{args.category}': {len(products)} 个产品")

    # 跳过已爬取
    if args.skip_crawled:
        products = [p for p in products if p.get('code') not in crawled_codes]
        logger.info(f"跳过已爬取: 剩余 {len(products)} 个产品")

    # 限制数量
    if args.limit > 0:
        products = products[:args.limit]
        logger.info(f"限制数量: {len(products)} 个产品")

    if not products:
        logger.info("没有需要爬取的产品")
        return

    logger.info(f"\n开始爬取 {len(products)} 个产品...")
    logger.info("-" * 60)

    success_count = 0
    failed_count = 0
    failed_products = []

    for i, product in enumerate(products, 1):
        code = product.get('code', '')
        title = product.get('title', '')
        category = product.get('category', '')

        logger.info(f"\n[{i}/{len(products)}] {title} ({code}) - {category}")

        try:
            success, message, filepath = crawl_product(product)

            if success:
                logger.info(f"  [SUCCESS] {message}")
                crawled_codes.add(code)
                success_count += 1
            else:
                logger.error(f"  [FAILED] {message}")
                failed_products.append({
                    'code': code,
                    'title': title,
                    'reason': message,
                    'time': datetime.now().isoformat()
                })
                failed_count += 1

        except Exception as e:
            logger.error(f"  [FAILED] 异常: {str(e)}")
            failed_products.append({
                'code': code,
                'title': title,
                'reason': str(e),
                'time': datetime.now().isoformat()
            })
            failed_count += 1

        # 更新元数据
        metadata['crawled_products'] = list(crawled_codes)
        metadata['failed_products'] = failed_products
        metadata['last_crawl'] = datetime.now().isoformat()
        metadata['stats'] = {'success': success_count, 'failed': failed_count}
        save_crawl_metadata(metadata)

        # 限速
        if i < len(products):
            time.sleep(RATE_LIMIT_SECONDS)

    # 打印统计
    logger.info("\n" + "=" * 60)
    logger.info("爬取完成!")
    logger.info(f"  成功: {success_count}")
    logger.info(f"  失败: {failed_count}")
    logger.info("=" * 60)

    # 打印失败列表
    if failed_products:
        logger.info("\n失败产品列表:")
        for fp in failed_products:
            logger.info(f"  - {fp['title']} ({fp['code']}): {fp['reason']}")


if __name__ == '__main__':
    main()
