---
title: "快速搭建New API大模型网关"
source_url: https://www.huaweicloud.com/solution/implementations/building-a-newapi-llm-gateway.html
collected_at: 2026-02-05
---

- [解决方案实践](https://www.huaweicloud.com/solution/implementations/index.html)
- 快速搭建New API大模型网关

# 快速搭建New API大模型网关

# 快速搭建New API大模型网关

[查看部署指南](https://support.huaweicloud.com/newapi-aislt/new-api_01.html)
[方案咨询](https://www.huaweicloud.com/consultation/?type=building-a-newapi-llm-gateway)

### 方案架构

该解决方案基于Flexus云服务器X实例帮助您快速部署New API大模型网关。

![](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/Building a NewAPI LLM Gateway_2.png)

快速搭建New API大模型网关

版本：1.0.0﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿

上次更新日期：2025年9月

来源：由华为云构建

部署：预计10分钟

卸载：预计5分钟

**[预估成本 ◥](https://support.huaweicloud.com/newapi-aislt/new-api_02.html)**

[查看部署指南](https://support.huaweicloud.com/newapi-aislt/new-api_01.html)

[一键部署](https://console.huaweicloud.com/rf/?region=cn-north-4&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/building-a-newapi-llm-gateway/building-a-newapi-llm-gateway.tf.json&stackName=building-a-newapi-llm-gateway&stackDescription=快速搭建New API大模型网关)

**架构描述﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿**

**架构描述**

- 创建一台华为云[Flexus云服务器X实例](https://www.huaweicloud.com/product/flexus-x.html)，用于搭建New API大模型网关
- 创建一个[弹性公网IP EIP](https://www.huaweicloud.com/product/eip.html)并关联华为云Flexus云服务器X实例，提供访问公网和被公网访问能力
- 创建一个安全组，通过配置安全组规则，为云服务器提供安全防护

展开内容

收起内容

### 方案优势

### 开箱即用

后端即服务，帮助开发者快速搭建生产级的AI大模型网关，部署完成即可使用。
### 低成本

提供高性价比的云服务器，用户可以根据实际需求自定义不同规格的云服务器。
### 一键部署

一键轻松部署，即可完成云服务器的创建和New API大模型网关的搭建。
