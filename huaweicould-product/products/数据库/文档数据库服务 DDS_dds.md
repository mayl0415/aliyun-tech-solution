---
title: "什么是文档数据库服务"
code: "dds"
category: "数据库"
source_url: "https://support.huaweicloud.com/productdesc-dds/zh-cn_topic_introduction.html"
crawled_at: "2026-02-05T16:29:59.730108"
---

# 什么是文档数据库服务

## 产品简介

支持集群和副本集部署，弹性伸缩

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-dds/zh-cn_image_0000001233316043.png)

![图片2](https://support.huaweicloud.com/productdesc-dds/zh-cn_image_0000001197407563.png)

## 详细说明

# 什么是文档数据库服务

文档数据库服务（Document Database Service，简称DDS）完全兼容MongoDB协议，提供安全、高可用、高可靠、弹性伸缩和易用的数据库服务，同时提供一键部署、弹性扩容、容灾、备份、恢复、监控和告警等功能，支持通过兼容MongoDB协议的BI、Spark等第三方组件进行对接。

使用DDS之前，需要您了解MongoDB和MongoDB协议相关的内容，请参考[官方文档](https://docs.mongodb.com/manual/introduction/)。

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-dds/zh-cn_image_0000002366992590.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/DDS/Videos/1751271953662322791.mp4)

#### 存储结构

**图1** 存储结构图
  
![](https://support.huaweicloud.com/productdesc-dds/zh-cn_image_0000001233316043.png)

如上图所示，DDS的基本管理单元是实例，与关系型数据库不同，DDS实例由数据库、集合、文档三部分组成。

DDS完全兼容MongoDB协议，所以在一些术语、数据结构、基本语法上同MongoDB是一致的。如下表格提供了MongoDB和关系型数据库中一些常见术语的映射关系，便于您理解和更好地使用DDS。

**表1** 术语解释

| **MongoDB中的术语** | **说明** | **关系型数据库中对应的术语** |
| --- | --- | --- |
| 数据库（Database） | 一个DDS实例中可以建立多个数据库，一个数据库中可以建立多个集合。 | 数据库（Database） |
| 集合（Collection） | 集合就是MongoDB文档组，一个集合可以包含多个文档。 | 表（Table） |
| 文档（Document） | 文档是一组键值(key-value)对(即BSON)，是MongoDB中最基本的单元。 | 行（Row） |

#### 数据结构

MongoDB一般采用类似JSON的格式存储，存储的内容是文档型的。如下图，示例中提供了关系型数据库和MongoDB数据库中的数据结构对比，帮助您更直观地了解MongoDB中的一些概念。

**图2** 数据结构
  
![](https://support.huaweicloud.com/productdesc-dds/zh-cn_image_0000001197407563.png)

#### 为什么选择文档数据库服务

请参见[产品优势](https://support.huaweicloud.com/productdesc-dds/dds_01_0040.html)和[典型应用](https://support.huaweicloud.com/productdesc-dds/dds_01_0015.html)。

#### 成长地图

您可以通过[成长地图](https://support.huaweicloud.com/dds/index.html)快速了解DDS的相关概念、入门使用、高手进阶和操作视频等。

#### 产品价格

详情请参见[计费说明](https://support.huaweicloud.com/price-dds/dds_billing_001.html)。

#### 如何访问文档数据库服务

您可以通过以下两种方式使用DDS。

* 控制台方式

  如果已[注册华为账号并开通华为云](https://support.huaweicloud.com/usermanual-account/account_id_001.html)，可直接登录[管理控制台](https://auth.huaweicloud.com/authui/login?#/login)，从主页选择“数据库 > 文档数据库服务”。

  如果未[注册华为账号并开通华为云](https://support.huaweicloud.com/usermanual-account/account_id_001.html)，请在[华为云官网](https://www.huaweicloud.com/)注册，具体操作请参见[如何注册华为云管理控制台的用户](https://support.huaweicloud.com/qs-consolehome/zh-cn_topic_0016739341.html)。
* API方式

  您可以通过编写代码调用API来访问文档数据库服务，具体操作请参见《[文档数据库服务API参考](https://support.huaweicloud.com/api-dds/dds_api_reference.html)》。

#### 兼容的引擎和版本

文档数据库服务兼容的引擎和版本，请参见[引擎和版本](https://support.huaweicloud.com/productdesc-dds/dds_01_0014.html)。

#### 部署建议

建议从以下维度考虑如何创建并使用文档数据库服务。

* 区域和可用区：区域和可用区决定了文档数据库实例所在的物理位置，文档数据库实例创建成功后，将无法更换区域。您可以根据用户地理位置、产品资源价格、容灾能力和网络时延等因素，选择区域和可用区。更多信息，请参见[区域和可用区](https://support.huaweicloud.com/productdesc-dds/dds_01_0023.html)。
* 网络规划：创建文档数据库实例时，推荐使用系统部署的弹性云服务器（Elastic Cloud Server，简称ECS）所使用的虚拟私有云（Virtual Private Network，简称VPC）和子网。
* 数据安全：文档数据库服务提供了全面的安全保障。您可以通过多可用区部署、审计日志、网络隔离、安全组、加密等多手段保障数据库的数据安全。

####
