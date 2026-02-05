## 🛠️ task_product.md

### Context

本项目需要从一个巨大的 `product.js` 文件中提取阿里云产品信息。该文件是一个混淆后的 JavaScript 文件，其中包含一个巨大的 `modelDatas` 对象。

### Objective

编写并运行一个 Python 脚本，从 `product.js` 中提取所有阿里云产品的 **详情页链接** 以及与之对应的 **产品介绍描述**，并将结果去重保存。

### Data Patterns (Ref: image_1a3c2a.jpg)

1. **产品链接模式**：匹配 `https://www.aliyun.com/product/[a-zA-Z0-9_-]+`。
2. **描述文本模式**：通常出现在链接附近的键值对中（如图片中显示的 `nunbjpiy4no7fmiplev` 对应链接，其前后可能存在中文字符串作为描述）。
3. **数据结构**：数据被包裹在深度嵌套的 JSON 结构中，但我们需要的是扁平化的“链接-描述”映射。

### Requirements

1. **内存安全**：禁止直接 `f.read()` 整个文件。必须使用**分块读取 (Chunking)** 或 **内存映射 (mmap)**。
2. **提取逻辑**：
* 搜索所有符合 `https://www.aliyun.com/product/*` 的 URL。
* 对于每一个匹配到的 URL，向上或向下查找最近的一个包含中文的字符串作为其“产品介绍”。
* 如果 URL 包含 `/tech-solution`，这类通常是技术方案，也需保留。


3. **去重处理**：以 URL 为唯一键进行去重，保留最长（最详尽）的描述文本。
4. **输出格式**：保存为 `aliyun_products.json`，格式如下：
```json
[
  {"url": "...", "description": "..."},
  ...
]

```



### Execution Steps

1. **Check Environment**: 确保处于虚拟环境中。
2. **Analysis**: 先读取文件的前 5000 行，分析 `product.js` 的具体字符边界和引号规则（是单引号还是双引号）。
3. **Scripting**: 编写 `extract_products.py`。建议使用 `re.finditer` 配合缓冲区，确保跨块的匹配不会丢失。
4. **Validation**: 打印提取到的前 5 条数据供确认。
5. **Full Run**: 执行全量提取。
