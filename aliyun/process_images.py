#!/usr/bin/env python3
"""处理爬取的Markdown文件中的图片"""

import re
import time
from pathlib import Path
from urllib.parse import urlparse

import requests

OUTPUT_DIR = Path("arch-solutions")
RAW_DIR = OUTPUT_DIR / "raw"
IMG_DIR = OUTPUT_DIR / "images"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}


def process_markdown_files():
    """处理所有Markdown文件"""
    IMG_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted(RAW_DIR.glob("solution-*.md"))
    print(f"共 {len(md_files)} 个文件待处理\n")

    for md_file in md_files:
        print(f"处理: {md_file.name}")
        content = md_file.read_text(encoding="utf-8")
        original_content = content

        # 1. 删除小图标（tech-solution-images/icons/ 路径）
        icon_pattern = r'!\[.*?\]\([^)]*tech-solution-images/icons/[^)]+\)\n*'
        content = re.sub(icon_pattern, '', content)

        # 2. 删除列表项中的图片（- ![](...)）
        list_img_pattern = r'^- !\[.*?\]\([^)]+\)\s*$\n?'
        content = re.sub(list_img_pattern, '', content, flags=re.MULTILINE)

        # 3. 删除特性小图标（图片后面紧跟 **标题** 的模式）
        # 匹配: ![](url)\n\n**标题**
        feature_icon_pattern = r'!\[.*?\]\([^)]+\)\n+\*\*[^*]+\*\*'
        content = re.sub(feature_icon_pattern, lambda m: m.group().split('\n')[-1], content)

        # 4. 提取架构图URL（排除GIF）
        # 架构图是独立一行且后面不是 **标题**
        lines = content.split('\n')
        arch_urls = []
        for i, line in enumerate(lines):
            match = re.match(r'^!\[.*?\]\((https?://[^)]+)\)$', line.strip())
            if match:
                url = match.group(1)
                # 跳过 GIF
                if url.lower().endswith('.gif'):
                    continue
                # 跳过小图标路径
                if 'tech-solution-images/icons' in url:
                    continue
                # 检查下一行是否是 **标题**（如果是则跳过）
                next_line = lines[i + 1].strip() if i + 1 < len(lines) else ''
                if re.match(r'^\*\*[^*]+\*\*$', next_line):
                    continue
                arch_urls.append(url)

        # 下载架构图
        base_name = md_file.stem  # solution-001
        for idx, img_url in enumerate(arch_urls):
            ext = Path(urlparse(img_url).path).suffix or '.png'
            if idx == 0:
                img_name = f"{base_name}{ext}"
            else:
                img_name = f"{base_name}-{idx+1}{ext}"

            img_path = IMG_DIR / img_name

            if not img_path.exists():
                try:
                    print(f"  下载架构图: {img_name}")
                    resp = requests.get(img_url, headers=HEADERS, timeout=30)
                    resp.raise_for_status()
                    img_path.write_bytes(resp.content)
                    time.sleep(0.3)
                except Exception as e:
                    print(f"  下载失败: {e}")

        # 5. 清理多余空行
        content = re.sub(r'\n{3,}', '\n\n', content)

        # 保存修改后的文件
        if content != original_content:
            md_file.write_text(content, encoding="utf-8")
            print(f"  已更新")

    print(f"\n完成！架构图保存在: {IMG_DIR}")


if __name__ == "__main__":
    process_markdown_files()
