# 阿里云产品爬虫

爬取阿里云产品详情页，将内容转换为Markdown格式，按分类组织。

## 目录结构

```
aliyun-product/
├── README.md                 # 本文件
├── product_crawler.py        # 产品爬虫脚本
├── check_progress.sh         # 进度检查脚本
├── crawl.log                 # 爬取日志
└── products/                 # 爬取结果
    ├── crawl_metadata.json   # 爬取元数据
    ├── 人工智能平台/
    ├── 计算/
    ├── 容器/
    ├── 存储/
    ├── 网络与CDN/
    ├── 安全/
    ├── 数据库/
    └── ...                   # 更多分类
```

## 使用方法

### 运行爬虫

```bash
# 爬取所有产品
python3 product_crawler.py

# 限制爬取数量
python3 product_crawler.py --limit 50

# 跳过已爬取的产品（断点续爬）
python3 product_crawler.py --skip-crawled

# 只爬取指定分类
python3 product_crawler.py --category "计算"

# 后台运行
nohup python3 product_crawler.py --skip-crawled > crawl.log 2>&1 &
```

### 检查进度

```bash
./check_progress.sh
```

## 数据来源

- 产品列表: https://www.aliyun.com/product/list
- 产品详情: https://www.aliyun.com/product/*
- 基础数据: aliyun/products_database.json (259个产品)

## Markdown 格式

每个产品保存为一个Markdown文件，包含：

```markdown
---
title: "产品完整标题"
short_title: "产品简称"
url: 产品URL
category_l1: "一级分类"
category_l2: "二级分类"
keywords: "关键词"
crawled_at: 爬取时间
---

# 产品简称

## 产品简介
产品描述...

## 产品图标
![产品图标](图标URL)

## 产品详情
- 特性1...
- 特性2...
```

## 注意事项

1. 使用 agent-browser 进行页面爬取
2. 请求间隔 2.5 秒限速，避免对服务器造成压力
3. 支持断点续爬，通过 crawl_metadata.json 记录已爬取的URL
4. 产品分类来自 products_database.json 中的 category_l1 字段

## 相关文件

- `../aliyun/products_database.json` - 产品基础数据
- `../aliyun/crawler.py` - 阿里云技术解决方案爬虫
