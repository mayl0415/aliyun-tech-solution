# 云厂商产品与解决方案知识库

从阿里云、腾讯云、华为云三大云厂商爬取的产品介绍与技术解决方案，共 **1519 篇** Markdown 文档，按云厂商和类别组织。

## 数据总览

| 云厂商 | 产品 | 解决方案 | 合计 |
|--------|------|----------|------|
| 阿里云 | 259 | 179 | 438 |
| 腾讯云 | 352 | 178 | 530 |
| 华为云 | 239 | 312 | 551 |
| **合计** | **850** | **669** | **1519** |

## 目录结构

```
aliyun-product/products_v2/{类别}/         # 阿里云产品 (259篇, 60个类别)
arch-solutions/organized/{类别}/{子类别}/   # 阿里云解决方案 (179篇, 7个类别)
tencent-product/products/{类别}/           # 腾讯云产品 (352篇, 20个类别)
tencent-product/solutions/{L1类别}/        # 腾讯云解决方案 (178篇, 3个类别)
huaweicould-product/products/{类别}/       # 华为云产品 (239篇, 27个类别)
huaweicould-solutions/solutions/           # 华为云解决方案 (312篇)
```

## 内容覆盖

**产品类别**涵盖：计算、存储、数据库、网络、安全、AI/机器学习、大数据、容器、中间件、开发运维、物联网、视频服务、CDN 等。

**解决方案**覆盖行业：AI、金融、制造、汽车、零售、教育、医疗、政府、互联网、智慧园区等。

## Markdown 格式

每篇文档包含 YAML frontmatter 元数据和正文内容：

```markdown
---
title: "产品/方案名称"
url: https://cloud.xxx.com/product/xxx
category: "分类"
crawled_at: 2026-02-09T12:00:00
---

# 标题

产品介绍、功能特性、架构图等...
```

## 用途

- RAG（检索增强生成）知识库
- 云产品对比分析
- 行业解决方案调研
- 云厂商产品图谱构建

## 技术栈

- Python 3.12 + uv
- 网页爬取：requests、beautifulsoup4、markdownify、trafilatura
- 浏览器自动化：agent-browser（处理需要 JS 渲染的页面）
- AI/LLM：langchain、langchain-ollama

## 快速开始

```bash
uv sync  # 安装依赖
```

爬虫脚本位于各模块目录下，详见 [CLAUDE.md](CLAUDE.md) 中的工具与爬虫章节。

## License

MIT
