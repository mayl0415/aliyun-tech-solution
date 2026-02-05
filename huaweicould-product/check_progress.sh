#!/bin/bash
# 检查爬取进度

cd "$(dirname "$0")"

echo "=== 华为云产品爬取进度 ==="
echo

# 检查进程是否在运行
if pgrep -f "python3 crawler.py" > /dev/null; then
    echo "状态: 运行中"
else
    echo "状态: 已停止"
fi
echo

# 读取元数据
if [ -f products/crawl_metadata.json ]; then
    echo "统计:"
    python3 -c "
import json
with open('products/crawl_metadata.json') as f:
    d = json.load(f)
print(f'  已爬取: {len(d.get(\"crawled_products\", []))} 个')
print(f'  成功: {d.get(\"stats\", {}).get(\"success\", 0)}')
print(f'  失败: {d.get(\"stats\", {}).get(\"failed\", 0)}')
print(f'  最后更新: {d.get(\"last_crawl\", \"N/A\")}')
"
fi
echo

# 统计文件数
echo "文件统计:"
for dir in products/*/; do
    if [ -d "$dir" ]; then
        count=$(find "$dir" -name "*.md" | wc -l)
        name=$(basename "$dir")
        echo "  $name: $count 个"
    fi
done
echo

# 显示最近日志
echo "最近日志:"
tail -5 crawl.log 2>/dev/null || tail -5 crawl_full.log 2>/dev/null
