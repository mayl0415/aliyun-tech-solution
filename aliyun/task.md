
# 任务：爬取阿里云解决方案并保存为Markdown

## 目标

从阿里云官网爬取解决方案页面，保存为Markdown格式，图片使用原始URL链接。

## 起始点

https://www.aliyun.com/solution

从这个页面开始，找到所有解决方案链接，然后爬取。

## 输出要求

### 目录结构
```
arch-solutions/
├── raw/
│   ├── solution-001.md
│   ├── solution-002.md
│   └── ...
└── metadata.json
```

### Markdown文件格式

每个文件包含：
- YAML元数据（标题、URL、抓取时间）
- 正文内容
- 图片用链接，不下载

示例：
```yaml
---
title: 数字化大屏解决方案
source_url: https://www.aliyun.com/solution/xxx
collected_at: 2025-02-03
---

[正文内容...]
```

## 技术要求

- HTML转Markdown
- 图片保留URL链接
- 清理导航、页脚等无关内容
- 每个请求间隔2-3秒

## 就这些

开始吧！