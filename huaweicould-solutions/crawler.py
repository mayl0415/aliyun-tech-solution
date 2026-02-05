#!/usr/bin/env python3
"""华为云解决方案爬虫"""

import argparse
import hashlib
import json
import re
import subprocess
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from markdownify import markdownify as md

# 配置
BASE_URL = "https://www.huaweicloud.com"
OUTPUT_DIR = Path(__file__).parent / "solutions"
REQUEST_DELAY = 2.0  # 请求间隔秒数

# 目录页面
DIRECTORY_PAGES = [
    "https://www.huaweicloud.com/solution/technical-directory.html",
    "https://www.huaweicloud.com/solution/industry-directory.html",
    "https://www.huaweicloud.com/solution/reference-architecture.html",
]

# 排除的 URL 模式（目录页面等）
EXCLUDE_PATTERNS = [
    "technical-directory.html",
    "industry-directory.html",
    "reference-architecture.html",
]


def setup_dirs():
    """创建输出目录"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def get_links_from_page(url: str) -> set[str]:
    """使用 agent-browser 从页面 HTML 获取解决方案链接"""
    print(f"  获取链接: {url}")
    try:
        # 打开页面
        subprocess.run(
            ["agent-browser", "open", url],
            capture_output=True,
            text=True,
            timeout=60,
        )
        time.sleep(3)  # 等待页面加载

        # 从完整 HTML 中提取所有 solution 链接
        result = subprocess.run(
            ["agent-browser", "eval", "document.documentElement.outerHTML"],
            capture_output=True,
            text=True,
            timeout=60,
        )

        if result.returncode != 0:
            print(f"    获取链接失败: {result.stderr}")
            return set()

        # 用正则提取所有 /solution/*.html 链接
        html = result.stdout
        matches = re.findall(r'/solution/[a-z0-9\-/]+\.html', html, re.I)

        links = set()
        for m in matches:
            if not any(p in m for p in EXCLUDE_PATTERNS):
                full_url = "https://www.huaweicloud.com" + m
                links.add(full_url)

        return links
    except Exception as e:
        print(f"    错误: {e}")
        return set()


def collect_all_links() -> list[str]:
    """收集所有目录页面的链接并去重"""
    all_links = set()

    for url in DIRECTORY_PAGES:
        links = get_links_from_page(url)
        print(f"    找到 {len(links)} 个链接")
        all_links.update(links)
        time.sleep(REQUEST_DELAY)

    return sorted(all_links)


def get_page_content(url: str) -> tuple[str, str] | None:
    """使用 agent-browser 获取页面内容"""
    try:
        # 打开页面
        result = subprocess.run(
            ["agent-browser", "open", url],
            capture_output=True,
            text=True,
            timeout=60,
        )
        time.sleep(2)

        # 获取页面 HTML
        result = subprocess.run(
            ["agent-browser", "get", "html", "body"],
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode != 0:
            return None

        html = result.stdout

        # 获取标题
        title_result = subprocess.run(
            ["agent-browser", "get", "title"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        title = title_result.stdout.strip().strip('"') if title_result.returncode == 0 else ""

        return html, title
    except Exception as e:
        print(f"    获取页面失败: {e}")
        return None


def clean_content(soup: BeautifulSoup) -> BeautifulSoup:
    """清理无关内容"""
    selectors = [
        "header",
        "footer",
        "nav",
        "script",
        "style",
        "noscript",
        "[class*='header']",
        "[class*='footer']",
        "[class*='nav-']",
        "[class*='cookie']",
        "[class*='popup']",
        "[class*='modal']",
        "[class*='feedback']",
        "[class*='chat']",
        "[class*='contact']",
        "[class*='consultation']",
        "[id*='header']",
        "[id*='footer']",
        ".breadcrumb",
        ".sidebar",
    ]
    for selector in selectors:
        try:
            for elem in soup.select(selector):
                elem.decompose()
        except Exception:
            pass
    return soup


def html_to_markdown(html: str, source_url: str) -> str:
    """将 HTML 转换为 Markdown"""
    soup = BeautifulSoup(html, "html.parser")

    # 直接处理整个 body，不尝试找特定内容区域
    # 华为云页面结构复杂，内容分散在多个 div 中
    main_content = soup

    # 清理内容
    clean_content(main_content)

    # 处理图片，确保使用完整 URL
    for img in main_content.find_all("img"):
        src = img.get("src") or img.get("data-src") or ""
        if src:
            if src.startswith("//"):
                src = "https:" + src
            elif src.startswith("/"):
                src = urljoin(BASE_URL, src)
            img["src"] = src

    # 转换为 Markdown
    content = md(str(main_content), heading_style="ATX", bullets="-")

    # 清理多余空行
    content = re.sub(r"\n{3,}", "\n\n", content)

    return content.strip()


def extract_title(html: str, default_title: str) -> str:
    """提取页面标题"""
    soup = BeautifulSoup(html, "html.parser")

    # 尝试多种方式获取标题
    title_tag = soup.find("h1")
    if title_tag:
        return title_tag.get_text(strip=True)

    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text(strip=True)
        # 去掉常见后缀
        for suffix in ["-华为云", "_华为云", "- 华为云", "_ 华为云", "_解决方案", "-解决方案"]:
            if title.endswith(suffix):
                title = title[: -len(suffix)]
        return title

    return default_title or "未知标题"


def title_to_filename(title: str) -> str:
    """将标题转换为安全的文件名"""
    # 清理标题中的特殊字符，保留中文、字母、数字
    # 移除常见后缀
    for suffix in ["-华为云", "_华为云", "- 华为云", "_ 华为云", "_解决方案", "-解决方案"]:
        if title.endswith(suffix):
            title = title[: -len(suffix)]
    # 替换不能用于文件名的字符
    filename = re.sub(r'[\\/*?:"<>|]', "", title)
    filename = filename.replace(" ", "-").strip("-")
    return filename[:80]  # 限制长度


def save_solution(content: str, title: str, source_url: str, index: int) -> dict:
    """保存解决方案为 Markdown 文件"""
    filename = f"{index:03d}-{title_to_filename(title)}.md"
    filepath = OUTPUT_DIR / filename
    collected_at = datetime.now().strftime("%Y-%m-%d")

    # 构建文件内容
    file_content = f"""---
