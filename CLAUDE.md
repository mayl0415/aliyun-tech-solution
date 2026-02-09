# CLAUDE.md

## 项目概述

三大云厂商（阿里云、腾讯云、华为云）的产品介绍与技术解决方案知识库。已爬取 **1519 篇** Markdown 文档，按云厂商和类别组织，可用于 RAG、知识问答、行业分析等场景。

## 数据总览

| 云厂商 | 类型 | 数量 | 路径 |
|--------|------|------|------|
| 阿里云 | 产品 | 259 | `aliyun-product/products_v2/{类别}/` |
| 阿里云 | 解决方案 | 179 | `arch-solutions/organized/{类别}/` |
| 腾讯云 | 产品 | 352 | `tencent-product/products/{类别}/` |
| 腾讯云 | 解决方案 | 178 | `tencent-product/solutions/{L1类别}/` |
| 华为云 | 产品 | 239 | `huaweicould-product/products/{类别}/` |
| 华为云 | 解决方案 | 312 | `huaweicould-solutions/solutions/` |
| **合计** | | **1519** | |

---

## 阿里云

### 产品（259 篇，60 个类别）

路径：`aliyun-product/products_v2/{类别}/{产品名}.md`

主要类别：其他(17)、数据库(15)、应用集成(13)、媒体服务(12)、关系型数据库(9)、智能客服(9)、网站性能优化(9)、网络与CDN(8)、应用架构(8)、AI应用(6)、企业云服务(6)、存储(6)、无影(6)、高性能计算(6) 等

### 解决方案（179 篇，7 个类别）

路径：`arch-solutions/organized/{类别}/{子类别}/{方案名}.md`

| 类别 | 数量 |
|------|------|
| AI | 67 |
| 互联网应用开发 | 43 |
| 大数据 | 31 |
| 安全 | 17 |
| 可观测 | 8 |
| 上云与迁云 | 7 |
| 网络 | 6 |

---

## 腾讯云

### 产品（352 篇，20 个类别）

路径：`tencent-product/products/{类别}/{产品名}.md`

| 类别 | 数量 | | 类别 | 数量 |
|------|------|-|------|------|
| 安全 | 32 | | 开发与运维 | 32 |
| 行业应用 | 32 | | 视频服务 | 30 |
| 推荐 | 25 | | 人工智能与机器学习 | 24 |
| 存储 | 24 | | 计算 | 24 |
| 数据库 | 20 | | 容器与中间件 | 19 |
| 大数据 | 18 | | 网络 | 17 |
| 办公协同 | 15 | | 服务与营销 | 15 |
| 云通信与企业服务 | 12 | | 物联网 | 6 |
| CDN与边缘 | 5 | | 微信生态 | 1 |
| 测试 | 1 | | | |

### 解决方案（178 篇，3 个 L1 类别）

路径：`tencent-product/solutions/{L1类别}/{方案名}.md`

| L1 类别 | 数量 |
|---------|------|
| 通用解决方案 | 86 |
| 行业解决方案 | 81 |
| 微信解决方案 | 11 |

---

## 华为云

### 产品（239 篇，27 个类别）

路径：`huaweicould-product/products/{类别}/{产品名}.md`

| 类别 | 数量 | | 类别 | 数量 |
|------|------|-|------|------|
| 开发与运维 | 26 | | 人工智能 | 18 |
| 管理与监管 | 18 | | 企业应用 | 15 |
| 存储 | 15 | | 网络 | 13 |
| 安全与合规 | 12 | | 大数据 | 12 |
| 用户服务 | 12 | | 计算 | 11 |
| 开天aPaaS | 10 | | 数据库 | 10 |
| 其他 | 8 | | 视频 | 7 |
| 应用中间件 | 7 | | 开发者工具 | 7 |
| 容器 | 6 | | 解决方案 | 6 |
| IoT物联网 | 5 | | CDN与智能边缘 | 4 |
| 迁移 | 4 | | 区块链 | 3 |
| 工业软件 | 3 | | 云生态 | 3 |
| 云化转型 | 2 | | 专属云 | 1 |
| 价格 | 1 | | | |

### 解决方案（312 篇）

路径：`huaweicould-solutions/solutions/{序号}-{标题}.md`

文件按编号命名（如 `001-德勤AI场景化咨询.md`），覆盖行业：AI、汽车、金融、制造、政府、教育、医疗、零售、互联网、智慧园区等。

元数据：`huaweicould-solutions/metadata.json`

---

## 工具与爬虫（参考）

### 环境

```bash
uv sync    # Python 3.12, uv 包管理
```

### 爬虫脚本

| 模块 | 主脚本 | 说明 |
|------|--------|------|
| `aliyun/` | `crawler.py` | 解决方案爬虫（API: getMenuTree），含后处理脚本 |
| `aliyun-product/` | `product_crawler_v2.py` | 产品爬虫（agent-browser） |
| `tencent-product/` | `tencent_product_crawler.py` | 产品爬虫（agent-browser） |
| `tencent-product/` | `tencent_solution_crawler.py` | 解决方案爬虫（agent-browser） |
| `huaweicould-product/` | `crawler.py` | 产品爬虫（agent-browser） |
| `huaweicould-solutions/` | `crawler.py` | 解决方案爬虫 |

### 通用工具

| 工具 | 说明 |
|------|------|
| `clean_duplicate_images.py` | 扫描清理 MD 中重复/模板图片（`--threshold N --clean`） |
| `image_reviewer.py` | Web 图片审核工具（端口 8899），逐文件保留有价值的图片 |

### 通用模式

- 所有爬虫支持 `--skip-crawled` 断点续爬
- 请求限速 2.5 秒间隔
- HTML → Markdown 转换时清洗导航/广告/脚本，相对 URL 转绝对 URL
- 需要 JS 渲染的页面使用 agent-browser（`open` → `snapshot -i` → `click/fill`）

### 腾讯云 API

```
https://qcloudimg.tencent-cloud.cn/scripts/qccomponents/v2/full-nav-tree.json
data[0]["tree"] → 产品目录    data[1]["tree"] → 解决方案目录
```
