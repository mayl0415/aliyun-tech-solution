#!/bin/bash
# 检查爬取进度

echo "=== 阿里云产品爬取进度 ==="
echo ""

# 统计已爬取的文件数
MD_COUNT=$(find products -name "*.md" 2>/dev/null | wc -l)
TOTAL=259

echo "已爬取: ${MD_COUNT} / ${TOTAL} ($(( MD_COUNT * 100 / TOTAL ))%)"
echo ""

# 检查爬虫进程
if pgrep -f product_crawler > /dev/null; then
    echo "爬虫状态: 运行中 ✓"
else
    echo "爬虫状态: 已停止"
fi
echo ""

# 按分类统计
echo "分类统计:"
for dir in products/*/; do
    if [ -d "$dir" ]; then
        count=$(find "$dir" -name "*.md" | wc -l)
        name=$(basename "$dir")
        printf "  %-20s: %d\n" "$name" "$count"
    fi
done | sort -t: -k2 -rn

echo ""
echo "最新爬取的5个产品:"
ls -lt products/*/*.md 2>/dev/null | head -5 | awk '{print "  " $NF}'