title: "{title}"
source_url: {source_url}
collected_at: {collected_at}
---

{content}
"""

    filepath.write_text(file_content, encoding="utf-8")

    return {
        "id": index,
        "title": title,
        "source_url": source_url,
        "filename": filename,
        "collected_at": collected_at,
        "content_hash": hashlib.md5(content.encode()).hexdigest(),
    }


def remove_duplicates(metadata_list: list[dict]) -> list[dict]:
    """删除重复内容的文件"""
    seen_hashes = {}
    unique_list = []
    removed = []

    for meta in metadata_list:
        content_hash = meta["content_hash"]
        if content_hash in seen_hashes:
            # 删除重复文件
            filepath = OUTPUT_DIR / meta["filename"]
            if filepath.exists():
                filepath.unlink()
                removed.append(meta["filename"])
        else:
            seen_hashes[content_hash] = meta["filename"]
            unique_list.append(meta)

    if removed:
        print(f"\n删除 {len(removed)} 个重复文件: {', '.join(removed)}")

    return unique_list


def crawl_solutions(limit: int | None = None, skip_collect: bool = False):
    """主爬取流程"""
    print("=" * 60)
    print("华为云解决方案爬虫")
    print("=" * 60)

    setup_dirs()
    parent_dir = Path(__file__).parent
    links_file = parent_dir / "solution_links.json"

    # 1. 收集或读取链接
    if skip_collect and links_file.exists():
        print("\n[1] 读取已保存的链接列表")
        all_links = json.loads(links_file.read_text(encoding="utf-8"))
        print(f"    共 {len(all_links)} 个链接")
    else:
        print("\n[1] 从目录页面收集链接")
        all_links = collect_all_links()
        print(f"\n    共找到 {len(all_links)} 个唯一解决方案链接")

        if not all_links:
            print("    无法获取解决方案链接")
            return

        # 保存链接列表
        links_file.write_text(json.dumps(all_links, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"    链接已保存到: {links_file}")

    # 应用限制
    if limit and limit < len(all_links):
        all_links = all_links[:limit]
        print(f"    限制爬取前 {limit} 个")

    # 2. 爬取每个解决方案
    print(f"\n[2] 开始爬取解决方案 (共 {len(all_links)} 个)")
    metadata_list = []

    for i, url in enumerate(all_links, 1):
        print(f"\n  [{i}/{len(all_links)}] {url}")

        time.sleep(REQUEST_DELAY)

        result = get_page_content(url)
        if not result:
            print("    跳过: 获取失败")
            continue

        html, page_title = result
        title = extract_title(html, page_title)

        # 跳过 404 页面
        if "404" in title or "页面不存在" in title or "not found" in title.lower():
            print(f"    跳过: 404 页面 ({title})")
            continue

        content = html_to_markdown(html, url)

        if len(content) < 100:
            print(f"    跳过: 内容过短 ({len(content)} 字符)")
            continue

        meta = save_solution(content, title, url, i)
        metadata_list.append(meta)
        print(f"    保存: {meta['filename']} ({len(content)} 字符)")

    # 3. 去重
    print("\n[3] 去重处理")
    metadata_list = remove_duplicates(metadata_list)

    # 4. 保存元数据
    metadata_path = parent_dir / "metadata.json"
    metadata = {
        "total": len(metadata_list),
        "collected_at": datetime.now().isoformat(),
        "source_pages": DIRECTORY_PAGES,
        "solutions": metadata_list,
    }
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n" + "=" * 60)
    print(f"完成! 共保存 {len(metadata_list)} 个解决方案")
    print(f"输出目录: {OUTPUT_DIR.absolute()}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="华为云解决方案爬虫")
    parser.add_argument("--limit", type=int, help="限制爬取数量")
    parser.add_argument("--skip-collect", action="store_true", help="跳过链接收集，使用已保存的链接")
    args = parser.parse_args()

    crawl_solutions(limit=args.limit, skip_collect=args.skip_collect)


if __name__ == "__main__":
    main()
