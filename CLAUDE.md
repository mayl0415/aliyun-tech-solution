# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

阿里云技术解决方案爬虫 - 从阿里云开发者中心爬取技术解决方案，将 HTML 转换为 Markdown，并按类别组织内容。集成了 LangChain/Ollama 用于 RAG 和 Agent 开发。

## 常用命令

```bash
# 安装依赖（使用 uv 包管理器）
uv sync

# 运行主爬虫
python aliyun/crawler.py

# 后处理流程（按顺序执行）
python aliyun/process_images.py    # 下载架构图
python aliyun/rename_files.py      # 用标题重命名文件
python aliyun/organize_files.py    # 按类别层级组织

# 使用阿里云 SDK（需要配置凭证）
export ALIBABA_CLOUD_ACCESS_KEY_ID="your_key"
export ALIBABA_CLOUD_ACCESS_KEY_SECRET="your_secret"
```

## 架构说明

**爬取流程：**
1. `crawler.py` - 从阿里云 API (`getMenuTree`) 获取解决方案列表，抓取详情页，转换为带 YAML frontmatter 的 Markdown
2. `process_images.py` - 从爬取内容中提取并下载架构图
3. `rename_files.py` - 用标题前缀重命名 Markdown 文件（如 `001-title.md`）
4. `organize_files.py` - 根据 API 元数据将文件按类别层级分类

**数据流向：**
- API 来源：`https://developer.aliyun.com/adc/api/skillBuilder/getMenuTree`
- 原始输出：`arch-solutions/raw/`
- 整理后输出：`arch-solutions/organized/{一级类别}/{二级类别}/`
- 元数据：`arch-solutions/metadata.json`（记录所有已爬取的解决方案）

**关键模式：**
- 各脚本模块化，可独立运行
- 请求间隔 2.5 秒限速
- HTML 清洗：转换前移除导航、页头、页脚、脚本、广告
- URL 规范化：在 Markdown 输出中将相对 URL 转为绝对 URL

## 技术栈

- Python 3.12，使用 `uv` 管理
- 网页爬取：requests、beautifulsoup4、markdownify
- 阿里云 SDK：aliyun-python-sdk-core、aliyun-python-sdk-ecs
- AI/LLM：langchain、langchain-ollama


## Browser Automation

Use `agent-browser` for web automation. Run `agent-browser --help` for all commands.

Core workflow:
1. `agent-browser open <url>` - Navigate to page
2. `agent-browser snapshot -i` - Get interactive elements with refs (@e1, @e2)
3. `agent-browser click @e1` / `fill @e2 "text"` - Interact using refs
4. Re-snapshot after page changes