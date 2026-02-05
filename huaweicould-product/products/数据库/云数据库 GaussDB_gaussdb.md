---
title: "什么是云数据库GaussDB"
code: "gaussdb"
category: "数据库"
source_url: "https://support.huaweicloud.com/productdesc-gaussdb/gaussdb_01_003.html"
crawled_at: "2026-02-05T16:30:05.964285"
---

# 什么是云数据库GaussDB

## 产品简介

新一代企业级分布式关系型数据库产品

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-gaussdb/figure/zh-cn_image_0000001692617257.png)

![图片2](https://support.huaweicloud.com/productdesc-gaussdb/figure/zh-cn_image_0000001629385838.png)

## 详细说明

# 什么是云数据库GaussDB

GaussDB是华为自主创新研发的分布式关系型数据库。该产品支持分布式事务，同城跨AZ部署，数据0丢失，PB级海量存储。同时拥有云上高可用，高可靠，高安全，弹性伸缩，一键部署，快速备份恢复，监控告警等关键能力，能为企业提供功能全面，稳定可靠，扩展性强，性能优越的企业级数据库服务。

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-gaussdb/figure/zh-cn_image_0000002367683721.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/support/opengauss-video/1719996582469644199.mp4)

#### 成长地图

您可以通过[云数据库GaussDB成长地图](https://support.huaweicloud.com/gaussdb/index.html)快速了解GaussDB的相关概念、入门使用和高手进阶等。

#### 如何使用云数据库GaussDB

您可以通过如下方式使用GaussDB。

* 管理控制台：您可以使用[管理控制台](https://auth.huaweicloud.com/authui/login?#/login)为您提供的Web界面完成GaussDB的相关操作。
* API：您可以编写代码调用API使用GaussDB，请参考[《云数据库GaussDB API参考》](https://support.huaweicloud.com/api-gaussdb/gaussdb_api_001.html)。

#### GaussDB分布式版形态整体架构

GaussDB分布式版形态整体架构如下：

**图1** GaussDB分布式版形态整体架构图
  
![](https://support.huaweicloud.com/productdesc-gaussdb/figure/zh-cn_image_0000001692617257.png "点击放大")

* Coordinator Node：协调节点CN，负责接收来自应用的访问请求，并向客户端返回执行结果；负责分解任务，并调度任务分片在各DN上并行执行。
* GTM：全局事务管理器（Global Transaction Manager），负责生成和维护全局事务ID、事务快照、时间戳、Sequence信息等全局唯一的信息。
* Data Node：数据节点DN，负责存储业务数据、执行数据查询任务以及向CN返回执行结果。

#### GaussDB 集中式形态整体架构

GaussDB 集中式形态整体架构如下：

**图2** GaussDB集中式形态整体架构图
  
![](https://support.huaweicloud.com/productdesc-gaussdb/figure/zh-cn_image_0000001629385838.png "点击放大")

* ETCD：分布式键值存储系统（Editable Text Configuration Daemon）。用于共享配置和服务发现（服务注册和查找）。
* CMS：集群管理组件（Cluster Management Server）。是用于管理集群状态的部件。
* Data Node：数据节点DN，负责存储业务数据、执行数据查询任务以及返回执行结果。

####
