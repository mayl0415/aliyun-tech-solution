#!/usr/bin/env python3
"""阿里云解决方案爬虫"""

import json
import re
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# 配置
BASE_URL = "https://www.aliyun.com"
MENU_API_URL = "https://developer.aliyun.com/adc/api/skillBuilder/getMenuTree?aliyun_lang=zh"
OUTPUT_DIR = Path("arch-solutions")
RAW_DIR = OUTPUT_DIR / "raw"
REQUEST_DELAY = 2.5  # 请求间隔秒数

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}


def setup_dirs():
    """创建输出目录"""
    RAW_DIR.mkdir(parents=True, exist_ok=True)


def fetch_solution_list_from_api() -> list[dict]:
    """从API获取解决方案列表"""
    print(f"    请求API: {MENU_API_URL}")
    try:
        response = requests.get(MENU_API_URL, headers=HEADERS, timeout=30)
        response.raise_for_status()
        data = response.json()

        solutions = []
        seen_urls = set()

        def extract_solutions(node):
            """递归提取所有 SOLUTION_DETAIL 类型的节点"""
            if not isinstance(node, dict):
                return
            # 检查当前节点
            if node.get("type") == "SOLUTION_DETAIL" and node.get("url"):
                url = node["url"]
                # 只保留一级目录 /solution/tech-solution/xxx
                path = urlparse(url).path.rstrip("/")
                parts = path.split("/")
                if len(parts) == 4 and parts[2] == "tech-solution" and url not in seen_urls:
                    seen_urls.add(url)
                    solutions.append({
                        "title": node.get("title", ""),
                        "url": url,
                        "type": node.get("type", ""),
                    })
            # 递归处理子节点
            if "children" in node and isinstance(node["children"], list):
                for child in node["children"]:
                    extract_solutions(child)

        # 遍历所有顶级节点
        if "data" in data and isinstance(data["data"], list):
            for item in data["data"]:
                extract_solutions(item)

        return solutions
    except Exception as e:
        print(f"    API请求失败: {e}")
        import traceback
        traceback.print_exc()
        return []


def fetch_page(url: str) -> str | None:
    """获取页面内容"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"  获取失败: {url} - {e}")
        return None


def extract_solution_links(html: str) -> list[dict]:
    """从列表页提取解决方案链接（只保留一级目录）"""
    soup = BeautifulSoup(html, "html.parser")
    solutions = []
    seen_urls = set()

    # 查找所有解决方案链接
    for a in soup.find_all("a", href=True):
        href = a.get("href", "")
        # 匹配 /solution/tech-solution/xxx 一级目录
        if "/solution/tech-solution/" in href and href != "/solution/tech-solution/":
            full_url = urljoin(BASE_URL, href.split("?")[0])  # 去掉查询参数
            # 只保留一级目录: /solution/tech-solution/xxx，不要 /solution/tech-solution/xxx/yyy
            path = urlparse(full_url).path.rstrip("/")
            parts = path.split("/")
            # 正确的路径应该是 ['', 'solution', 'tech-solution', 'xxx']
            if len(parts) == 4 and parts[1] == "solution" and parts[2] == "tech-solution" and parts[3]:
                if full_url not in seen_urls:
                    seen_urls.add(full_url)
                    title = a.get_text(strip=True) or parts[3]
                    solutions.append({"url": full_url, "title": title})

    return solutions


def clean_content(soup: BeautifulSoup) -> BeautifulSoup:
    """清理无关内容"""
    # 移除导航、页脚、脚本等
    for selector in [
        "header",
        "footer",
        "nav",
        "script",
        "style",
        "noscript",
        ".aliyun-header",
        ".aliyun-footer",
        ".aliyun-nav",
        "#aliyun-header",
        "#aliyun-footer",
        ".breadcrumb",
        ".side-nav",
        ".sidebar",
        ".comment",
        ".related",
        ".ad",
        ".advertisement",
        "[class*='cookie']",
        "[class*='popup']",
        "[class*='modal']",
    ]:
        for elem in soup.select(selector):
            elem.decompose()
    return soup


def html_to_markdown(html: str, source_url: str) -> str:
    """将HTML转换为Markdown"""
    soup = BeautifulSoup(html, "html.parser")

    # 尝试找到主内容区域
    main_content = (
        soup.find("main")
        or soup.find("article")
        or soup.find(class_=re.compile(r"content|main|article", re.I))
        or soup.find(id=re.compile(r"content|main|article", re.I))
        or soup.body
    )

    if not main_content:
        main_content = soup

    # 清理内容
    clean_content(main_content)

    # 处理图片，确保使用完整URL
    for img in main_content.find_all("img"):
        src = img.get("src") or img.get("data-src") or ""
        if src:
            if src.startswith("//"):
                src = "https:" + src
            elif src.startswith("/"):
                src = urljoin(BASE_URL, src)
            img["src"] = src

    # 转换为Markdown
    content = md(str(main_content), heading_style="ATX", bullets="-")

    # 清理多余空行
    content = re.sub(r"\n{3,}", "\n\n", content)

    return content.strip()


def extract_title(html: str) -> str:
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
        for suffix in ["-阿里云", "_阿里云", "- 阿里云", "_ 阿里云"]:
            if title.endswith(suffix):
                title = title[: -len(suffix)]
        return title
    return "未知标题"


def save_solution(
    content: str, title: str, source_url: str, index: int
) -> dict:
    """保存解决方案为Markdown文件"""
    filename = f"solution-{index:03d}.md"
    filepath = RAW_DIR / filename
    collected_at = datetime.now().strftime("%Y-%m-%d")

    # 构建文件内容
    file_content = f"""---
title: {title}
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
    }


def crawl_solutions():
    """主爬取流程"""
    print("=" * 60)
    print("阿里云解决方案爬虫")
    print("=" * 60)

    setup_dirs()

    # 1. 从API获取解决方案列表
    print(f"\n[1] 从API获取解决方案列表")
    solutions = fetch_solution_list_from_api()
    print(f"    找到 {len(solutions)} 个解决方案")

    if not solutions:
        print("    无法获取解决方案列表")
        return

    # 保存解决方案列表到文件
    list_file = OUTPUT_DIR / "solution_list.json"
    list_file.write_text(json.dumps(solutions, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"    列表已保存到: {list_file}")

    # 2. 爬取每个解决方案
    print(f"\n[2] 开始爬取解决方案 (共 {len(solutions)} 个)")
    metadata_list = []

    for i, sol in enumerate(solutions, 1):
        url = sol["url"]
        title = sol["title"]

        print(f"\n    [{i}/{len(solutions)}] {title}")
        print(f"    URL: {url}")

        time.sleep(REQUEST_DELAY)

        html = fetch_page(url)
        if not html:
            continue

        page_title = extract_title(html)
        content = html_to_markdown(html, url)

        if len(content) < 100:
            print(f"    警告: 内容过短 ({len(content)} 字符), 跳过")
            continue

        meta = save_solution(content, page_title or title, url, i)
        metadata_list.append(meta)
        print(f"    保存: {meta['filename']} ({len(content)} 字符)")

    # 3. 保存元数据
    metadata_path = OUTPUT_DIR / "metadata.json"
    metadata = {
        "total": len(metadata_list),
        "collected_at": datetime.now().isoformat(),
        "source": MENU_API_URL,
        "solutions": metadata_list,
    }
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n" + "=" * 60)
    print(f"完成! 共保存 {len(metadata_list)} 个解决方案")
    print(f"输出目录: {OUTPUT_DIR.absolute()}")
    print("=" * 60)


if __name__ == "__main__":
    crawl_solutions()
