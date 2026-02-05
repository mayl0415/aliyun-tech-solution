#!/usr/bin/env python3
"""
阿里云产品爬虫 - 使用 agent-browser 爬取产品列表和详情页
"""

import json
import subprocess
import time
import re
import os
from pathlib import Path
from datetime import datetime


def run_browser_command(cmd: str, timeout: int = 30) -> str:
    """运行 agent-browser 命令"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return ""
    except Exception as e:
        print(f"Error running command: {e}")
        return ""


def get_page_snapshot() -> str:
    """获取当前页面快照"""
    return run_browser_command("agent-browser snapshot 2>/dev/null", timeout=30)


def open_url(url: str, wait_ms: int = 3000) -> str:
    """打开URL"""
    return run_browser_command(f'agent-browser open "{url}" --wait {wait_ms}', timeout=60)


def extract_product_links_from_snapshot(snapshot: str) -> list:
    """从快照中提取产品链接"""
    products = []
    lines = snapshot.split('\n')

    current_category = ""

    for line in lines:
        # 检测分类标题
        category_match = re.search(r'link "([^"]+) "', line)
        if category_match:
            cat = category_match.group(1).strip()
            # 检查是否是分类
            if cat in ['人工智能与机器学习', '计算', '容器', '存储', '网络与CDN', '安全',
                       '中间件', '数据库', '大数据计算', '媒体服务', '企业服务与云通信',
                       '域名与网站', '终端用户计算', '物联网', 'Serverless', '开发工具',
                       '迁移与运维管理', '专有云']:
                current_category = cat
                continue

        # 提取产品链接 - 匹配包含产品描述的链接
        # 格式: link "产品名称 描述..." [ref=eXX]
        product_match = re.search(r'link "([^"]+)" \[ref=e\d+\]', line)
        if product_match:
            text = product_match.group(1)
            # 过滤非产品链接
            if any(skip in text for skip in ['查看更多', '立即购买', '免费试用',
                                              '产品动态', '解决方案', '精选产品',
                                              'HOT', 'NEW', '登录', '注册']):
                continue
            # 产品描述通常较长
            if len(text) > 20 and current_category:
                products.append({
                    'name': text.split(' ')[0] if ' ' in text else text,
                    'description': text,
                    'category': current_category
                })

    return products


def parse_product_list_page() -> dict:
    """解析产品列表页，提取分类和产品信息"""
    print("正在获取产品列表页...")
    open_url("https://www.aliyun.com/product/list", wait_ms=5000)
    time.sleep(2)

    snapshot = get_page_snapshot()

    # 从快照中解析产品信息
    categories = {}
    current_category = None

    lines = snapshot.split('\n')
    for line in lines:
        # 检测分类 - treeitem 格式
        cat_match = re.search(r'treeitem "  ([^"]+)\(\d+\)"', line)
        if cat_match:
            current_category = cat_match.group(1).strip()
            if current_category not in categories:
                categories[current_category] = []
            continue

        # 检测分类标题链接
        cat_link_match = re.search(r'link "([^"]+) " \[ref=', line)
        if cat_link_match:
            cat_name = cat_link_match.group(1).strip()
            if cat_name in ['人工智能与机器学习', '计算', '容器', '存储', '网络与CDN',
                           '安全', '中间件', '数据库', '大数据计算', '媒体服务',
                           '企业服务与云通信', '域名与网站', '终端用户计算', '物联网',
                           'Serverless', '开发工具', '迁移与运维管理', '专有云']:
                current_category = cat_name
                if current_category not in categories:
                    categories[current_category] = []
                continue

        # 检测产品链接
        if current_category:
            # 产品链接格式: link "产品名 描述..." [ref=eXX]
            prod_match = re.search(r'link "([^"]+)" \[ref=e(\d+)\]', line)
            if prod_match:
                text = prod_match.group(1)
                # 过滤掉非产品的链接
                skip_keywords = ['免费试用', '查看更多', '登录', '注册', '控制台',
                                '文档', '备案', '产品', '解决方案', '权益', '定价',
                                '云市场', '伙伴', '服务', '了解阿里云', '大模型',
                                'img ', '打开菜单']
                if any(kw in text for kw in skip_keywords) and len(text) < 50:
                    continue

                # 产品通常有详细描述
                if len(text) > 30:
                    # 提取产品名和描述
                    parts = text.split(' ', 1)
                    name = parts[0]
                    desc = parts[1] if len(parts) > 1 else ''

                    # 清理免费试用标记
                    name = name.replace('免费试用', '').strip()
                    desc = desc.replace('免费试用', '').strip()

                    categories[current_category].append({
                        'name': name,
                        'description': desc,
                        'full_text': text
                    })

    return categories


def load_existing_products() -> dict:
    """加载已有的产品数据"""
    db_path = Path(__file__).parent.parent / 'aliyun' / 'products_database.json'
    if db_path.exists():
        with open(db_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # 创建URL到产品的映射
            return {p['url']: p for p in data.get('products', [])}
    return {}


def get_product_detail(url: str) -> dict:
    """获取产品详情页内容"""
    print(f"  正在获取: {url}")
    open_url(url, wait_ms=3000)
    time.sleep(1.5)

    snapshot = get_page_snapshot()

    # 解析详情页内容
    detail = {
        'url': url,
        'title': '',
        'description': '',
        'features': [],
        'raw_content': ''
    }

    lines = snapshot.split('\n')
    content_lines = []

    for line in lines:
        # 清理行
        line = line.strip()
        if not line:
            continue

        # 提取文本内容
        text_match = re.search(r'(?:link|text|heading|paragraph) "([^"]+)"', line)
        if text_match:
            text = text_match.group(1)
            # 过滤导航和UI元素
            if len(text) > 10 and not any(skip in text for skip in
                ['登录', '注册', '控制台', '打开菜单', '[ref=']):
                content_lines.append(text)

    detail['raw_content'] = '\n'.join(content_lines[:100])  # 限制内容长度

    return detail


def save_product_markdown(product: dict, category: str, output_dir: Path):
    """保存产品为Markdown文件"""
    # 创建分类目录
    cat_dir = output_dir / category
    cat_dir.mkdir(parents=True, exist_ok=True)

    # 生成安全的文件名
    safe_name = re.sub(r'[<>:"/\\|?*]', '', product.get('short_title', product.get('name', 'unknown')))
    safe_name = safe_name[:50]  # 限制文件名长度

    filepath = cat_dir / f"{safe_name}.md"

    # 生成Markdown内容
    content = f"""---
