#!/usr/bin/env python3
"""
扫描 products_v2 目录下的 Markdown 文件，找出重复的图片并清理
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import json

PRODUCTS_DIR = Path(__file__).parent / 'products_v2'
REPORT_FILE = Path(__file__).parent / 'duplicate_images_report.json'

def scan_images():
    """扫描所有 md 文件中的图片"""
    # 图片URL -> 出现的文件列表
    image_files = defaultdict(list)
    # 文件 -> 图片列表
    file_images = {}

    for md_file in PRODUCTS_DIR.rglob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 提取所有图片 URL: ![...](url)
        images = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', content)
        file_images[str(md_file)] = images

        for img_url in images:
            image_files[img_url].append(str(md_file))

    return image_files, file_images

def analyze_duplicates(image_files, file_images):
    """分析重复图片"""
    # 在多个文件中出现的图片（跨文件重复）
    cross_file_duplicates = {
        url: files for url, files in image_files.items()
        if len(files) > 1
    }

    # 同一文件内重复的图片
    in_file_duplicates = {}
    for filepath, images in file_images.items():
        seen = {}
        for img in images:
            if img in seen:
                if filepath not in in_file_duplicates:
                    in_file_duplicates[filepath] = []
                in_file_duplicates[filepath].append(img)
            seen[img] = True

    return cross_file_duplicates, in_file_duplicates

def clean_in_file_duplicates(in_file_duplicates, dry_run=True):
    """清理文件内的重复图片（保留第一个，删除后续重复的）"""
    cleaned_files = []

    for filepath, dup_images in in_file_duplicates.items():
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        for img_url in set(dup_images):
            # 找到所有这个图片的位置
            pattern = rf'!\[[^\]]*\]\({re.escape(img_url)}\)\n*'
            matches = list(re.finditer(pattern, content))

            if len(matches) > 1:
                # 保留第一个，删除其他的
                for match in reversed(matches[1:]):
                    content = content[:match.start()] + content[match.end():]

        if content != original_content:
            cleaned_files.append({
                'file': filepath,
                'duplicates_removed': list(set(dup_images))
            })

            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

    return cleaned_files


def remove_common_template_images(cross_file_duplicates, threshold=10, dry_run=True):
    """
    删除出现在多个文件中的通用模板图片
    threshold: 出现次数超过此值的图片被认为是模板图片
    """
    # 要删除的图片 URL 列表
    template_images = [
        url for url, files in cross_file_duplicates.items()
        if len(files) >= threshold
    ]

    # 添加一些明确应该删除的图片模式
    delete_patterns = [
        'clear.png',  # 跟踪像素
        'ynuf.alipay.com',  # 支付宝跟踪
    ]

    cleaned_count = 0
    affected_files = set()

    for md_file in PRODUCTS_DIR.rglob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        removed_in_file = []

        # 删除模板图片
        for img_url in template_images:
            pattern = rf'!\[[^\]]*\]\({re.escape(img_url)}\)\n*'
            if re.search(pattern, content):
                content = re.sub(pattern, '', content)
                removed_in_file.append(img_url)

        # 删除匹配特定模式的图片
        for pattern_str in delete_patterns:
            pattern = rf'!\[[^\]]*\]\([^)]*{re.escape(pattern_str)}[^)]*\)\n*'
            if re.search(pattern, content):
                content = re.sub(pattern, '', content)
                removed_in_file.append(f'pattern:{pattern_str}')

        if content != original_content:
            affected_files.add(str(md_file))
            cleaned_count += len(removed_in_file)

            if not dry_run:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)

    return {
        'template_images_removed': template_images,
        'affected_files_count': len(affected_files),
        'total_removals': cleaned_count
    }

def generate_report(image_files, file_images, cross_file_duplicates, in_file_duplicates):
    """生成报告"""
    report = {
        'summary': {
            'total_files': len(file_images),
            'total_unique_images': len(image_files),
            'cross_file_duplicate_images': len(cross_file_duplicates),
            'files_with_internal_duplicates': len(in_file_duplicates),
        },
        'cross_file_duplicates': {
            url: {
                'count': len(files),
                'files': [str(Path(f).relative_to(PRODUCTS_DIR)) for f in files]
            }
            for url, files in sorted(cross_file_duplicates.items(), key=lambda x: -len(x[1]))[:50]  # Top 50
        },
        'in_file_duplicates': {
            str(Path(filepath).relative_to(PRODUCTS_DIR)): list(set(imgs))
            for filepath, imgs in in_file_duplicates.items()
        }
    }
    return report

def main():
    import argparse
    parser = argparse.ArgumentParser(description='清理重复图片')
    parser.add_argument('--clean', action='store_true', help='执行全部清理')
    parser.add_argument('--clean-internal', action='store_true', help='清理文件内重复图片')
    parser.add_argument('--clean-template', action='store_true', help='清理跨文件的模板图片')
    parser.add_argument('--threshold', type=int, default=10, help='模板图片阈值（出现次数，默认10）')
    args = parser.parse_args()

    print("扫描图片...")
    image_files, file_images = scan_images()

    print("分析重复...")
    cross_file_duplicates, in_file_duplicates = analyze_duplicates(image_files, file_images)

    print("\n=== 统计摘要 ===")
    print(f"总文件数: {len(file_images)}")
    print(f"唯一图片数: {len(image_files)}")
    print(f"跨文件重复图片数: {len(cross_file_duplicates)}")
    print(f"有内部重复的文件数: {len(in_file_duplicates)}")

    # 生成报告
    report = generate_report(image_files, file_images, cross_file_duplicates, in_file_duplicates)

    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"\n详细报告已保存到: {REPORT_FILE}")

    # 显示跨文件重复最多的图片
    if cross_file_duplicates:
        print("\n=== 跨文件重复最多的图片 (Top 10) ===")
        sorted_dups = sorted(cross_file_duplicates.items(), key=lambda x: -len(x[1]))[:10]
        for url, files in sorted_dups:
            print(f"\n图片出现在 {len(files)} 个文件中:")
            print(f"  URL: {url[:80]}...")
            for f in files[:3]:
                print(f"    - {Path(f).relative_to(PRODUCTS_DIR)}")
            if len(files) > 3:
                print(f"    ... 还有 {len(files)-3} 个文件")

    # 显示将被清理的模板图片
    template_count = len([url for url, files in cross_file_duplicates.items() if len(files) >= args.threshold])
    print(f"\n出现 >= {args.threshold} 次的图片（将被视为模板图片）: {template_count} 个")

    # 显示文件内重复
    if in_file_duplicates:
        print(f"\n=== 文件内重复 ({len(in_file_duplicates)} 个文件) ===")
        for filepath, imgs in list(in_file_duplicates.items())[:5]:
            print(f"\n{Path(filepath).relative_to(PRODUCTS_DIR)}:")
            for img in set(imgs):
                count = imgs.count(img) + 1
                print(f"  - 重复 {count} 次: {img[:60]}...")

    # 清理文件内重复
    if args.clean_internal or args.clean:
        print("\n=== 清理文件内重复图片 ===")
        cleaned = clean_in_file_duplicates(in_file_duplicates, dry_run=False)
        print(f"已清理 {len(cleaned)} 个文件")
        for item in cleaned[:10]:
            print(f"  - {Path(item['file']).relative_to(PRODUCTS_DIR)}: 移除 {len(item['duplicates_removed'])} 种重复图片")

    # 清理模板图片
    if args.clean_template or args.clean:
        print(f"\n=== 清理模板图片 (阈值: {args.threshold}) ===")
        result = remove_common_template_images(cross_file_duplicates, threshold=args.threshold, dry_run=False)
        print(f"移除的模板图片类型: {len(result['template_images_removed'])} 种")
        print(f"影响的文件数: {result['affected_files_count']}")
        print(f"总移除次数: {result['total_removals']}")
        print("\n移除的图片:")
        for url in result['template_images_removed'][:10]:
            print(f"  - {url[:70]}...")
        if len(result['template_images_removed']) > 10:
            print(f"  ... 还有 {len(result['template_images_removed'])-10} 种")

if __name__ == '__main__':
    main()
