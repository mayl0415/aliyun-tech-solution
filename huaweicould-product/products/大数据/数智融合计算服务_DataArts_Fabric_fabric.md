---
title: "什么是DataArts Fabric"
code: "fabric"
category: "大数据"
source_url: "https://support.huaweicloud.com/productdesc-fabric/dataartsfabric_01_0002.html"
crawled_at: "2026-02-05T16:52:54.724293"
---

# 什么是DataArts Fabric

## 产品简介

数据+AI一站式开发平台

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-fabric/figure/zh-cn_image_0000002516459296.png)

## 详细说明

# 什么是DataArts Fabric

数智融合计算服务DataArts Fabric是华为云提供的数据+AI一站式开发平台，提供从数据处理、分析到模型微调、推理、部署上线的全生命周期管理能力，让数据工程师、数据科学家、AI应用开发工程师等多角色使用自己最熟悉的工具，在同一个工作台上工作，实现从开发到生产的高效协同。DataArts Fabric可实现自动扩缩，以支持最苛刻的应用程序。根据应用程序的需求以细粒度增量扩展资源，与为峰值负载预置资源池的服务相比，可为客户节省高达50%的成本。

DataArts Fabric基于Serverless资源池，让数据和AI的多种工作负载共池、CPU和NPU异构资源共池、开发和生产共池，变革客户的资源投资方式，实现在离线混部、训推一体，帮助客户削峰填谷，提升资源使用率。它提供极致体验，客户无需管理集群，零资源门槛启动开发和生产任务，使客户在快速变化的业务中，低成本试错。

#### 产品架构

DataArts Fabric提供高性能、高可靠、低时延、低成本的海量存储系统，与华为云的大数据服务组合使用，可大幅度降低成本，帮助企业简单快捷地管理大数据。

* **SQL引擎**

  DataArts Fabric提供分布式SQL引擎，实现了元数据服务、计算、缓存和存储的分层解耦和弹性，让每一层动态分配资源而不会影响另一层的性能或可用性。语句级别的弹性扩缩、高性能分布式分析引擎可帮助您在几秒钟内查询TB级别数据，在几分钟内查询PB级别数据。
* **分布式Ray**

  DataArts Fabric支持分布式计算框架Ray，来帮助客户解决规模日益增大的数据处理和机器学习/深度学习任务对分布式计算的问题，也为数据工程和机器学习工程提供统一的完整Workflow。DataArts Fabric Ray支持Ray-Data、Ray-Train、Ray-Serve模块，分别满足分布式数据预处理、分布式训练、分布式模型推理服务的应用场景。
* **异构资源管理**

  DataArts Fabric支持CPU+NPU资源统一纳管、统一资源分配；资源调度粒度支持容器级和Actor级，并且支持安全沙箱来实现资源隔离、可靠容错。
* **多语义缓存加速**

  DataArts Fabric提供跨引擎、多模态、多语义加速，例如数据缓存、模型缓存、CheckPoint缓存。

**图1** 产品架构图
  
![](https://support.huaweicloud.com/productdesc-fabric/figure/zh-cn_image_0000002516459296.png)

#### 访问方式

DataArts Fabric提供了多种访问方式。

当前提供了Web化的服务管理平台，即管理控制台和基于HTTPS请求的API（Application Programming Interface）管理方式。除此外，DataArts Fabric也提供SDK客户端，更进一步方便计算引擎的对接集成。

* 控制台方式

  DataArts Fabric支持通过[管理控制台](https://console.huaweicloud.com/fabric/)访问，包含Ray作业、SQL作业等功能。您可以在管理控制台端到端完成您的数据、AI开发。
* API方式

  如果您需要将DataArts Fabric集成到第三方系统，用于二次开发，请使用API方式访问DataArts Fabric。具体操作和API详细描述，请参见[API参考](https://support.huaweicloud.com/api-fabric/dataartsfabric_03_0001.html)。
* SDK方式

  如果您需要将DataArts Fabric功能集成到第三方系统，用于二次开发，可选择调用SDK方式完成目的。DataArts Fabric的SDK是对DataArts Fabric提供的REST API进行的Python/Java封装，简化用户的开发工作。具体操作和SDK详细描述，请参见[SDK参考](https://support.huaweicloud.com/sdkreference-fabric/dataartsfabric_04_0001.html)。

####