title: {product.get('title', product.get('name', ''))}
url: {product.get('url', '')}
category: {category}
keywords: {product.get('keywords', '')}
crawled_at: {datetime.now().isoformat()}
---

# {product.get('short_title', product.get('name', ''))}

{product.get('description', '')}

"""

    if product.get('raw_content'):
        content += f"""
## 详细内容

{product.get('raw_content', '')}
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath


def main():
    """主函数"""
    output_dir = Path(__file__).parent / 'products'
    output_dir.mkdir(exist_ok=True)

    # 加载已有产品数据
    existing_products = load_existing_products()
    print(f"已加载 {len(existing_products)} 个已有产品数据")

    # 解析产品列表页
    categories = parse_product_list_page()
    print(f"\n发现 {len(categories)} 个分类")
    for cat, prods in categories.items():
        print(f"  - {cat}: {len(prods)} 个产品")

    # 保存分类信息
    metadata = {
        'categories': categories,
        'total_products': sum(len(p) for p in categories.values()),
        'crawled_at': datetime.now().isoformat()
    }

    with open(output_dir / 'metadata.json', 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print(f"\n元数据已保存到 {output_dir / 'metadata.json'}")

    # 爬取详情页并保存
    crawled_count = 0
    for url, product in existing_products.items():
        if crawled_count >= 5:  # 先测试5个
            break

        category = product.get('category_l1', '其他')
        if not category:
            category = '其他'

        # 获取详情
        detail = get_product_detail(url)
        product.update(detail)

        # 保存Markdown
        filepath = save_product_markdown(product, category, output_dir)
        print(f"  已保存: {filepath}")

        crawled_count += 1
        time.sleep(2.5)  # 限速

    print(f"\n爬取完成，共处理 {crawled_count} 个产品")


if __name__ == '__main__':
    main()
