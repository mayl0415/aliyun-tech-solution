---
title: "什么是云数据库TaurusDB企业版"
code: "taurusdb"
category: "数据库"
source_url: "https://support.huaweicloud.com/productdesc-taurusdb/introduction.html"
crawled_at: "2026-02-05T16:30:18.312568"
---

# 什么是云数据库TaurusDB企业版

## 产品简介

新一代完全兼容MySQL的企业级数据库

## 详细说明

# 什么是云数据库TaurusDB企业版

云数据库TaurusDB企业版是华为自研的最新一代企业级高扩展高性能云原生数据库，完全兼容MySQL。基于华为最新一代DFV存储，采用计算存储分离架构，128TB的海量存储，故障秒级切换，既拥有商业数据库的高可用和性能，又具备开源低成本效益。

TaurusDB企业版支持的版本请参见[TaurusDB引擎和版本](https://support.huaweicloud.com/productdesc-taurusdb/taurusdb_01_0005.html)。

云数据库TaurusDB支持企业版和标准版两种产品形态。企业版和标准版的区别请参见[TaurusDB企业版和标准版有什么区别](https://support.huaweicloud.com/taurusdb_faq/taurusdb_faq_0330.html)。

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-taurusdb/figure/zh-cn_image_0000002310820866.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/support/taurusdb-video/1746601055755857492.mp4)

#### **成长地图**

您可以通过[成长地图](https://support.huaweicloud.com/taurusdb/index.html)快速了解TaurusDB的相关概念、入门使用、高手进阶等。

#### **如何使用TaurusDB**

您可以通过如下方式使用TaurusDB。

管理控制台：您可以使用[管理控制台](https://auth.huaweicloud.com/authui/login?#/login)为您提供的Web界面完成TaurusDB的相关操作。

了解[TaurusDB产品优势](https://support.huaweicloud.com/productdesc-taurusdb/taurusdb_01_0002.html)可以帮助您更好地选购TaurusDB。

#### 产品优势

* 性能强悍
  + 采用计算与存储分离，日志即数据架构，性能提升至开源MySQL的7倍。
  + 通过RDMA协议进行数据库传输，使IO性能不再成为瓶颈。
  + 引入内核特性，例如Query result cache、Query plan cache、Online DDL等，提升用户体验。
* 弹性扩展
  + 横向扩展：1写15只读节点，快速添加只读节点，满足高并发场景性能需求。
  + 纵向扩展：分钟级规格升降级，轻松应对业务高峰。
* 高可靠性
  + 支持跨可用区部署，跨区域备份，提升实例容灾能力。
  + 存储三副本，数据更安全。
  + 共享分布式存储，主节点故障时，只读节点自动升级成主节点，RPO为0。
  + 主从节点时延支持ms级，保证业务高可用。
* 安全防护
  + 采用共享分布式存储，故障秒级恢复，数据“0”丢失。
  + 采用VPC、安全组、SSL连接和数据加密等严格控制安全访问。
  + 已通过ISO 27001、CSA、可信云、等保三级等国内外15+安全认证，国内首家获得NIST CSF最高认证。
* 高兼容性

  完全兼容MySQL，应用无需改造即可轻松迁移上云。
* 高效备份
  + 全量备份采用快照机制，秒级完成创建快照，具有更高的备份效率。
  + 基于底层存储系统的多时间点特性，不需增量日志回放，可直接实现按时间点回滚。
* 海量存储
  + 华为自研DFV分布式存储，容量高达128TB。
  + 根据数据量自动伸缩，无需提前规划，节约成本。
* 算子下推

  将过滤条件、列投影、聚合运算从计算节点下推到存储节点，跨存储节点并行处理，减少网络流量和计算节点的压力，提升查询执行效率。同时与并行查询功能进行融合，达成全流程并行执行。

####
