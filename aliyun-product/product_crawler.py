#!/usr/bin/env python3
"""
阿里云产品详情页爬虫
使用 agent-browser 爬取每个产品的详情页内容
支持增量爬取和断点续爬
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
OUTPUT_DIR = Path(__file__).parent / 'products'
METADATA_FILE = OUTPUT_DIR / 'crawl_metadata.json'
RATE_LIMIT_SECONDS = 2.5  # 请求间隔


def run_browser_command(cmd: str, timeout: int = 60) -> str:
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
        print(f"  [警告] 命令超时: {cmd[:50]}...")
        return ""
    except Exception as e:
        print(f"  [错误] 运行命令失败: {e}")
        return ""


def open_url(url: str, wait_ms: int = 3000) -> bool:
    """打开URL，返回是否成功"""
    output = run_browser_command(f'agent-browser open "{url}" --wait {wait_ms}', timeout=60)
    return '✓' in output or 'Error' not in output.lower()


def get_page_content() -> str:
    """获取页面文本内容"""
    return run_browser_command('agent-browser snapshot 2>/dev/null', timeout=30)


def parse_product_page(snapshot: str, url: str) -> Dict:
    """解析产品详情页内容"""
    result = {
        'url': url,
        'content_sections': [],
        'features': [],
        'descriptions': []
    }

    # 需要过滤的内容关键词
    skip_keywords = [
        '登录', '注册', '控制台', '打开菜单', '免费试用', '立即购买',
        '查看更多', '产品动态', '产品文档', 'img ', '备案', '浙公网安备',
        '京ICP', '网站地图', '隐私政策', '服务条款', '联系我们', '关于我们',
        '电商营销', '广告创作', '短剧', 'AI coding', 'AI 办公', '智能客服',
        '企业上云', '补贴', '出海', '组合购', '老友焕新', '权益中心',
        '定价', '价格计算', '成本管理', '云市场', '伙伴', 'AI 体验馆',
        '通义万相', '通义千问', '通义灵码', '通义星尘', '通义听悟', '通义晓蜜',
        '大模型服务平台百炼', '产品定价', '免费', 'HOT', 'NEW',
        '售前咨询', '售后在线', '我要建议', '我要投诉', '快捷注册', '登录阿里云',
        # 相关产品推荐
        '人工智能平台 PAI', '快速部署 Dify', 'DeepSeek', '微调',
        '云数据库 RDS', '云解析 DNS', 'MaxCompute', '实时音视频通话',
        '聊天系统', '安全防护体系', 'Bolt.diy', '多模态数据信息提取',
        # 活动和促销
        '采购季', '优惠折扣', '包年更优惠', '钉群'
    ]

    lines = snapshot.split('\n')

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 提取链接文本
        link_match = re.search(r'link "([^"]+)" \[ref=', line)
        if link_match:
            text = link_match.group(1)
            # 过滤UI元素和无关内容
            if len(text) > 25 and not any(skip in text for skip in skip_keywords):
                # 只保留与产品相关的内容
                result['descriptions'].append(text)

        # 提取heading
        heading_match = re.search(r'heading "([^"]+)"', line)
        if heading_match:
            text = heading_match.group(1)
            if text and len(text) > 2 and not any(skip in text for skip in skip_keywords):
                result['content_sections'].append(('heading', text))

        # 提取paragraph/text
        text_match = re.search(r'(?:paragraph|text) "([^"]+)"', line)
        if text_match:
            text = text_match.group(1)
            if len(text) > 30 and not any(skip in text for skip in skip_keywords):
                result['content_sections'].append(('paragraph', text))

    return result


def generate_markdown(product: Dict, page_content: Dict) -> str:
    """生成产品的Markdown内容"""
    md = f"""---
title: "{product.get('title', '').replace('"', '\\"')}"
short_title: "{product.get('short_title', '').replace('"', '\\"')}"
url: {product.get('url', '')}
category_l1: "{product.get('category_l1', '')}"
category_l2: "{product.get('category_l2', '')}"
keywords: "{product.get('keywords', '')}"
crawled_at: {datetime.now().isoformat()}
---

# {product.get('short_title', product.get('title', '未知产品'))}

"""

    # 产品描述
    if product.get('description'):
        md += f"""## 产品简介

{product.get('description')}

"""

    # 产品图片
    if product.get('image'):
        md += f"""## 产品图标

![产品图标]({product.get('image')})

"""

    # 详情页内容
    if page_content.get('descriptions'):
        md += "## 产品详情\n\n"
        seen = set()
        for desc in page_content['descriptions'][:20]:  # 限制数量
            # 去重
            if desc in seen or len(desc) < 30:
                continue
            seen.add(desc)
            md += f"- {desc}\n\n"

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
    db_path = Path(__file__).parent.parent / 'aliyun' / 'products_database.json'
    if db_path.exists():
        with open(db_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('products', [])
    return []


def sanitize_filename(name: str) -> str:
    """生成安全的文件名"""
    # 移除不安全字符
    safe = re.sub(r'[<>:"/\\|?*\r\n]', '', name)
    # 移除多余空格
    safe = re.sub(r'\s+', ' ', safe).strip()
    # 限制长度
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

    # 打开页面
    if not open_url(url, wait_ms=3000):
        print(f"  [错误] 无法打开页面: {url}")
        return None

    time.sleep(1)  # 等待页面加载

    # 获取页面内容
    snapshot = get_page_content()
    if not snapshot:
        print(f"  [警告] 页面内容为空: {url}")

    # 解析页面
    page_content = parse_product_page(snapshot, url)

    # 生成Markdown
    markdown = generate_markdown(product, page_content)

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

    # 保存文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown)

    return filepath


def main():
    """主函数"""
    import argparse
    parser = argparse.ArgumentParser(description='阿里云产品详情爬虫')
    parser.add_argument('--limit', type=int, default=0, help='限制爬取数量，0表示全部')
    parser.add_argument('--skip-crawled', action='store_true', help='跳过已爬取的产品')
    parser.add_argument('--category', type=str, help='只爬取指定分类')
    args = parser.parse_args()

    # 创建输出目录
    OUTPUT_DIR.mkdir(exist_ok=True)

    # 加载数据
    products = load_products_database()
    metadata = load_crawl_metadata()
    crawled_urls = set(metadata.get('crawled_urls', []))

    print(f"产品总数: {len(products)}")
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

    # 开始爬取
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
                print(f"  ✗ 爬取失败")
                metadata.setdefault('errors', []).append({
                    'url': url,
                    'time': datetime.now().isoformat(),
                    'error': 'crawl_failed'
                })
                error_count += 1
        except Exception as e:
            print(f"  ✗ 异常: {e}")
            metadata.setdefault('errors', []).append({
                'url': url,
                'time': datetime.now().isoformat(),
                'error': str(e)
            })
            error_count += 1

        # 保存进度
        metadata['crawled_urls'] = list(crawled_urls)
        metadata['last_crawl'] = datetime.now().isoformat()
        save_crawl_metadata(metadata)

        # 限速
        time.sleep(RATE_LIMIT_SECONDS)

    print(f"\n爬取完成!")
    print(f"  成功: {success_count}")
    print(f"  失败: {error_count}")
    print(f"  输出目录: {OUTPUT_DIR}")


if __name__ == '__main__':
    main()
