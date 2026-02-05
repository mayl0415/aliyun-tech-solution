---
title: "快速部署Embedding及Reranker模型"
source_url: https://www.huaweicloud.com/solution/implementations/deploying-embedding-and-reranker-models.html
collected_at: 2026-02-05
---

- [解决方案实践](https://www.huaweicloud.com/solution/implementations/index.html)
- 快速部署Embedding及Reranker模型

# 快速部署Embedding及Reranker模型

# 快速部署Embedding及Reranker模型

[查看部署指南](https://support.huaweicloud.com/derm-aislt/derm_01.html)
[方案咨询](https://www.huaweicloud.com/consultation/?type=deploying-embedding-and-reranker-models)

### 方案架构

该解决方案帮助您在华为云Flexus云服务器X实例（弹性云服务器 ECS）上快速部署Embedding（bge-m3）及Reranker（bge-reranker-v2-m3）模型。

![](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/SAC/2022_new/deploying-embedding-and-reranker-models.jpg)

**快速部署Embedding及Reranker模型**

版本：1.0.0﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿

上次更新日期：2025年3月

来源：由华为云构建

部署：预计10分钟

卸载：预计5分钟

**[预估成本 ◥](https://support.huaweicloud.com/derm-aislt/derm_02.html)**

3~6元（按需计费：Flexus云服务器X实例2.28元/小时，弹性公网IP EIP0.80元/GB，体验本方案预计成本不超过6元）

7~14元（按需计费：弹性云服务器ECS 6.64元/小时，弹性公网IP EIP0.80元/GB，体验本方案预计成本不超过14元）

**[查看源代码 ◥](https://gitee.com/HuaweiCloudDeveloper/huaweicloud-solution-deploying-embedding-and-reranker-models/tree/master-dev/)**

支持区域：

西南-贵阳一
华北-北京四
华东-上海一
华东二
华南-广州
华北-乌兰察布一

[查看部署指南](https://support.huaweicloud.com/derm-aislt/derm_01.html)
[一键部署（CPU版）](https://console.huaweicloud.com/rf/?region=cn-southwest-2&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-9.obs.cn-southwest-2.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/deploying-embedding-and-reranker-models/deploying-embedding-and-reranker-models.tf.json&stackName=deploying-embedding-and-reranker-models&stackDescription=快速部署Embedding及Reranker模型（CPU）)
[一键部署（GPU版）](https://console.huaweicloud.com/rf/?region=cn-southwest-2&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-9.obs.cn-southwest-2.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/deploying-embedding-and-reranker-models/deploying-embedding-and-reranker-models-gpu.tf.json&stackName=deploying-embedding-and-reranker-models-gpu&stackDescription=快速部署Embedding及Reranker模型（GPU）)

[查看部署指南](https://support.huaweicloud.com/derm-aislt/derm_01.html)
[一键部署（CPU版）](https://console.huaweicloud.com/rf/?region=cn-north-4&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/deploying-embedding-and-reranker-models/deploying-embedding-and-reranker-models.tf.json&stackName=deploying-embedding-and-reranker-models&stackDescription=快速部署Embedding及Reranker模型)
[一键部署（GPU版）](https://console.huaweicloud.com/rf/?region=cn-north-4&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/deploying-embedding-and-reranker-models/deploying-embedding-and-reranker-models-gpu.tf.json&stackName=deploying-embedding-and-reranker-models-gpu&stackDescription=快速部署Embedding及Reranker模型（GPU）)

[查看部署指南](https://support.huaweicloud.com/derm-aislt/derm_01.html)
[一键部署](https://console.huaweicloud.com/rf/?region=cn-east-3&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-3.obs.cn-east-3.myhuaweicloud.com/solution-as-code-moudle/deploying-embedding-and-reranker-models/deploying-embedding-and-reranker-models.tf.json&stackName=deploying-embedding-and-reranker-models&stackDescription=快速部署Embedding及Reranker模型)

[查看部署指南](https://support.huaweicloud.com/derm-aislt/derm_01.html)
[一键部署](https://console.huaweicloud.com/rf/?region=cn-east-4&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-16.obs.cn-east-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-module/deploying-embedding-and-reranker-models/deploying-embedding-and-reranker-models.tf.json&stackName=deploying-embedding-and-reranker-models&stackDescription=快速部署Embedding及Reranker模型)

[查看部署指南](https://support.huaweicloud.com/derm-aislt/derm_01.html)
[一键部署](https://console.huaweicloud.com/rf/?region=cn-south-1&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-2.obs.cn-south-1.myhuaweicloud.com/solution-as-code-moudle/deploying-embedding-and-reranker-models/deploying-embedding-and-reranker-models.tf.json&stackName=deploying-embedding-and-reranker-models&stackDescription=快速部署Embedding及Reranker模型)

[查看部署指南](https://support.huaweicloud.com/derm-aislt/derm_01.html)
[一键部署](https://console.huaweicloud.com/rf/?region=cn-north-9&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-17.obs.cn-north-9.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-module/deploying-embedding-and-reranker-models/deploying-embedding-and-reranker-models.tf.json&stackName=deploying-embedding-and-reranker-models&stackDescription=快速部署Embedding及Reranker模型)

**架构描述**

**架构描述**

- 创建一个[弹性公网IP EIP](https://www.huaweicloud.com/product/eip.html)，用于提供访问公网和被公网访问能力
- 创建一台[Flexus云服务器X实例](https://www.huaweicloud.com/product/flexus-x.html)（[弹性云服务器 ECS](https://www.huaweicloud.com/product/ecs.html)，含GPU服务器），用于部署Embedding（bge-m3）及Reranker（bge-reranker-v2-m3）模型
- 创建一个安全组，通过配置安全组规则，为云服务器提供安全防护

展开内容

收起内容

### 方案优势

### 高效性

内置 bge-m3及bge-reranker-v2-m3模型实现高效的文本相似度计算、分类等任务，重排序模型，推理速度快。
### 低成本

提供高性价比的云服务器，用户可以根据实际需求自定义不同规格的云服务器。
### 一键部署

一键轻松部署，即可快速完成云服务器和公网IP等资源的下发以及Embedding bge-m3及Reranker模型的部署。
