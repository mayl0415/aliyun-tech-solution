---
title: "什么是ModelArts"
code: "modelarts"
category: "人工智能"
source_url: "https://support.huaweicloud.com/productdesc-modelarts/modelarts_01_0001.html"
crawled_at: "2026-02-05T16:30:24.597090"
---

# 什么是ModelArts

## 产品简介

面向AI开发者的一站式开发平台

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-modelarts/figure/zh-cn_image_0000001991454402.png)

## 详细说明

# 什么是ModelArts

ModelArts是华为云提供的一站式AI开发平台，提供海量数据预处理及半自动化标注、大规模分布式训练、自动化模型生成及端-边-云模型按需部署能力，帮助用户快速创建和部署模型，管理全周期AI工作流。

“一站式”是指AI开发的各个环节，包括数据处理、算法开发、模型训练、模型部署都可以在ModelArts上完成。从技术上看，ModelArts底层支持各种异构计算资源，开发者可以根据需要灵活选择使用，而不需要关心底层的技术。同时，ModelArts支持Tensorflow、PyTorch、MindSpore等主流开源的AI开发框架，也支持开发者使用自研的算法框架，匹配您的使用习惯。

#### 产品架构

ModelArts产品架构请参考[图1](#ZH-CN_TOPIC_0000001991454374__fig196178251251)。

**图1** ModelArts产品架构
  
![](https://support.huaweicloud.com/productdesc-modelarts/figure/zh-cn_image_0000001991454402.png "点击放大")

* 算力层提供全系列昇腾硬件，万卡级大规模集群管理能力，提供资源负载调度管理能力，兼容业界主流AI开发调试、训练推理框架。
* AI平台层提供端到端的AI开发工具链，支持开发者一站式完成模型开发和上线，并提供高效的资源管理能力，支持自动化故障恢复，提升AI模型开发、训练、上线全流程效率。
* AI开发工具链层提供端到端的大模型开发工具链，支持主流优质开源大模型“开箱即用”，提供大模型开发套件，提升大模型开发效率并缩短开发周期。

#### 产品形态

ModelArts提供多种产品形态，如下表所示。

**表1** ModelArts产品形态介绍

| 产品形态 | 产品定位 | 使用场景 |
| --- | --- | --- |
| ModelArts Standard | 面向AI开发者的一站式开发平台， 提供了简洁易用的管理控制台，包含自动学习、数据管理、开发环境、模型训练、模型管理、部署上线等端到端的AI开发工具链，实现AI全流程生命周期管理。 | 面向有AI开发平台诉求的用户。 |
| ModelArts Studio（MaaS） | 提供端到端的大模型生产工具链和昇腾算力资源，并预置了当前主流的第三方开源大模型。支持大模型数据生产、微调、提示词工程、应用编排等功能。 | 用户无需自建平台，可以基于MaaS平台开箱即用，对预置大模型进行二次开发，用于生产商用。 |
| ModelArts Lite-Server | 面向云主机资源型用户，基于裸金属服务器进行封装，可以通过弹性公网IP直接访问操作服务器。 | 适用于已经自建AI开发平台，仅有算力需求的用户，提供高性价比的AI算力，并预装主流AI开发套件以及自研的加速插件。 |
| ModelArts Lite-Cluster | 面向k8s资源型用户，提供k8s原生接口，用户可以直接操作资源池中的节点和k8s集群。 | 适用于已经自建AI开发平台，仅有算力需求的用户。要求用户具备k8s基础知识和技能。 |
| ModelArts Edge | 为客户提供了统一边缘部署和管理能力，支持统一纳管异构边缘设备，提供模型部署、模型管理和节点管理、资源池与负载均衡、应用商用保障等能力，帮助客户快速构建高性价比的边云协同AI解决方案。 | 适用于边缘部署场景。 |
| AI Gallery | AI Gallery百模千态社区，为用户提供优质的昇腾云AI模型开发体验和丰富的社区资源。 | 适用于AI开发探索。 |

#### 访问方式

ModelArts基于不同的产品形态提供了多种访问方式。

* **管理控制台方式**

  ModelArts Standard支持通过管理控制台访问，包含自动学习、数据管理、开发环境、模型训练、模型管理、部署上线等功能，您可以在管理控制台端到端完成您的AI开发。

  ModelArts MAAS可以通过管理控制台访问，包括大模型数据生产、微调、提示词工程、应用编排等功能。
* **SDK方式**

  如果您需要将ModelArts Standard功能集成到第三方系统，用于二次开发，可选择调用SDK方式完成目的。ModelArts的SDK是对ModelArts Standard提供的REST API进行的Python封装，简化用户的开发工作。具体操作和SDK详细描述，请参见《[SDK参考](https://support.huaweicloud.com/sdkreference-modelarts/modelarts_04_0001.html)》。

  除此之外，在ModelArts Standard的Notebook中编写代码时，也可直接调用ModelArts SDK。
* **API方式**

  如果您需要将ModelArts Standard集成到第三方系统，用于二次开发，请使用API方式访问ModelArts，具体操作和API详细描述，请参见《[API参考](https://support.huaweicloud.com/api-modelarts/modelarts_03_0002.html)》。
* **云原生方式**

  如果您使用的是ModelArts Lite Server形态，您可以通过弹性公网IP直接访问云主机，详情请参见《[ModelArts Lite Server用户指南](https://support.huaweicloud.com/usermanual-server-modelarts/usermanual-server-0002.html)》。

  如果您使用的是ModelArts Lite Cluster形态，您可以通过k8s原生接口操作集群，详情请参见《[ModelArts Lite Cluster用户指南](https://support.huaweicloud.com/usermanual-cluster-modelarts/umn-cluster-modelarts-0002.html)》。

#### 视频介绍

[![](https://support.huaweicloud.com/productdesc-modelarts/figure/zh-cn_image_0000002498519104.png)](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/support/modelarts-video/1668414834279893472.mp4)

####
