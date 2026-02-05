---
title: "快速搭建Dify-LLM应用开发平台"
source_url: https://www.huaweicloud.com/solution/implementations/building-a-dify-llm-application-development-platform.html
collected_at: 2026-02-05
---

- [解决方案实践](https://www.huaweicloud.com/solution/implementations/index.html)
- 快速搭建Dify-LLM应用开发平台

# 快速搭建Dify-LLM应用开发平台

# 快速搭建Dify-LLM应用开发平台

[查看部署指南](https://support.huaweicloud.com/dify-aislt/dify_01.html)
[方案咨询](https://www.huaweicloud.com/consultation/?type=building-a-dify-llm-application-development-platform)

### 方案架构

该解决方案基于云容器引擎 CCE帮助您快速部署高可用Dify LLM应用开发平台。

![](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/Dify-cce.jpg)

**快速搭建Dify-LLM应用开发平台**

版本：3.0.0﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿

上次更新日期：2026年2月

来源：由华为云构建

部署：预计20分钟

卸载：预计10分钟

**[预估成本 ◥](https://support.huaweicloud.com/dify-aislt/dify_02.html)**

单机：2~5元（ 按需计费：Flexus云服务器X实例0.95元/小时，弹性公网IP EIP 0.80元/GB，体验本方案预计成本不超过5元）

增强：6-12元（按需计费：Flexus云服务器X实例3.3元/小时，云搜索服务CSS1.3元/小时，弹性公网IP EIP 0.80元/GB，体验本方案预计成本不超过12元）

高可用：35~70元（按需计费：X实例、EIP、OBS、CCE、Redis、RDS、CSS、ELB、NAT等资源累积约35元/小时，体验本方案预计成本不超过70元）

**[查看源代码 ◥](https://gitee.com/HuaweiCloudDeveloper/huaweicloud-solution-building-a-dify-llm-application-development-platform/tree/master-dev/)**

支持区域：

华北-北京四
西南-贵阳一
华南-广州
华东-上海一
亚太-香港
华北-乌兰察布一
亚太-雅加达

[查看部署指南](https://support.huaweicloud.com/dify-aislt/dify_01.html)
[一键部署（社区版单机部署）](https://console.huaweicloud.com/unibuy-flexus/?region=cn-north-4#/buy/flexusMix/iqa-new)
[一键部署（知识库搜索增强版）](https://console.huaweicloud.com/rf/?region=cn-north-4&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/building-a-dify-llm-application-development-platform/building-a-dify-llm-application-development-platform-css.tf.json&stackName=building-a-dify-llm-application-development-platform-css&stackDescription=快速搭建Dify-LLM应用开发平台（知识库搜索增强版）)
[一键部署（CCE容器高可用版）](https://console.huaweicloud.com/unibuy-flexus/?region=cn-north-4#/buy/flexusMix/iqa-high)

[查看部署指南](https://support.huaweicloud.com/dify-aislt/dify_01.html)
[一键部署（社区版单机部署）](https://console.huaweicloud.com/unibuy-flexus/?region=cn-southwest-2#/buy/flexusMix/iqa-new)
[一键部署（知识库搜索增强版）](https://console.huaweicloud.com/rf/?region=cn-southwest-2&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-9.obs.cn-southwest-2.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/building-a-dify-llm-application-development-platform/building-a-dify-llm-application-development-platform-css.tf.json&stackName=building-a-dify-llm-application-development-platform-css&stackDescription=快速搭建Dify-LLM应用开发平台（知识库搜索增强版）)
[一键部署（CCE容器高可用版）](https://console.huaweicloud.com/unibuy-flexus/?region=cn-southwest-2#/buy/flexusMix/iqa-high)

[查看部署指南](https://support.huaweicloud.com/dify-aislt/dify_01.html)
[一键部署（社区版单机部署）](https://console.huaweicloud.com/unibuy-flexus/?region=cn-south-1#/buy/flexusMix/iqa-new)
[一键部署（知识库搜索增强版）](https://console.huaweicloud.com/rf/?region=cn-south-1&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-2.obs.cn-south-1.myhuaweicloud.com/solution-as-code-moudle/building-a-dify-llm-application-development-platform/building-a-dify-llm-application-development-platform-css.tf.json&stackName=building-a-dify-llm-application-development-platform-css&stackDescription=%E5%BF%AB%E9%80%9F%E6%90%AD%E5%BB%BADify-LLM%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E5%B9%B3%E5%8F%B0%EF%BC%88%E7%9F%A5%E8%AF%86%E5%BA%93%E6%90%9C%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%89%88%EF%BC%89)

[查看部署指南](https://support.huaweicloud.com/dify-aislt/dify_01.html)
[一键部署（社区版单机部署）](https://console.huaweicloud.com/unibuy-flexus/?region=cn-east-3#/buy/flexusMix/iqa-new)
[一键部署（知识库搜索增强版）](https://console.huaweicloud.com/rf/?region=cn-east-3&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-3.obs.cn-east-3.myhuaweicloud.com/solution-as-code-moudle/building-a-dify-llm-application-development-platform/building-a-dify-llm-application-development-platform-css.tf.json&stackName=building-a-dify-llm-application-development-platform-css&stackDescription=快速搭建Dify-LLM应用开发平台（知识库搜索增强版）)
[一键部署（CCE容器高可用版）](https://console.huaweicloud.com/unibuy-flexus/?region=cn-east-3#/buy/flexusMix/iqa-high)

[查看部署指南](https://support.huaweicloud.com/dify-aislt/dify_01.html)
[一键部署（社区版单机部署）](https://console.huaweicloud.com/unibuy-flexus/?region=ap-southeast-1#/buy/flexusMix/iqa-new)

[查看部署指南](https://support.huaweicloud.com/dify-aislt/dify_01.html)
[一键部署（知识库搜索增强版）](https://console.huaweicloud.com/rf/?locale=zh-cn&region=cn-north-9#/console/stack/stackCreate?templateUrl=https://documentation-samples-17.obs.cn-north-9.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-module/building-a-dify-llm-application-development-platform/building-a-dify-llm-application-development-platform-css.tf.json&stackName=building-a-dify-llm-application-development-platform-css&stackDescription=%E5%BF%AB%E9%80%9F%E6%90%AD%E5%BB%BADify-LLM%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E5%B9%B3%E5%8F%B0%EF%BC%88%E7%9F%A5%E8%AF%86%E5%BA%93%E6%90%9C%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%89%88%EF%BC%89)

[查看部署指南](https://support.huaweicloud.com/dify-aislt/dify_01.html)
[一键部署（CCE容器高可用版）](https://console.huaweicloud.com/rf/?region=ap-southeast-4&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-18.obs.ap-southeast-4.myhuaweicloud.com/solution-as-code-module/building-a-dify-llm-application-development-platform/building-a-dify-llm-application-development-platform-k8s.tf&stackName=building-a-dify-llm-application-development-platform&stackDescription=快速搭建Dify-LLM应用开发平台（CCE容器高可用版）)

**架构描述**

**社区版单机部署：**

1. 创建一台华为云[Flexus云服务器X实例](https://www.huaweicloud.com/product/flexus-x.html)（FlexusX），用于搭建Dify-LLM应用开发平台

2. 创建一个[弹性公网IP EIP](https://www.huaweicloud.com/product/eip.html)并关联FlexusX实例，提供访问公网和被公网访问能力

3. 创建一个安全组，通过配置安全组规则，为云服务器提供安全防护

**知识库搜索增强版：**

1. 创建一台FlexusX实例，用于搭建Dify-LLM应用开发平台

2. 创建一台FlexusX实例，用于部署Embedding（bge-m3）及Reranker（bge-reranker-v2-m3）模型

3. 创建两个弹性公网IP EIP并分别关联两个FlexusX实例，提供访问公网和被公网访问能力

4. 创建一个[云搜索服务 CSS](https://www.huaweicloud.com/product/es.html) OpenSearch集群，提供在线分布式搜索及语义搜索等功能

5. 创建一个安全组，通过配置安全组规则，为云服务器提供安全防护

**CCE容器高可用版：**

1. 创建三个弹性公网IP EIP，提供访问公网和被公网访问能力

2. 创建一个[弹性负载均衡 ELB](https://www.huaweicloud.com/product/elb.html)，并绑定EIP，将访问流量自动分发到不同后端服务，扩展应用系统对外的服务能力，实现强大的应用容错性能

3. 创建一个[NAT网关 NAT](https://www.huaweicloud.com/product/nat.html)，并绑定EIP，配置SNAT规则，提供安全可靠的公网NAT网关和私网NAT网关服务，保护私有网络信息不对外暴露

4. 创建三台FlexusX实例，用于安装部署Dify5个核心插件

5. 创建一个[云容器引擎 CCE](https://www.huaweicloud.com/product/cce.html) Turbo集群，创建节点池并将三台FlexusX实例纳管为集群的Node节点

6. 创建一台FlexusX实例，用于部署Embedding（bge-m3）及Reranker（bge-reranker-v2-m3）模型

7. 使用[对象存储服务 OBS](https://www.huaweicloud.com/product/obs.html)，用于将Dify的知识库挂载在对象存储服务 OBS桶上

8. 创建一个[分布式缓存服务Redis®\*版](https://www.huaweicloud.com/product/dcs.html)，兼容Redis，为用户提供高性能、低成本NoSQL数据库，同时数据流转过程中数据的一致性

9. 创建一个[云数据库 RDS for PostgreSQL](https://www.huaweicloud.com/product/pg.html)实例，主备分区部署，具备跨可用区故障容灾的能力

10. 创建一个云搜索服务 CSS OpenSearch集群，提供在线分布式搜索及语义搜索等功能

11. 创建四个安全组，通过配置安全组规则，为云服务器提供安全防护

**架构描述**

**云服务器单机部署：**

1. 创建一台华为云[Flexus云服务器X实例](https://www.huaweicloud.com/product/flexus-x.html)（FlexusX），用于搭建Dify-LLM应用开发平台

2. 创建一个[弹性公网IP EIP](https://www.huaweicloud.com/product/eip.html)并关联华为云Flexus云X实例，提供访问公网和被公网访问能力

3. 创建一个安全组，通过配置安全组规则，为云服务器提供安全防护

**知识库搜索增强版：**

1. 创建一台FlexusX实例，用于搭建Dify-LLM应用开发平台

2. 创建一台FlexusX实例，用于部署Embedding（bge-m3）及Reranker（bge-reranker-v2-m3）模型

3. 创建两个弹性公网IP EIP并分别关联两个FlexusX实例，提供访问公网和被公网访问能力

4. 创建一个[云搜索服务 CSS](https://www.huaweicloud.com/product/es.html) OpenSearch集群，提供在线分布式搜索及语义搜索等功能

5. 创建一个安全组，通过配置安全组规则，为云服务器提供安全防护

**CCE容器高可用版：**

1. 创建三个弹性公网IP EIP，提供访问公网和被公网访问能力

2. 创建一个[弹性负载均衡 ELB](https://www.huaweicloud.com/product/elb.html)，并绑定EIP，将访问流量自动分发到不同后端服务，扩展应用系统对外的服务能力，实现强大的应用容错性能

3. 创建一个[NAT网关 NAT](https://www.huaweicloud.com/product/nat.html)，并绑定EIP，配置SNAT规则，提供安全可靠的公网NAT网关和私网NAT网关服务，保护私有网络信息不对外暴露

4. 创建三台FlexusX实例，用于安装部署Dify5个核心插件

5. 创建一个[云容器引擎 CCE](https://www.huaweicloud.com/product/cce.html) Turbo集群，创建节点池并将三台FlexusX实例纳管为集群的Node节点

6. 创建一台FlexusX实例，用于部署Embedding（bge-m3）及Reranker（bge-reranker-v2-m3）模型

7. 使用[对象存储服务 OBS](https://www.huaweicloud.com/product/obs.html)，用于将Dify的知识库挂载在对象存储服务 OBS桶上

8. 创建一个[分布式缓存服务Redis®\*版](https://www.huaweicloud.com/product/dcs.html)，兼容Redis，为用户提供高性能、低成本NoSQL数据库，同时数据流转过程中数据的一致性

9. 创建一个[云数据库 RDS for PostgreSQL](https://www.huaweicloud.com/product/pg.html)实例，主备分区部署，具备跨可用区故障容灾的能力

10. 创建一个云搜索服务 CSS OpenSearch集群，提供在线分布式搜索及语义搜索等功能

11. 创建四个安全组，通过配置安全组规则，为云服务器提供安全防护

展开内容

收起内容

### 方案优势

### 成本优化

提供高性价比的云服务器，按需选择资源规格、支持自动扩展，减少资源闲置，优化成本投入，进一步降低客户的运营成本。
### 高可用性

通过云容器引擎 CCE、云数据库 RDS for PostgreSQL、云搜索服务 CSS OpenSearch部署应用，更好地托管与简化维护应用实例，确保系统的高性能和可扩展性。
### 一键部署

一键轻松部署，即可完成云服务资源的创建及Dify-LLM应用开发平台的搭建。
