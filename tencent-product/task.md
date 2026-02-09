# 腾讯云产品页面爬虫任务

## 目标

爬取腾讯云产品详情页面，提取产品信息并保存为 Markdown 文件，按分类组织文件结构。

## 数据来源

- **产品目录 API**: `https://qcloudimg.tencent-cloud.cn/scripts/qccomponents/v2/full-nav-tree.json`
- **产品页面基础 URL**: `https://cloud.tencent.com/product/{slug}`

### 数据结构

```json
{
  "id": "RfNxg4tk6m",
  "type": "entry",           // "entry" 表示产品, "dir" 表示目录
  "dictId": "2000",
  "dictType": "product",     // 过滤条件: dictType == "product"
  "title": "云服务器",        // 产品全名
  "slug": "cvm",             // URL 标识符
  "link": "https://cloud.tencent.com/product/cvm",
  "desc": "安全稳定，高弹性的计算服务",
  "description": "稳定、安全、弹性、高性能的云端计算服务...",
  "tag": "hot",              // 可选: hot/new 等标签
  "children": []
}
```

### 分类层级

数据为三层递归树结构:
1. 一级分类 (如: 计算、存储、网络)
2. 二级分类 (如: 云服务器、高性能计算)
3. 产品条目 (type="entry", dictType="product")

## 爬取规则

1. **URL 过滤**: 只爬取 `link` 以 `https://cloud.tencent.com/product/` 开头的页面
2. **去重**: 根据 `link` 字段去重，避免重复爬取
3. **限速**: 请求间隔 2.5 秒
4. **跳过已爬取**: 支持断点续爬

## 输出结构

```
tencent-product/
├── products/
│   ├── {一级分类}/
│   │   ├── {产品名}.md
│   │   └── ...
│   └── crawl_metadata.json
├── task.md
└── tencent_product_crawler.py
```

### Markdown 格式

```markdown
---
title: "产品全名"
slug: "cvm"
url: https://cloud.tencent.com/product/cvm
category_l1: "计算"
category_l2: "云服务器"
desc: "短描述"
crawled_at: 2026-02-05T12:00:00
---

# 产品名

## 产品简介
...

## 产品图片
![图片](url)

## 产品功能
...
```

## 命令行参数

```bash
# 爬取产品 (跳过已爬取，限制数量)
python tencent-product/tencent_product_crawler.py --skip-crawled --limit 100

# 只爬取指定分类
python tencent-product/tencent_product_crawler.py --category "计算"

# 爬取单个URL测试
python tencent-product/tencent_product_crawler.py --url https://cloud.tencent.com/product/cvm
```

## 后处理

爬取完成后，运行去重脚本清理重复图片:
```bash
python tencent-product/clean_duplicate_images.py --clean --threshold 5
```
