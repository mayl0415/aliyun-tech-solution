# 阿里云页面爬取方法

## 产品页面爬取

### 流程

```
1. extract_products.py    → 从 product.js 提取产品 URL 列表 → aliyun_products.json
2. extract_categories.py  → 从 product.js 提取产品分类结构 → product_categories.json
3. build_product_db.py    → 获取页面 meta 信息 → products_database.json
```

### 数据来源

产品数据来自 `https://www.aliyun.com/product/list` 页面的 JS 文件 `product.js`。

需要手动下载 product.js：打开页面 → F12 → Network → 找到包含产品数据的 JS 文件

### 分类结构

product.js 中的分类树结构：
- `type: "model-category"` 表示分类节点
- `title` 是分类名称
- `children` 包含子分类或产品数据

产品数据使用混淆的键名：
- `cnjaya55gweyu3l7mcza`: 产品名称
- `d9j9vkzi8t7eutgpcpe0`: 产品代码
- `xihv7dyfgoycfxw76wus`: 产品链接

### 输出

最终输出 `products_database.json`，每个产品包含：
```json
{
  "url": "https://www.aliyun.com/product/ecs",
  "title": "云服务器ECS - 高性能弹性计算服务",
  "short_title": "云服务器 ECS",
  "description": "产品描述...",
  "keywords": "关键词1,关键词2",
  "image": "产品图标URL",
  "category_l1": "计算",
  "category_l2": ""
}
```

### 注意事项

阿里云产品页面是 SPA（JavaScript 渲染），使用 requests 无法获取渲染后的页面内容。

**推荐方案**：只获取 meta 标签信息（`build_product_db.py`），因为 meta 标签已包含完整的产品信息。

如需完整页面内容（包括功能介绍、架构图等），需使用 Playwright/Selenium 渲染页面。

---

## 解决方案爬取

## 整体流程

```
1. crawler.py        → 爬取页面内容，转为 Markdown
2. process_images.py → 处理图片（过滤/下载）
3. rename_files.py   → 重命名文件（加上标题）
4. organize_files.py → 按分类目录组织文件
```

## 核心技术栈

| 功能 | 库 |
|------|-----|
| HTTP 请求 | `requests` |
| HTML 解析 | `BeautifulSoup` |
| HTML→Markdown | `markdownify` |

## 关键方法

### 1. 获取链接列表（两种方式）

**方式 A：从 API 获取**（推荐）

```python
# 阿里云有菜单树 API，直接返回 JSON
MENU_API_URL = "https://developer.aliyun.com/adc/api/skillBuilder/getMenuTree"
response = requests.get(MENU_API_URL, headers=HEADERS)
data = response.json()
# 递归遍历 data["data"] 提取所有链接
```

**方式 B：从页面解析**

```python
soup = BeautifulSoup(html, "html.parser")
for a in soup.find_all("a", href=True):
    # 匹配目标链接模式
    if "/solution/tech-solution/" in href:
        solutions.append({"url": full_url, "title": title})
```

### 2. 请求配置

```python
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
    "Accept": "text/html,application/xhtml+xml,...",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}
REQUEST_DELAY = 2.5  # 秒，避免被封
```

### 3. 内容提取与清理

```python
# 定位主内容区
main_content = (
    soup.find("main")
    or soup.find("article")
    or soup.find(class_=re.compile(r"content|main|article", re.I))
    or soup.body
)

# 移除无关元素
for selector in ["header", "footer", "nav", "script", "style",
                 ".breadcrumb", ".sidebar", ".ad", ...]:
    for elem in soup.select(selector):
        elem.decompose()
```

### 4. HTML 转 Markdown

```python
from markdownify import markdownify as md

# 处理图片 URL（相对路径→绝对路径）
for img in soup.find_all("img"):
    src = img.get("src") or img.get("data-src")
    if src.startswith("//"):
        src = "https:" + src
    elif src.startswith("/"):
        src = urljoin(BASE_URL, src)
    img["src"] = src

# 转换
content = md(str(main_content), heading_style="ATX", bullets="-")
content = re.sub(r"\n{3,}", "\n\n", content)  # 清理多余空行
```

### 5. 保存格式（YAML frontmatter + 正文）

```python
file_content = f"""---
title: {title}
source_url: {source_url}
collected_at: {datetime.now().strftime("%Y-%m-%d")}
---

{content}
"""
filepath.write_text(file_content, encoding="utf-8")
```

## 输出目录结构

```
arch-solutions/
├── raw/                    # 原始 Markdown 文件
│   ├── 001-标题.md
│   └── ...
├── images/                 # 下载的架构图
├── organized/              # 按分类组织后的文件
│   ├── 分类1/
│   │   ├── 子分类1/
│   │   └── ...
│   └── ...
├── metadata.json           # 元数据（标题、URL、文件名映射）
└── solution_list.json      # 解决方案列表
```

## 复用要点

爬取其他页面时需要调整：

1. **链接获取逻辑** - 根据目标网站结构修改 `fetch_solution_list_from_api()` 或 `extract_solution_links()`
2. **内容定位选择器** - 修改 `main_content` 查找逻辑，适配目标网站 DOM 结构
3. **清理规则** - 根据目标网站调整要移除的 CSS 选择器
4. **URL 过滤规则** - 修改链接匹配模式
