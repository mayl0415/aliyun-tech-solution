#!/usr/bin/env python3
"""重命名文件，使用数字+标题格式"""

import json
import re
from pathlib import Path

OUTPUT_DIR = Path("arch-solutions")
RAW_DIR = OUTPUT_DIR / "raw"
IMG_DIR = OUTPUT_DIR / "images"


def sanitize_filename(title: str) -> str:
    """将标题转换为安全的文件名"""
    # 移除或替换不安全的字符
    name = title.strip()
    # 替换特殊字符
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    # 将空格和连续空白替换为下划线
    name = re.sub(r'\s+', '_', name)
    # 限制长度
    if len(name) > 60:
        name = name[:60]
    return name


def rename_files():
    """重命名所有文件"""
    metadata_path = OUTPUT_DIR / "metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))

    print(f"开始重命名 {len(metadata['solutions'])} 个解决方案\n")

    for sol in metadata["solutions"]:
        idx = sol["id"]
        title = sol["title"]
        old_filename = sol["filename"]  # solution-001.md

        # 生成新文件名
        safe_title = sanitize_filename(title)
        new_basename = f"{idx:03d}-{safe_title}"
        new_filename = f"{new_basename}.md"

        # 重命名 md 文件
        old_md = RAW_DIR / old_filename
        new_md = RAW_DIR / new_filename
        if old_md.exists():
            old_md.rename(new_md)
            print(f"  {old_filename} -> {new_filename}")

        # 重命名对应的图片文件
        old_img_base = old_filename.replace(".md", "")  # solution-001
        for img_file in IMG_DIR.glob(f"{old_img_base}*"):
            # 获取后缀（可能是 .png, -2.png 等）
            suffix = img_file.name[len(old_img_base):]  # .png 或 -2.png
            new_img_name = f"{new_basename}{suffix}"
            new_img = IMG_DIR / new_img_name
            img_file.rename(new_img)
            print(f"    {img_file.name} -> {new_img_name}")

        # 更新 metadata
        sol["filename"] = new_filename

    # 保存更新后的 metadata
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n完成！metadata.json 已更新")


if __name__ == "__main__":
    rename_files()
