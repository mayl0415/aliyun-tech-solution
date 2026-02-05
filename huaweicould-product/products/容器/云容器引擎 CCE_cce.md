---
title: "什么是云容器引擎"
code: "cce"
category: "容器"
source_url: "https://support.huaweicloud.com/productdesc-cce/cce_productdesc_0001.html?utm_source=cce_Growth_map&utm_medium=display&utm_campaign=help_center&utm_content=Growth_map"
crawled_at: "2026-02-05T16:29:22.898614"
---

# 什么是云容器引擎

## 产品简介

提供高可靠的企业级容器应用管理服务

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-cce/zh-cn_image_0000002106561213.png)

## 详细说明

# 什么是云容器引擎

云容器引擎（Cloud Container Engine，简称CCE）是一个企业级的[Kubernetes](https://kubernetes.io/)集群托管服务，支持容器化应用的全生命周期管理，为您提供高度可扩展的、高性能的云原生应用部署和管理方案。

#### 为什么选择云容器引擎

云容器引擎深度整合高性能的计算（ECS/BMS）、网络（VPC/EIP/ELB）、存储（EVS/OBS/SFS）等服务，并支持GPU、NPU、ARM等异构计算架构，支持多可用区（Available Zone，简称AZ）、多区域（Region）容灾等技术构建高可用[Kubernetes](https://kubernetes.io/)集群。

华为云是全球首批Kubernetes认证服务提供商（Kubernetes Certified Service Provider，KCSP），是国内最早投入Kubernetes社区的厂商，是容器开源社区主要贡献者和容器生态领导者。华为云也是CNCF云原生计算基金会的创始成员及白金会员，云容器引擎是全球首批通过CNCF基金会Kubernetes一致性认证的容器服务。

更多选择理由，请参见[产品优势](https://support.huaweicloud.com/productdesc-cce/cce_productdesc_0003.html)和[应用场景](https://support.huaweicloud.com/productdesc-cce/cce_productdesc_0004.html)。

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-cce/zh-cn_image_0000002342460104.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/support/cce-video/CCE_Intro_CN_20210223.mp4)、

#### 产品形态

云容器引擎包含多种产品形态。

|  |  |  |  |
| --- | --- | --- | --- |
| 集群类型 | CCE Standard | CCE Turbo | CCE Autopilot |
| 产品定位 | 标准版本集群，提供高可靠、安全的商业级容器集群服务。 | 面向云原生2.0的新一代容器集群产品，计算、网络、调度全面加速。 | 无用户节点的Serverless版集群，无需对节点的部署、管理和安全性进行维护，并根据CPU和内存资源用量按需付费。 |
| 使用场景 | 面向有云原生数字化转型诉求的用户，期望通过容器集群管理应用，获得灵活弹性的算力资源，简化对计算、网络、存储的资源管理复杂度。 | 适合对极致性能、资源利用率提升和全场景覆盖有更高诉求的客户。 | 适合具有明显的波峰波谷特征的业务负载，例如在线教育、电子商务等行业。 |
| 网络模型 | 面向性能和规模要求不高的场景，提供以下网络模型：   * 容器隧道网络模型 * VPC网络模型   详情请参见[容器网络模型对比](https://support.huaweicloud.com/usermanual-cce/cce_10_0281.html)。 | 云原生网络2.0模型：面向大规模和高性能的场景。  组网规模最大支持2000节点 | 云原生网络2.0模型：面向大规模和高性能的场景。 |
| Pod使用主机端口（hostPort） | 支持 | 不支持 | 不支持 |
| 网络性能 | VPC网络叠加容器网络，性能有一定损耗 | VPC网络和容器网络融合，性能无损耗 | VPC网络和容器网络融合，性能无损耗 |
| 容器网络隔离 | * 容器隧道网络模式：集群内部网络隔离策略，支持NetworkPolicy。 * VPC网络模式：开启DataPlane V2后支持NetworkPolicy，详情请参见[DataPlane V2网络加速说明](https://support.huaweicloud.com/usermanual-cce/cce_10_0945.html)。 | Pod可直接关联安全组，基于安全组的隔离策略，支持集群内外部统一的安全隔离。 | Pod可直接关联安全组，基于安全组的隔离策略，支持集群内外部统一的安全隔离。 |
| 容器资源隔离 | 普通容器：Cgroups隔离 | * 安全容器：当前仅物理机支持，提供虚机级别的隔离 * 普通容器：Cgroups隔离 | 提供虚机级别的隔离 |
| 边缘基础设施管理 | 不支持 | 支持管理边缘云资源，详情请参见[在CCE Turbo分布式集群中使用边缘云资源](https://support.huaweicloud.com/usermanual-cce/cce_10_0840.html) | 不支持 |

#### 产品架构

**图1** CCE产品架构
  
![](https://support.huaweicloud.com/productdesc-cce/zh-cn_image_0000002106561213.png "点击放大")

* 计算：全面适配华为云各类计算实例，支持虚拟机和裸机混合部署、高性价比鲲鹏实例、GPU和华为云独有的昇腾算力；支持GPU虚拟化、共享调度、资源感知的调度优化。
* 网络：支持对接高性能、安全可靠、多协议的独享型ELB作为业务流量入口。
* 存储：对接云存储，支持EVS、SFS和OBS，提供磁盘加密、快照和备份能力。
* 集群服务：支持购买集群、连接集群、升级集群、管理集群等一系列集群生命周期管理服务。
* 容器编排：CCE提供了管理Helm Chart（模板）的控制台，能够帮助您方便地使用模板部署应用，并在控制台上管理应用。
* 制品仓库：对接容器镜像服务，支持镜像全生命周期管理的服务，提供简单易用、安全可靠的镜像管理功能，帮助您快速部署容器化服务。
* 弹性伸缩：支持工作负载和节点的弹性伸缩，可以根据业务需求和策略，经济地自动调整弹性计算资源的管理服务。
* 服务治理：深度集成应用服务网格，提供开箱即用的应用服务网格流量治理能力，用户无需修改代码，即可实现灰度发布、流量治理和流量监控能力。
* 容器运维：深度集成容器智能分析，可实时监控应用及资源，支持采集、管理、分析日志，采集各项指标及事件并提供一键开启的告警能力。
* 扩展插件市场：提供了多种类型的插件，用于管理集群的扩展功能，以支持选择性扩展满足特性需求的功能。

#### 云容器引擎学习路径

您可以借助云容器引擎[成长地图](https://support.huaweicloud.com/cce/index.html)，快速了解产品，由浅入深学习使用和运维CCE。

####
