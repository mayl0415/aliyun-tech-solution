# 华为云解决方案爬虫任务

## 目标
爬取华为云解决方案架构页面，提取技术方案内容并保存为 Markdown 文件。

## 数据源
三个目录页面：
- https://www.huaweicloud.com/solution/technical-directory.html (技术方案目录)
- https://www.huaweicloud.com/solution/industry-directory.html (行业解决方案目录)
- https://www.huaweicloud.com/solution/reference-architecture.html (参考架构)

## 爬取流程

### 1. 收集链接
- 访问三个目录页面
- 提取所有 `https://www.huaweicloud.com/solution/**.html` 链接
- 去重处理
- 排除目录页面本身

### 2. 爬取内容
- 遍历所有解决方案链接
- 提取页面主要内容
- 保留架构图等图片链接（转为绝对 URL）
- 转换为带 YAML frontmatter 的 Markdown

### 3. 去重清理
- 检测并删除内容重复的文件
- 使用内容哈希进行比对

## 输出结构
```
huaweicould-solutions/
├── solutions/              # Markdown 文件目录
│   └── *.md               # 解决方案文档
├── metadata.json          # 爬取元数据
├── solution_links.json    # 链接列表
└── crawler.py             # 爬虫脚本
```

## 运行命令
```bash
# 爬取解决方案
python huaweicould-solutions/crawler.py

# 可选：指定限制数量
python huaweicould-solutions/crawler.py --limit 50
```
