---
title: "云数据库 TencentDB for CTSDB"
url: https://cloud.tencent.com/product/ctsdb
category: "数据库"
crawled_at: 2026-02-06T17:26:32.543188
---

# 云数据库 TencentDB for CTSDB

腾讯云时序数据库（TencentDB for CTSDB）是一种高效、安全、易用的云上时序数据存储服务。特别适用于物联网、大数据和互联网监控等拥有海量时序数据的场景。您可以根据实际业务需求快速创建CTSDB 实例，并随着业务变化实时线性扩展实例。

### 高性能服务

通过批量接口写入数据，降低网络开销。采用数据先写入内存，再周期性的Dump 为不可变的文件存储的策略提高写入性能。通过倒排索引加速任意维度数据查询，能实现数据秒级可查。

### 低成本存储

采用列式存储以及高效的编码和压缩算法提高数据压缩比。通过表 Rollup 功能，对历史数据做聚合，支持指定数据过期时间，数据按时间分区管理，过期后自动清理，降低存储成本。

### 稳定可靠

提供丰富多样的监控指标，实时监控实例健康状态。使用分布式部署方式，有效应对集群内单点故障。数据多副本存储，多个副本在故障时能自动切换，保证系统的高可用性。

### 简单易用

提供丰富的数据类型，并采用 RESTful API 接口。可弹性扩展，并且数据自动实现均衡。兼容 Elasticsearch 的数据访问协议，开发简单。控制台提供丰富的数据管理和运维功能，操作简单便捷。

### 超强聚合分析能力

不仅支持 Min、Max、Sum、Avg 等基本聚合分析，也支持Group By、区间、Geo 和嵌套等复杂的聚合分析，还支持脚本聚合，例如可对多字段计算结果做聚合。

### 安全防护

通过 VPC 网络的访问方式实现外网隔离和用户资源全面隔离。完善的网络监控服务保障您的网络安全。强大的用户鉴权和授权机制，保证数据安全性。

- 物联网环境监控
- 互联网业务监控和分析
- 大数据实时分析

自动交易算法持续收集金融市场的交易数据，各种采集终端上报的用户社交及购物娱乐数据以及日志清洗程序得到的业务状态数据等都可以存储在 CTSDB 数据库，然后通过 API 获取数据，以便实现高效实时分析及建模等需求。

![](https://mc.qcloudimg.com/static/img/6c2db7f80b150763f2529ab8342aa509/image.svg)

[2023-04

全新推出时序数据库 InfluxDB 版分布式集群，兼容开源协议和生态，支持云原生扩展、聚合分析等。](https://cloud.tencent.com/document/product/652/89877)

[2022-02

新增支持类 SQL 查询，优化数据压缩和写入性能。](https://cloud.tencent.com/document/product/652/48652)

[2021-10

腾讯云时序数据库 CTSDB 支持 Prometheus 数据的远程存储 Remote Storage。](https://cloud.tencent.com/document/product/652/48652)

[2021-06

时序数据库 CTSDB 上线硅谷、孟买地域，分别覆盖美国、亚太南部用户的需求。](https://cloud.tencent.com/document/product/652/31908)

[2021-05

时序数据库 CTSDB 上线法兰克福地域，覆盖欧洲地区用户的需求。](https://cloud.tencent.com/document/product/652/31908)

[2021-03

时序数据库 CTSDB 上线新加坡地域，覆盖亚太和东南亚地区的需求。](https://cloud.tencent.com/document/product/652/31908)

[2020-09

集群节点数量小于30个时，可充分满足使用要求；超过30个时，可新购或将通用集群架构优化升级。](https://cloud.tencent.com/document/product/652/13532)

[2020-08

随着 CTSDB 上线多伦多一区，时序数据库 CTSDB 已经上线华北、华东、华南和北美等地区。](https://cloud.tencent.com/document/product/652/31908)

[2020-07

用户可通过配置告警策略，设定告警阈值，便于第一时间了解到实例的运行状态。](https://cloud.tencent.com/document/product/652/13542)

[2018-12

腾讯云时序数据库 CTSDB 于2018年12月正式上线，可达每秒千万级数据点写入，亿级数据秒级分析。](https://cloud.tencent.com/document/product/652/13531)

上一页

下一页

[### 产品简介

帮助您快速了解时序数据库 CTSDB 产品的定位、概述、优势、以及具体功能。](https://cloud.tencent.com/document/product/652)

[### 快速入门

创建 CTSDB 实例后，您还需要进行 CTSDB 实例的初始化，以轻松启用实例。](https://cloud.tencent.com/document/product/652/13537)

[### 操作指南

本文将为您介绍时序数据库 CTSDB 的基本操作及系统限制等内容。](https://cloud.tencent.com/document/product/652/31936)

[### 开发指南

时序数据库 CTSDB 支持 HTTP 协议进行数据写入和查询等操作。](https://cloud.tencent.com/document/product/652/13611)

[### 最佳实践

云数据库 CTSDB 是一款分布式、可扩展、支持近实时数据搜索与分析的时序数据库。](https://cloud.tencent.com/document/product/652/17737)

[### 地域和可用区

查看腾讯云在境内外的地域和可用区信息。](https://cloud.tencent.com/document/product/652/31908)

### 定价

时序数据库 CTSDB 目前支持包年包月和按量计费两种模式（按量计费购买前需要实名认证，详见实名认证指引）。

- [计费概述](https://cloud.tencent.com/document/product/652/31944)
- [产品定价](https://cloud.tencent.com/document/product/652/31942)
- [购买方式](https://cloud.tencent.com/document/product/652/19153)
- [续费说明](https://cloud.tencent.com/document/product/652/31937)
- [欠费说明](https://cloud.tencent.com/document/product/652/31943)
- [退款说明](https://cloud.tencent.com/document/product/652/31945)

### 怎么连接 CTSDB？

CTSDB 提供基于 HTTP 协议，以 JSON 为数据交互格式的 RESTful API 供用户访问，发送请求的同时需加上实例的用户名和密码。

### CTSDB 如何保证高性能查询的？

### CTSDB 相比较关系数据库的优势是什么？

### CTSDB 目前提供什么网络类型的连接？

更多问题请查看 [常见问题](https://cloud.tencent.com/document/product/652/13547)，也可在 [问答社区](https://cloud.tencent.com/developer/ask) 中进行提问 。

按照我们的入门指南，只需点几次鼠标，即可创建您的首个腾讯云 CTSDB。

