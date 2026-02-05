---
title: "什么是CloudTable"
code: "cloudtable"
category: "大数据"
source_url: "https://support.huaweicloud.com/productdesc-cloudtable/cloudtable_01_0002.html"
crawled_at: "2026-02-05T16:31:35.343312"
---

# 什么是CloudTable

## 产品简介

企业级托管型云数仓产品

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-cloudtable/zh-cn_image_0000002444266401.png)

## 详细说明

# 什么是CloudTable

表格存储服务（CloudTable Service，简称CloudTable）是基于HBase、Doris、ClickHouse、StarRocks提供的全托管数据存储和分析服务。CloudTable提供GB~PB级数据存储和分析能力，用于在线查询、数据仓库、数据集市、实时分析等场景。可被广泛应用于互联网、物联网、车联网、金融、政府、物流、制造、零售等行业。表格存储服务为用户提供专属集群，即开即用，适合业务吞吐量大，时延要求低的用户。

* CloudTable提供基于HBase全托管的NoSQL服务，提供毫秒级随机读写能力，适用于海量（半）结构化、时空、时序数据存储，可被广泛应用于物联网、车联网、金融、智慧城市、气象等行业。更多请参见[HBase](https://support.huaweicloud.com/productdesc-cloudtable/cloudtable_02_0011.html)组件介绍。
* CloudTable提供基于Doris全托管的实时数仓服务，仅需亚秒级响应时间即可返回海量数据下的查询结果，不仅可以支持高并发的点查询场景，也可以支持高吞吐的复杂分析场景。因此，Doris能够较好的满足报表分析、即席查询、统一数仓构建、数据湖联邦查询加速等使用场景，用户可以在此之上构建用户行为分析、AB实验平台、日志检索分析、用户画像分析、订单分析等应用。更多请参见[Doris](https://support.huaweicloud.com/productdesc-cloudtable/cloudtable_02_0013.html)组件介绍。
* CloudTable ClickHouse是一款开源的面向联机分析处理的列式数据库，其独立于Hadoop大数据体系，最核心的特点是压缩率和极速查询性能。同时，ClickHouse支持SQL查询，且查询性能好，特别是基于大宽表的聚合分析查询性能非常优异，比其他分析型数据库速度快一个数量级。更多请参见[ClickHouse](https://support.huaweicloud.com/productdesc-cloudtable/cloudtable_02_0015.html)组件介绍。
* CloudTable提供基于StarRocks全托管分析型数据仓库，可以灵活创建和管理集群以及数据。使用向量化、MPP架构、CBO、智能物化视图、可实时更新的列式存储引擎等技术实现多维、实时、高并发的数据分析。更多请参见[StarRocks](https://support.huaweicloud.com/productdesc-cloudtable/cloudtable_02_0017.html)组件介绍。

#### CloudTable产品架构

CloudTable产品架构如下图所示：

**图1** 产品架构
  
![](https://support.huaweicloud.com/productdesc-cloudtable/zh-cn_image_0000002444266401.png "点击放大")

* Doris：MySQL生态，易上手，多表复杂分析性能优于传统MPP。
* ClickHouse：万列大宽表多维聚合分析，亚秒级响应，全自助分析。
* HBase：高并发，毫秒级查询响应。
* StarRocks：MySQL生态，易上手，多表聚合查询，轻量化交互式分析。

#### 产品优势

* 丰富场景：兼容HBase、Doris、ClickHouse、StarRocks等引擎。
* 高可靠：架构高可用，内核深度优化，提升系统稳定性。
* 高性价比：支持冷热分离，不同压缩算法，存储成本低。
* 简单易用：通过控制台分钟级构建分析集群，提供完善的集群运维管理、监控告警等功能，使您无需关注底层基础设施，利用完善的SQL语句支持，专注于数据价值的分析。

#### 首次使用CloudTable

如果您是首次使用CloudTable的用户，建议您学习并了解如下信息：

* 基础知识了解

  通过CloudTable产品功能章节的内容，了解CloudTable相关的基础知识，包含CloudTable各组件的基本原理和场景介绍，以及CloudTable服务的特有概念和功能的详细介绍。
* 入门使用

  您可以参考[《快速入门》](https://support.huaweicloud.com/qs-cloudtable/cloudtable_06_0001.html)学习并上手使用CloudTable。《快速入门》提供了样例的详细操作指导，您可以基于此操作指导，创建和使用CloudTable集群。
* 使用更多的功能，并查看其相关操作指导

  如果您是一个CloudTable集群使用人员，可以参考[用户指南](https://support.huaweicloud.com/usermanual-cloudtable/cloudtable_01_0020.html)完成集群创建、参数配置、查看告警等操作。

  如果您是一个开发者，可以参考CloudTable提供的[开发指南](https://support.huaweicloud.com/devg-cloudtable/cloudtable_dev_process.html)操作指导及样例工程开发并运行调测自己的应用程序。您也可以通过API调用完成CloudTable集群创建/查询操作，您可以参考[《API参考》](https://support.huaweicloud.com/api-cloudtable/CreateCluster.html)获取详情。

####
