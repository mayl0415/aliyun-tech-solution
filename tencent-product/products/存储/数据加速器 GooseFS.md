---
title: "数据加速器 GooseFS"
url: https://cloud.tencent.com/product/goosefs
category: "存储"
crawled_at: 2026-02-06T17:23:18.962331
---

# 数据加速器 GooseFS

数据加速器（Data Accelerator Goose File System，GooseFS）采用了分布式集群架构，具备高性能、低延迟、大吞吐等特性；能够为上层计算应用提供统一的命名空间和访问协议，方便用户在不同的存储系统管理和流转数据。GooseFS 能够加速海量数据分析、机器学习、人工智能等业务访问存储的性能，适用于基因计算、自动驾驶等业务场景。

[立即申请](https://cloud.tencent.com/apply/p/2t8vfv8m17b)[产品文档](https://cloud.tencent.com/document/product/1424)

- [最新活动立即使用 GooseFS + COS 构建云原生数据湖存储](https://console.cloud.tencent.com/cos/dataLake)

### GooseFS

- #### 加速方式

  缓存加速，GooseFS 提供读写缓存，数据持久化存储于对象存储 COS 中
- #### 部署模式

  独立部署（与计算节点混部）、半托管、全托管

- 极致性能：基于分布式缓存架构，为用户提供近计算端的高性能数据访问能力。
- 成本集约：充分利用计算节点的闲置本地盘资源提供数据访问加速能力。
- 生态亲和性：支持 Spark、Tensorflow 等大数据、AI计算框架，管理多种存储服务。
- 易用性：通过透明加速能力提供平滑升级能力。
- 稳定性：支持CLS、云 Prometheus等日志监控服务，简化运维流程，提升稳定性。

### GooseFSx

- #### 加速方式

  高性能加速，主机请求写入 GooseFSx 后立即返回到主机
- #### 部署模式

  全托管

- 超高性能：可提供TB/s吞吐、千万级 IOPS、亚毫秒级延时。
- 与计算生态无缝融合：兼容 POSIX 文件语义，可批量自动挂载为本地目录。
- 数据流动：主机通过 GooseFSx 立即访问 COS 数据，可将结果回写 COS。
- 冷热分层弹性高效：GooseFSx 与 COS 相互解耦，各自弹性扩展且深度融合。
- 简单易用：全托管服务、上手即用，无需关心部署、配置、调优、管理、运维等。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/iGVMG754AI9Go4tkoXxfO.png)

### 多数据源支持

可对接多种数据源，允许存储任意规模的结构化、半结构化、非结构化数据，同时可以按原样存储数据。

### 计算弹性

通过计算与存储分离，实现计算资源的弹性伸缩，满足客户对计算资源的灵活调度。

### 成本最优

为集中式存储池，可快速扩展或缩减存储资源，实现存储数据冷热分层，降低大数据分析与机器学习存储成本。

### 服务集成

无缝支持腾讯云各类计算分析、机器学习产品，包括弹性 MapReduce、流计算 Oceanus。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/4IyUuOPkdog3KJ4WpuGzX.png)

### 按需流动数据

自动执行、手动触发或周期性流动数据，主机通过 GooseFSx 立即访问和高性能处理 COS 的数据，并按需将计算结果持久化到 COS。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/I8WHYZBE0nk21bwYVnWYV.png)

### 极高性能和极低时延

采用专为高性能工作负载设计的全并行架构，性能随容量扩展而线性扩展，可提供TB/s吞吐、千万级 IOPS、亚毫秒级延时。

- 机器学习
- 大数据分析
- 交互式查询
- AI 训练仿真场景
- 高性能计算场景

高性能计算场景

高性能计算场景，需要极高的存储性能；满足不同规模 GPU 算力需求，性能线性扩展。

主要能力

- 超高性能：数据从 COS 按需预热到数据加速器，满足 HPC 计算的数百 GB 的高吞吐和亚毫秒级低延时的性能需求，性能随容量扩展而线性扩展。
- 与计算生态无缝融合：兼容 POSIX 文件语义，能够批量自动挂载成主机的本地目录，实现存储资源快速弹性供给。
- 冷热分层弹性高效：温冷数据持久化到 COS，热数据缓存到数据加速器，数据加速器与 COS 相互解耦，各自弹性伸缩，又深度融合，实现数据按需流动。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/y8SF4OUN6GEMmJiRpCVVm.png)

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/hYHgs8s3q_bi4iMvnt41e.png)

蔚来

智能电动汽车品牌

提供容器化场景下的高性能访问和文件共享服务，利用 COS 作为数据湖存储底座，为客户提供成本性能兼具的方案。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/cerDKZrAYFduw5qgpHoQn.png)

酷狗

音频媒体播放软件

通过 GooseFS 协助酷狗实时查询大数据业务优化，通过加速 IO 访问的方案协助客户提升 Presto/Spark 业务优化查询速度，实现存储性能优化。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/JTSqq1F1KA7lQ54WzJYjr.png)

高途

在线教育平台

通过 GooseFS+公有云 CHDFS 的方案实现存算分离，相比友商的本地盘方案，为客户降低了40%的整体成本，提升30%的计算作业性能。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/rsP-IW9bZe3geqZPBLAKG.png)

易久批

互联网商城平台

通过 Fluid + GooseFS 的技术方案，加速 AI 训练业务的模型分发速度，有效提升容器启动性能，实现数倍性能优化。

[### 文档总览

提供产品动态、核心特性、快速入门、开发者指南、部署指南、运维指南、云原生实践等文档指引，方便您快速上手 GooseFS。](https://cloud.tencent.com/document/product/1424)

[### 快速入门

提供入门 GooseFS 的关键路径，帮助您快速上手 GooseFS 使用。](https://cloud.tencent.com/document/product/1424/54278)

[### 产品动态

提供 GooseFS 产品更新说明，方便您了解最新版本能力。](https://cloud.tencent.com/document/product/1424/68331)

[### 核心特性

提供 GooseFS 核心特性介绍，包括缓存策略、统一命名空间、透明加速、Table 管理等特性。](https://cloud.tencent.com/document/product/1424/54286)

[### 运维指南

提供 GooseFS 的操作指南，包括部署、运维、监控等，帮助您熟悉 GooseFS 的产品使用。](https://cloud.tencent.com/document/product/1424/68305)

开始申请使用数据加速器 GooseFS。

[立即申请](https://cloud.tencent.com/apply/p/2t8vfv8m17b)
