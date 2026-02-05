---
title: "什么是湖仓构建LakeFormation"
code: "lakeformation"
category: "大数据"
source_url: "https://support.huaweicloud.com/productdesc-lakeformation/lakeformation_01_0001.html"
crawled_at: "2026-02-05T16:31:44.188323"
---

# 什么是湖仓构建LakeFormation

## 产品简介

高效搭建数智融合一体化解决方案

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-lakeformation/zh-cn_image_0000001878825509.png)

## 详细说明

# 什么是湖仓构建LakeFormation

湖仓构建（DataArts Lake Formation，简称LakeFormation）是企业级数据湖一站式构建服务，在存算分离架构基础上提供数据湖元数据统一管理的可视化界面及API，兼容Hive元数据模型以及Ranger权限模型，支持对接MapReduce服务（MRS）、数据仓库服务（DWS）、数据湖探索（DLI）、AI开发平台ModelArts、数据治理中心 DataArts Studio等多种计算引擎及大数据云服务，使用户可以便捷高效地构建数据湖和运营相关业务，加速释放业务数据价值。

LakeFormation产品通过底层资源实现跨AZ部署及高可靠、弹性伸缩、元数据统一管理、元数据与文件目录联动授权、对接多计算引擎等功能，是一个Serverless服务。

#### LakeFormation架构

LakeFormation服务架构图如[图1](#lakeformation_01_0001__fig18831136112919)所示。

**图1** LakeFormation服务架构
  
![](https://support.huaweicloud.com/productdesc-lakeformation/zh-cn_image_0000001878825509.png "点击放大")

LakeFormation功能包括元数据管理、数据权限管理、控制台、API。

* 元数据基于Hive元数据模型，支持Catalog、数据库、表、函数等元数据对象。
* 数据权限管理提供权限策略的配置和对应的权限访问控制。
  + 授权主体支持IAM用户和用户组以及LakeFormation角色。
  + 授权对象支持Catalog、数据库、表及列、函数等元数据对象，也支持OBS路径。
  + 授权操作包含元数据对象的相关操作，以及OBS路径的读写操作。
* Console支持实例管理、元数据管理、数据权限管理、接入管理、任务管理等操作。
* API层提供兼容Hive社区的元数据接口，以及兼容Ranger社区的权限同步接口，以便与MRS、DWS等服务集成对接。

#### 产品优势

* 生态开放

  遵循开源事实标准，支撑存量业务平滑演进。

  + 提供兼容Hive/Spark/Flink/Trino社区的元数据接口，支持计算引擎平滑对接。
  + 提供兼容Ranger的权限接口，一次授权，统一生效。
  + 提供迁移工具，支持存量MRS集群相关元数据的平滑迁移。
* 数智融合

  打通大数据的数据壁垒，实现真正数智融合。

  + 支持数据库、表、函数、模型、非结构化数据集等统一管理。
  + 实现统一的细粒度数据权限管理，支持跨服务/跨集群的数据共享。
* 大规格高可靠

  支撑超大规模大数据业务的高可靠。

  + 超大规模元数据管理能力。
  + 统一权限管理能力，支持海量细粒度权限管理。
  + 支持多AZ的容灾能力。
* 简单易用

  提供基于元数据的增值管理能力。

  + Serverless架构，开箱即用。
  + 提供数据湖管理、元数据统计等管理能力。

#### 访问方式

当前提供了Web化的服务管理平台，即管理控制台和基于HTTPS请求的API（Application programming interface）管理方式。除此外，LakeFormation也提供SDK客户端，更进一步方便计算引擎的对接集成。

* API方式

  如果用户需要将公有云平台上的LakeFormation实例集成到第三方系统，用于二次开发，可使用API方式访问LakeFormation实例，具体操作请参见[API参考](https://support.huaweicloud.com/api-lakeformation/lakeformation_04_0002.html)。
* 控制台方式

  如果用户已注册公有云，用户可使用管理控制台方式，从服务列表中选择“大数据 > 湖仓构建 LakeFormation”访问LakeFormation。
* SDK方式
  + LakeFormation提供兼容Hive元数据模型的SDK客户端，如果用户需要将Hive、Spark等计算引擎对接LakeFormation，用于统一元数据管理，可使用SDK方式访问LakeFormation实例。
  + LakeFormation提供了REST（Representational State Transfer）风格API，支持通过HTTPS请求调用。
  + SDK使用的具体操作请参见[SDK参考](https://support.huaweicloud.com/sdkreference-lakeformation/lakeformation_07_0001.html)。

####
