---
title: "什么是专属分布式存储服务"
code: "dss"
category: "存储"
source_url: "https://support.huaweicloud.com/productdesc-dss/zh-cn_topic_0081591984.html"
crawled_at: "2026-02-05T16:51:44.770351"
---

# 什么是专属分布式存储服务

## 产品简介

提供独享的物理存储资源

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-dss/zh-cn_image_0000002498370210.jpg)

![图片2](https://support.huaweicloud.com/productdesc-dss/zh-cn_image_0170873651.png)

## 详细说明

# 什么是专属分布式存储服务

专属分布式存储服务（Dedicated Distributed Storage Service，DSS）为您提供独享的物理存储资源，通过数据冗余和缓存加速等多项技术，提供高可用性和持久性，以及稳定的低时延性能；可灵活对接ECS、BMS以及DCC等多种不同类型的计算服务，适用于HPC、OLAP以及混合负载等应用场景。

**图1** 专属分布式存储架构图
  
![](https://support.huaweicloud.com/productdesc-dss/zh-cn_image_0000002498370210.jpg "点击放大")

#### 功能特点

* 规格丰富
  + 高IO：高性能、高扩展、高可靠，适用于性能相对较高，读写速率要求高，有实时数据存储需求的应用场景。
  + 超高IO：低时延、高性能，适用于低时延，高读写速率要求，数据密集型应用场景。
* 弹性扩展
  + 按需扩容：可根据业务需求扩容存储池。
  + 性能线性增长：支持在线扩容DSS下的磁盘，并且性能线性增长，满足业务需求。
* 安全可靠
  + 三副本冗余：数据持久性高达99.9999999%。
  + 数据加密：系统盘和数据盘均支持数据加密，保护数据安全。
* 备份恢复
  + 云备份服务：可为专属分布式存储下的磁盘创建备份，利用备份数据回滚磁盘，最大限度保障您数据的安全性和正确性，确保业务安全。

#### 专属分布式存储服务与云硬盘的区别

**表1** DSS与EVS的区别

| **服务名称** | **总体介绍** | 存储类别 | 典型应用场景 | 性能规格 |
| --- | --- | --- | --- | --- |
| 专属分布式存储服务 | 专属分布式存储服务为用户提供独享的物理存储资源，存储池资源物理隔离，数据持久性高达99.9999999%，可同时对接多种不同类型的计算服务，如ECS、BMS、DCC等，功能丰富、安全可靠。 | 存储池物理隔离，资源独享，专属存储。 | * 对接专属云中的ECS、BMS等计算服务 * 对接非专属云中的ECS、BMS等计算服务 * 混合负载，专属分布式存储可同时支持HPC、数据库、Email、OA办公、Web等多个应用混合部署 * 高性能计算 * OLAP应用 | * 高IO： 起步规格13.6TB，扩容步长13.6TB，最大可扩容至435.2TB，最大IOPS为1500 IOPS/TB。 * 超高IO： 起步规格7.225TB，扩容步长7.225TB，最大可扩容至289TB，最大IOPS为8000 IOPS/TB。 |
| 云硬盘 | 云硬盘可以为云服务器提供高可靠、高性能、规格丰富并且可弹性扩展的块存储服务。 | 共享存储池资源 | * 企业日常办公应用 * 开发测试 * 企业应用，例如SAP、Microsoft Exchange和Microsoft SharePoint等 * 分布式文件系统 * 各类数据库，例如：MongoDB、Oracle、SQL Server、MySQL和PostgreSQL等 | 云硬盘支持按需扩容，最小扩容步长为1GB，单个磁盘可由10GB扩展至32TB。 |

**图2** DSS与EVS的区别
  
![](https://support.huaweicloud.com/productdesc-dss/zh-cn_image_0170873651.png "点击放大")

####
