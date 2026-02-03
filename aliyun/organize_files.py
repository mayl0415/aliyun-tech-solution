#!/usr/bin/env python3
"""按API目录结构组织文件"""

import json
import re
import shutil
from pathlib import Path

import requests

OUTPUT_DIR = Path("arch-solutions")
RAW_DIR = OUTPUT_DIR / "raw"
IMG_DIR = OUTPUT_DIR / "images"

MENU_API_URL = "https://developer.aliyun.com/adc/api/skillBuilder/getMenuTree?aliyun_lang=zh"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}


def sanitize_dirname(name: str) -> str:
    """将名称转换为安全的目录名"""
    name = name.strip()
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    name = re.sub(r'\s+', '_', name)
    return name


def get_menu_structure():
    """从API获取目录结构，构建 URL -> (一级目录, 二级目录) 的映射"""
    print("获取API目录结构...")
    response = requests.get(MENU_API_URL, headers=HEADERS, timeout=30)
    response.raise_for_status()
    data = response.json()

    url_to_category = {}

    def find_solutions(node, l1, l2):
        """递归查找所有 SOLUTION_DETAIL 节点"""
        if node.get("type") == "SOLUTION_DETAIL" and node.get("url"):
            url_to_category[node["url"]] = (l1, l2)
        for child in node.get("children", []) or []:
            find_solutions(child, l1, l2)

    # 遍历所有顶级分类
    if "data" in data:
        for level1 in data["data"]:
            level1_title = level1.get("title", "未分类")

            # 遍历二级子节点
            for child1 in level1.get("children", []) or []:
                level2_title = child1.get("title", "未分类")
                find_solutions(child1, level1_title, level2_title)

    print(f"  找到 {len(url_to_category)} 个解决方案的分类信息")
    return url_to_category


def organize_files():
    """组织文件到分类目录"""
    # 获取目录结构
    url_to_category = get_menu_structure()

    # 读取 metadata
    metadata_path = OUTPUT_DIR / "metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))

    # 创建新的目录结构
    new_base = OUTPUT_DIR / "organized"
    if new_base.exists():
        shutil.rmtree(new_base)

    print(f"\n开始组织文件...")

    organized_solutions = []

    for sol in metadata["solutions"]:
        url = sol["source_url"]
        old_filename = sol["filename"]
        old_basename = old_filename.replace(".md", "")

        # 获取分类
        if url in url_to_category:
            level1, level2 = url_to_category[url]
        else:
            level1, level2 = "其他", "未分类"

        # 创建目录
        safe_l1 = sanitize_dirname(level1)
        safe_l2 = sanitize_dirname(level2)
        target_dir = new_base / safe_l1 / safe_l2
        target_dir.mkdir(parents=True, exist_ok=True)

        # 移动 md 文件
        old_md = RAW_DIR / old_filename
        new_md = target_dir / old_filename
        if old_md.exists():
            shutil.copy2(old_md, new_md)

        # 移动对应的图片
        for img_file in IMG_DIR.glob(f"{old_basename}*"):
            new_img = target_dir / img_file.name
            shutil.copy2(img_file, new_img)

        # 更新 metadata
        sol["category_l1"] = level1
        sol["category_l2"] = level2
        sol["path"] = str(target_dir.relative_to(new_base) / old_filename)
        organized_solutions.append(sol)

        print(f"  {old_filename} -> {safe_l1}/{safe_l2}/")

    # 保存更新后的 metadata
    new_metadata = {
        "total": len(organized_solutions),
        "source": MENU_API_URL,
        "solutions": organized_solutions,
    }
    (new_base / "metadata.json").write_text(
        json.dumps(new_metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # 统计分类
    print(f"\n目录结构:")
    for l1_dir in sorted(new_base.iterdir()):
        if l1_dir.is_dir():
            print(f"  {l1_dir.name}/")
            for l2_dir in sorted(l1_dir.iterdir()):
                if l2_dir.is_dir():
                    count = len(list(l2_dir.glob("*.md")))
                    print(f"    {l2_dir.name}/ ({count} 个)")

    print(f"\n完成！文件已组织到: {new_base}")


if __name__ == "__main__":
    organize_files()
