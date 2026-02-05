---
title: "什么是分布式数据库中间件"
code: "ddm"
category: "数据库"
source_url: "https://support.huaweicloud.com/productdesc-ddm/ddm_01_0001.html"
crawled_at: "2026-02-05T16:52:16.471127"
---

# 什么是分布式数据库中间件

## 产品简介

突破容量和性能瓶颈，支持数据高并发访问

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-ddm/zh-cn_image_0000001222317300.png)

![图片2](https://support.huaweicloud.com/productdesc-ddm/zh-cn_image_0000001269775385.png)

## 详细说明

# 什么是分布式数据库中间件

#### 产品定义

分布式数据库中间件（Distributed Database Middleware，简称DDM），是一款分布式关系型数据库中间件。兼容MySQL协议，专注于解决数据库分布式扩展问题，突破传统数据库的容量和性能瓶颈，实现海量数据高并发访问。

DDM是由华为云自主研发的云原生分布式数据库中间件，采用存算分离架构，提供分库分表、读写分离、弹性扩容等能力，具有稳定可靠、高度可扩展、持续可运维的特点。服务器集群管理对用户完全透明，用户通过DDM管理控制台进行数据库运维与数据读写，提供类似传统单机数据库的使用体验。

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-ddm/zh-cn_image_0000001934500053.png)](https://bbs-video.huaweicloud.com/video/media/20181026/20181026182003_86761.mp4)

#### 产品优势

* 自动分库分表

  传统数据库通常是单机部署，一旦出现问题，数据可能全部丢失，故障影响面100%。

  而DDM支持自动分库分表，将数据分散到多个数据节点存储，分散风险，影响面降低至1/N，支撑业务爆发式增长。
* 读写分离

  DDM充分利用数据节点只读实例能力，当水平拆分后，依然存在较大查询压力，则可以开启读写分离能力，业务系统无需改造，提升数据库处理能力和访问效率，轻松应对高并发场景。
* 弹性扩容

  传统数据库计算能力和存储能力有限，CPU/内存/网络处理能力受限于机器配置，存储受限于SSD或者云盘的大小，只能支撑中小规模的业务系统。

  而DDM既支持计算层（DDM）扩容（增加节点数或提升节点规格），也支持存储层在线扩容，存储层扩容可以通过增加分片数或者数据节点数来解决单表数据量过多和容量瓶颈等问题，确保计算、存储均可线性扩展，解决业务在快速发展的过程中针对数据库扩展性产生的后顾之忧与运维压力。

#### 业务架构

**图1** DDM业务架构
  
![](https://support.huaweicloud.com/productdesc-ddm/zh-cn_image_0000001222317300.png)

#### DDM原理

**图2** DDM原理
  
![](https://support.huaweicloud.com/productdesc-ddm/zh-cn_image_0000001269775385.png)

####
