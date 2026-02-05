# 华为云产品架构爬虫

爬取华为云产品详情页，主要获取产品架构图和描述，转换为 Markdown 格式并按分类组织。

## 目标

1. 获取华为云所有产品的架构图和产品说明
2. 按产品分类组织文件结构
3. 保留图片链接，清理重复图片

## 数据源

### 产品列表 API

```
GET https://portal.huaweicloud.com/rest/cbc/portaldocdataservice/v1/books/items?appId=CHINA-ZH_CN
```

**返回结构：**
```json
{
  "data": [
    {
      "code": "compute",
      "name": "计算",
      "cnName": "计算",
      "enName": "Compute",
      "products": [
        {
          "code": "ecs",
          "title": "弹性云服务器 ECS",
          "uri": "https://support.huaweicloud.com/ecs/index.html",
          "description": "可随时自动获取、弹性伸缩的云服务器"
        }
      ]
    }
  ]
}
```

**关键字段说明：**
- `data[].name` - 产品分类名称（一级目录）
- `data[].code` - 分类代码
- `data[].products[].code` - 产品代码（用于构建文档中心 URL）
- `data[].products[].title` - 产品完整名称
- `data[].products[].uri` - 产品详情页地址（备用）
- `data[].products[].description` - 产品简介

## 爬取流程

```
┌─────────────────────────────────────────────────────────────────┐
│                     1. 获取产品列表                              │
│         调用 API 获取所有分类和产品信息                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    2. 遍历每个产品                               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              3. 尝试访问文档中心（优先）                          │
│    URL: https://support.huaweicloud.com/progressive_knowledge/  │
│         {product_code}.html                                     │
│    示例: https://support.huaweicloud.com/progressive_knowledge/ │
│         ecs.html                                                │
└─────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              │                               │
        访问成功 (200)                   访问失败 (404)
              │                               │
              ▼                               ▼
┌─────────────────────────┐     ┌─────────────────────────┐
│ 4a. 查找"了解"模块       │     │ 4b. 访问产品详情页       │
│ 点击"什么是xxx"链接      │     │ (product.uri)           │
└─────────────────────────┘     └─────────────────────────┘
              │                               │
              └───────────────┬───────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    5. 抓取页面内容                               │
│    - 提取产品描述                                                │
│    - 提取架构图及说明                                            │
│    - 保留图片链接                                                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    6. 保存为 Markdown                            │
│    输出路径: products/{分类名}/{产品代码}.md                      │
└─────────────────────────────────────────────────────────────────┘
```

### 步骤详解

#### 3. 文档中心页面

**URL 格式:** `https://support.huaweicloud.com/progressive_knowledge/{code}.html`

如果页面存在，需要在页面中查找"了解"模块：

```html
<div class="step-item step-item-three">
  <div class="step-title">
    <div class="step-subtitle">了解</div>
  </div>
  <div class="step-content">
    <a class="por-link step-text c-linkblock"
       href="https://support.huaweicloud.com/productdesc-ecs/zh-cn_topic_0013771112.html">
      什么是弹性云服务器
    </a>
  </div>
</div>
```

查找逻辑：
1. 找到 `class="step-subtitle"` 且文本为"了解"的元素
2. 在其父级的 `.step-content` 中找到包含"什么是"的链接
3. 访问该链接获取产品详情页

#### 4. 页面内容提取

从产品详情页提取：
- 页面标题
- 产品概述/简介
- **架构图**（重点）
- 架构说明文字

## 输出结构

```
huaweicloud-product/
├── task.md                   # 任务说明（本文件）
├── crawler.py                # 爬虫脚本
├── clean_duplicate_images.py # 重复图片清理脚本
├── crawl_metadata.json       # 爬取元数据（记录已爬取的产品）
└── products/                 # 爬取结果
    ├── 计算/
    │   ├── ecs.md
    │   ├── bms.md
    │   └── ...
    ├── 存储/
    │   ├── obs.md
    │   └── ...
    ├── 网络/
    │   └── ...
    └── ...
```

## Markdown 输出格式

```markdown
---
title: "弹性云服务器 ECS"
code: "ecs"
category: "计算"
source_url: "https://support.huaweicloud.com/productdesc-ecs/xxx.html"
crawled_at: "2025-02-05T12:00:00"
---

# 弹性云服务器 ECS

## 产品简介

可随时自动获取、弹性伸缩的云服务器...

## 架构图

![ECS 架构图](https://support.huaweicloud.com/xxx/xxx.png)

## 架构说明

弹性云服务器由以下组件构成...
```

## 命令行使用

```bash
# 爬取所有产品
python3 crawler.py

# 限制爬取数量
python3 crawler.py --limit 50

# 跳过已爬取的产品（断点续爬）
python3 crawler.py --skip-crawled

# 只爬取指定分类
python3 crawler.py --category "计算"

# 爬取指定产品
python3 crawler.py --code ecs

# 后台运行全量爬取
nohup python3 crawler.py --skip-crawled > crawl_full.log 2>&1 &

# 检查爬取进度
./check_progress.sh

# 清理重复图片（待实现）
# python3 clean_duplicate_images.py --clean --threshold 5
```

## 技术要点

1. **使用 requests + BeautifulSoup 进行页面爬取**
   - 直接 HTTP 请求获取页面内容
   - BeautifulSoup 解析 HTML 结构
   - markdownify 转换为 Markdown 格式

2. **请求限速**
   - 请求间隔 2.5 秒，避免对服务器造成压力

3. **断点续爬**
   - 使用 `crawl_metadata.json` 记录已爬取的产品
   - 支持中断后继续爬取（--skip-crawled）

4. **图片处理**
   - 保留原始图片 URL（不下载到本地）
   - 过滤小图标、logo 等无关图片
   - 后期可清理重复的模板图片

5. **错误处理**
   - 文档中心不存在时，回退到产品详情页
   - 记录爬取失败的产品，方便后续重试
   - 日志同时输出到控制台和文件

## 注意事项

1. 文件名使用产品 `code` 而非中文标题，避免特殊字符问题
2. 分类目录使用中文名称 `name`
3. 部分产品可能没有架构图，只保存产品描述
4. API 返回的 `uri` 是备用入口，优先使用文档中心
