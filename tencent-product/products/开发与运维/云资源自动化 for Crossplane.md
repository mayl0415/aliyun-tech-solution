---
title: "云资源自动化 for Crossplane"
url: https://cloud.tencent.com/product/iacp
category: "开发与运维"
crawled_at: 2026-02-09T11:10:06.501747
---

# 云资源自动化 for Crossplane

云资源自动化 for Crossplane（Infrastructure Automation for Crossplane）是一款基于当前业界流行的多云管理开源工具 Crossplane 开发的腾讯云产品。作为构建于 Kubernetes 之上的扩展，通过与腾讯云的云资源服务相结合，用户能够以 Kubernetes 方式使用基础设施即代码原则管理云上基础设施，轻松实施跨云平台的 DevOps 和多云部署等场景。

[快速入门](https://cloud.tencent.com/document/product/1763/105828)[产品文档](https://cloud.tencent.com/document/product/1763)

[开源仓库](https://github.com/crossplane-contrib/provider-tencentcloud)

- [产品体验使用 Crossplane 快速创建一个 VPC 资源](https://cloud.tencent.com/document/product/1763/105828)
- [技术实践Crossplane 资源创建实践教程](https://cloud.tencent.com/document/product/1763/105833)

![](https://cloudcache.tencent-cloud.com/qcloud/ui/static/tc_portal_icon/88f9c9b1-4fb0-4c3a-aa7c-d3ed88458a84.png)

### 完全免费（不含云基础资源）

起源于开源技术，您只需要为所创建的云基础资源付费，本产品不会产生云资源的额外使用成本或者影响云资源的价格。

![](https://cloudcache.tencent-cloud.com/qcloud/ui/static/tc_portal_icon/d4fae081-d2a8-408e-8b8d-4fe6457d5a58.png)

### 覆盖较多腾讯云产品

云资源自动化 for Crossplane 已经提供超过 260 个 CRD，覆盖计算、存储、网络、容器服务、负载均衡、中间件、数据库等腾讯云产品。借助 Crossplane，您可以快速管理业务所依赖的腾讯云基础设施。

### 声明式API

Crossplane 使用 Kubernetes 风格的声明式 API，允许开发人员和运维人员使用熟悉的工具和工作流程来管理腾讯云基础设施，可以无缝接入当前业务已有的 DevOps 流程，不会对业务造成迁移负担。

### 云原生生态

Crossplane 作为 CNCF 沙箱项目，它同时遵循了 CNCF 的最佳实践和标准。使用者可以结合 Helm 来部署腾讯云资源；可以结合 OPA 设置准入规则，实施基于策略的腾讯云资源管理；可以与 Prometheus 和 Grafana 集成，以提供对腾讯云资源的实时监控和报警功能。

### 实时状态同步

Crossplane 通过定义 Kubernetes 控制器，监视管理的腾讯云资源状态并提供状态同步。如果有人修改或删除了 Kubernetes 之外的资源，Crossplane 会撤销更改或重新创建已删除的腾讯云资源，以确保资源的一致性和可靠性。

- 多种集成方式
- 多云管理
- App/Infra 一体化部署

云资源自动化 for Crossplane 让应用程序以及依赖基础设施的部署，都可以通过 Kubernetes Yaml 进行描述，通过 Kubectl 进行部署，数据的共享也更加的安全和高效。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/0oNpsBWj38m3rCwfpKHHy.svg)

[### 产品简介

帮助您快速了解云资源自动化 for Crossplane 产品的功能特性及应用场景。](https://cloud.tencent.com/document/product/1763/105824)

[### 新手指引

帮助您快速了解、体验云资源自动化 for Crossplane 产品。](https://cloud.tencent.com/document/product/1763/105828)

[### 工具指南

帮助您快速了解 Crossplane 的架构和使用核心组件。](https://cloud.tencent.com/document/product/1763/105830)

[### 实践教程

提供常用的云资源 Crossplane 示例，帮助您快速上手。](https://cloud.tencent.com/document/product/1763/105833)

[### 购买指南

云资源自动化 for Crossplane 服务免费，仅收取您创建的云资源或服务的费用。](https://cloud.tencent.com/document/product/1763/105827)

### 可以去哪里获取 API 密钥？

您可以点击 [获取密钥](https://console.cloud.tencent.com/cam/capi) 来获取云 API 的使用密钥。

### 怎么快速定位问题？

### 存量的云资源如何纳入 Crossplane 管理？

您只需要执行几个命令和配置，即可完成使用 Crossplane 管理一个腾讯云 VPC 实例的体验。

[快速入门](https://cloud.tencent.com/document/product/1763/105828)
