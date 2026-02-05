---
title: "快速搭建EvalScope模型性能评测平台"
source_url: https://www.huaweicloud.com/solution/implementations/deploying-evalscope-for-model-performance-evaluation.html
collected_at: 2026-02-05
---

- [解决方案实践](https://www.huaweicloud.com/solution/implementations/index.html)
- 快速搭建EvalScope模型性能评测平台

# 快速搭建EvalScope模型性能评测平台

# 快速搭建EvalScope模型性能评测平台

[查看部署指南](https://support.huaweicloud.com/evalscope-aislt/evalscope_01.html)
[方案咨询](https://www.huaweicloud.com/consultation/?type=deploying-evalscope-for-model-performance-evaluation)

### 方案架构

该解决方案帮助您在华为云Flexus云服务器X实例（弹性云服务器 ECS）上快速搭建EvalScope模型性能评测平台。

![](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/SAC/2025/25-05/Deploying EvalScope for Model Performance Evaluation.png)

**快速搭建EvalScope模型性能评测平台**

版本：1.1.0﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿

上次更新日期：2025年4月

来源：由华为云构建

部署：预计10分钟

卸载：预计5分钟

**[预估成本 ◥](https://support.huaweicloud.com/evalscope-aislt/evalscope_02.html)**

**[查看源代码 ◥](https://gitee.com/HuaweiCloudDeveloper/huaweicloud-solution-deploying-evalscope-for-model-performance-evaluation/tree/master-dev/)**

支持区域：

华北-北京四
西南-贵阳一

[查看部署指南](https://support.huaweicloud.com/evalscope-aislt/evalscope_01.html)
[一键部署](https://console.huaweicloud.com/rf/?region=cn-north-4&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/deploying-evalscope-for-model-performance-evaluation/deploying-evalscope-for-model-performance-evaluation.tf.json&stackName=deploying-evalscope-for-model-performance-evaluation&stackDescription=快速搭建EvalScope模型性能评测平台)

[查看部署指南](https://support.huaweicloud.com/evalscope-aislt/evalscope_01.html)
[一键部署](https://console.huaweicloud.com/rf/?region=cn-southwest-2&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-9.obs.cn-southwest-2.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/deploying-evalscope-for-model-performance-evaluation/deploying-evalscope-for-model-performance-evaluation.tf.json&stackName=deploying-evalscope-for-model-performance-evaluation&stackDescription=快速搭建EvalScope模型性能评测平台)

**架构描述**

**架构描述**

- 创建一个[弹性公网IP EIP](https://www.huaweicloud.com/product/eip.html)，用于提供访问公网和被公网访问能力
- 创建一台[Flexus云服务器X实例](https://www.huaweicloud.com/product/flexus-x.html)（[弹性云服务器 ECS](https://www.huaweicloud.com/product/ecs.html)），用于搭建EvalScope模型性能评测平台
- 创建一个安全组，通过配置安全组规则，为云服务器提供安全防护

展开内容

收起内容

### 方案优势

### 功能完备

EvalScope代码完全使用Python语言编写，具有轻量化的特点，提供了丰富的定制选项，用户可以根据自己的需求灵活配置评测任务，满足多样化的模型评估需求。
### 低成本

提供高性价比的云服务器，用户可以根据实际需求自定义不同规格的云服务器。
### 一键部署

一键轻松部署，即可快速完成云服务器和公网IP等资源的下发以及EvalScope模型性能评测平台的搭建。
