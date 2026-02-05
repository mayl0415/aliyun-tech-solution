---
title: "快速搭建DeepSeek推理系统"
source_url: https://www.huaweicloud.com/solution/implementations/building-a-deepseek-lnference-system.html
collected_at: 2026-02-05
---

- [解决方案实践](https://www.huaweicloud.com/solution/implementations/index.html)
- 快速搭建DeepSeek推理系统

# 快速搭建DeepSeek推理系统

# 快速搭建DeepSeek推理系统

[查看部署指南](https://support.huaweicloud.com/deepseek-aislt/deepseek_01.html)
[方案咨询](https://www.huaweicloud.com/consultation/?type=building-a-deepseek-inference-system)

### 方案架构

该解决方案帮助您在华为云Flexus云服务器X实例（弹性云服务器 ECS）上快速搭建DeepSeek-R1蒸馏版模型。

![](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/SAC/2025/25-05/Building a DeepSeek Inference System.png)

**快速搭建DeepSeek推理系统**

版本：1.1.0﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿

上次更新日期：2025年5月

来源：由华为云构建

部署：预计10分钟

卸载：预计5分钟

**[预估成本 ◥](https://support.huaweicloud.com/deepseek-aislt/deepseek_02.html)**

2~4元（按需计费：Flexus云服务器X实例0.38元/小时，弹性公网IP EIP 0.80元/GB，体验本方案预计成本不超过4元）

**[查看源﻿﻿﻿﻿代码 ◥](https://gitee.com/HuaweiCloudDeveloper/huaweicloud-solution-building-a-deepseek-inference-system/tree/master-dev/)**

支持区域：

华东-上海一
华北-北京四
华南-广州
华北-乌兰察布一
西南-贵阳一
华东二
拉美-墨西哥城二

[查看部署指南](https://support.huaweicloud.com/deepseek-aislt/deepseek_01.html)
[一键部署（CPU版）](https://console.huaweicloud.com/rf/?region=cn-east-3&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-3.obs.cn-east-3.myhuaweicloud.com/solution-as-code-moudle/building-a-deepseek-inference-system/building-a-deepseek-inference-system.tf.json&stackName=building-a-deepseek-inference-system&stackDescription=快速搭建DeepSeek推理系统)
[一键部署（GPU版）](https://console.huaweicloud.com/rf/?region=cn-east-3&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-3.obs.cn-east-3.myhuaweicloud.com/solution-as-code-moudle/building-a-deepseek-inference-system/building-a-deepseek-inference-system-gpu.tf.json&stackName=building-a-deepseek-inference-system-gpu&stackDescription=快速搭建DeepSeek推理系统)

[查看部署指南](https://support.huaweicloud.com/deepseek-aislt/deepseek_01.html)
[一键部署（CPU版）](https://console.huaweicloud.com/rf/?region=cn-north-4&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/building-a-deepseek-inference-system/building-a-deepseek-inference-system.tf.json&stackName=building-a-deepseek-inference-system&stackDescription=快速搭建DeepSeek推理系统)
[一键部署（GPU版）—— 白名单客户开放](https://console.huaweicloud.com/rf/?region=cn-north-4&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/building-a-deepseek-inference-system/building-a-deepseek-inference-system-gpu.tf.json&stackName=building-a-deepseek-inference-system-gpu&stackDescription=快速搭建DeepSeek推理系统)

[查看部署指南](https://support.huaweicloud.com/deepseek-aislt/deepseek_01.html)
[一键部署（CPU版）](https://console.huaweicloud.com/rf/?region=cn-south-1&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-2.obs.cn-south-1.myhuaweicloud.com/solution-as-code-moudle/building-a-deepseek-inference-system/building-a-deepseek-inference-system.tf.json&stackName=building-a-deepseek-inference-system&stackDescription=快速搭建DeepSeek推理系统)
[一键部署（GPU版）—— 白名单客户开放](https://console.huaweicloud.com/rf/?region=cn-south-1&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-2.obs.cn-south-1.myhuaweicloud.com/solution-as-code-moudle/building-a-deepseek-inference-system/building-a-deepseek-inference-system-gpu.tf.json&stackName=building-a-deepseek-inference-system-gpu&stackDescription=快速搭建DeepSeek推理系统)

[查看部署指南](https://support.huaweicloud.com/deepseek-aislt/deepseek_01.html)
[一键部署（CPU版）](https://console.huaweicloud.com/rf/?region=cn-north-9&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-17.obs.cn-north-9.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-module/building-a-deepseek-inference-system/building-a-deepseek-inference-system.tf.json&stackName=building-a-deepseek-inference-system&stackDescription=快速搭建DeepSeek推理系统)
[一键部署（GPU版）—— 白名单客户开放](https://console.huaweicloud.com/rf/?region=cn-north-9&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-17.obs.cn-north-9.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-module/building-a-deepseek-inference-system/building-a-deepseek-inference-system-gpu.tf.json&stackName=building-a-deepseek-inference-system-gpu&stackDescription=快速搭建DeepSeek推理系统)

[查看部署指南](https://support.huaweicloud.com/deepseek-aislt/deepseek_01.html)
[一键部署（CPU版）](https://console.huaweicloud.com/rf/?region=cn-southwest-2&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-9.obs.cn-southwest-2.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/building-a-deepseek-inference-system/building-a-deepseek-inference-system.tf.json&stackName=building-a-deepseek-inference-system&stackDescription=快速搭建DeepSeek推理系统)

[查看部署指南](https://support.huaweicloud.com/deepseek-aislt/deepseek_01.html)
[一键部署（CPU版）](https://console.huaweicloud.com/rf/?region=cn-east-4&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-16.obs.cn-east-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-module/building-a-deepseek-inference-system/building-a-deepseek-inference-system.tf.json&stackName=building-a-deepseek-inference-system&stackDescription=快速搭建DeepSeek推理系统)

[查看部署指南](https://support.huaweicloud.com/deepseek-aislt/deepseek_01.html)
[一键部署（GPU版）](https://console.huaweicloud.com/rf/?region=la-north-2#/console/stack/stackCreate?templateUrl=https://documentation-samples-13.obs.la-north-2.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-module/building-a-deepseek-inference-system/building-a-deepseek-inference-system-gpu.tf.json&stackName=building-a-deepseek-inference-system-gpu&stackDescription=快速搭建DeepSeek推理系统)

**架构描述**

**架构描述**

- 创建一个[弹性公网IP EIP](https://www.huaweicloud.com/product/eip.html)，用于提供访问公网和被公网访问能力
- 创建一台[Flexus云服务器X实例](https://www.huaweicloud.com/product/flexus-x.html)（[弹性云服务器 ECS](https://www.huaweicloud.com/product/ecs.html)），用于搭建DeepSeek-R1蒸馏版模型
- 创建一个安全组，通过配置安全组规则，为云服务器提供安全防护

展开内容

收起内容

### 方案优势

### 高性能

DeepSeek通过强化学习技术显著提升推理能力，支持多步骤逻辑推理，能够逐步分解复杂问题并解决问题。
### 低成本

提供高性价比的云服务器，用户可以根据实际需求自定义不同规格的云服务器。
### 一键部署

一键轻松部署，即可完成云服务器及公网IP等资源的快速下发和DeepSeek-R1蒸馏版模型的搭建。
