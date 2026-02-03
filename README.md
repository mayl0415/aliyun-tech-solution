# Aliyun Tech Solution Crawler & Agent

这是一个用于自动爬取阿里云官网技术解决方案（Tech Solutions）并将其转化为 Markdown 格式的工具库，同时也包含与阿里云 SDK 集成的示例代码。

## 🚀 功能特性

- **自动爬虫**：从阿里云开发者中心 API 获取最新的技术解决方案列表。
- **HTML 转 Markdown**：自动抓取解决方案详情页，清理无关导航和样式，转换为干净的 Markdown 文档。
- **元数据管理**：自动生成 `metadata.json` 和 `solution_list.json` 以便后续处理。
- **内容保存**：抓取的内容存储在 `arch-solutions/raw` 目录下。
- **阿里云 SDK 集成**：包含使用阿里云 Python SDK 进行资源查询（如 ECS 实例类型）的示例。
- **语义化集成**：预装了 LangChain 和 Ollama 等 AI 工具，方便后续进行 RAG（检索增强生成）或 Agent 开发。

## 📂 项目结构

```text
.
├── aliyun/
│   └── crawler.py         # 解决方案爬虫主脚本
├── arch-solutions/        # 爬取的输出目录
│   ├── raw/               # 转换后的 Markdown 文件
│   ├── metadata.json      # 抓取的任务元数据
│   └── solution_list.json # 原始解决方案列表
├── aliyun.py              # 阿里云 SDK 调用示例
├── main.py                # 项目入口入口
├── pyproject.toml         # 项目配置与依赖管理
└── README.md
```

## 🛠️ 快速开始

### 1. 安装依赖
本项目使用 `uv` 进行包管理（推荐），也可以使用 `pip`:

```bash
# 使用 uv
uv sync

# 使用 pip
pip install -r requirements.txt
```

### 2. 爬取阿里云解决方案
运行爬虫脚本，它会自动抓取所有技术解决方案并保存到 `arch-solutions` 目录：

```bash
python aliyun/crawler.py
```

### 3. 使用阿里云 SDK
在使用 `aliyun.py` 前，请确保已设置环境变量：

```bash
export ALIBABA_CLOUD_ACCESS_KEY_ID="您的AccessKeyID"
export ALIBABA_CLOUD_ACCESS_KEY_SECRET="您的AccessKeySecret"

python aliyun.py
```

## 🔐 安全说明
项目代码中**严禁硬编码**任何阿里云 AccessKey 和 Secret。所有密钥应通过环境变量或安全的配置文件读取。`.gitignore` 已经配置了常见的敏感文件过滤。

## 📜 开源协议
MIT License
