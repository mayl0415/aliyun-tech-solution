---
title: "云数据库 TencentDB for Memcached"
url: https://cloud.tencent.com/product/cmem
category: "数据库"
crawled_at: 2026-02-06T17:26:25.743727
---

# 云数据库 TencentDB for Memcached

腾讯云数据库 Memcached（TencentDB for Memcached）是腾讯自主研发的极高性能、内存级、持久化、分布式 Key-Value 存储服务。适用于高速缓存的场景，兼容 Memcached 协议，为您提供主从热备、自动容灾切换、数据备份、故障迁移、实例监控全套服务。腾讯云数据库 Memcached 现已停售，请移步使用腾讯云数据库 Redis® 的 Memcached 引擎。

### 托管部署

只需在管理控制台中单击几下，即可在几分钟内启动并连接到一个可以立即投入生产的 Memcached 服务。无需用户自己去安装、部署、运维，减少用户的人力开销。

### 数据保障机制

采用主从热备的架构，主机数据自动同步到备机，数据保持一致。当主机出现故障时，系统会自动检测到故障，服务切换到备机，在过程中您无需做任务处理，无需担心数据丢失，保证您的业务正常运行不中断。

### 高性能

云数据库 Memcached 由腾讯研发团队自研多年，兼容 Memcached 绝大多数协议，并优化了核心源代码，现已用于腾讯内部多个系统。单台 Cache 服务器支持50万次/秒的访问，帮助您轻松应对高峰时段的海量访问。

### 平滑扩展

提供自动扩容功能，当存储容量达到一定值时，系统会自动调整容量大小，扩容过程中业务无中断，您无需关心容量使用瓶颈，只需考虑写入和读出数据即可。

### 全面的日常监控

提供专业数据指标的监控，如 CPU 负载、QPS 等，支持操作可视化的数据展示以及自定义告警，您可以在控制台实例详情里点击查看每个指标的数据曲线图获取实例运行状态。

![](https://qcloudimg.tencent-cloud.cn/raw/19bc84e4269a14256d0de8d384a26408.png)

### 高性价比

云数据库 Memcached 部署在云端，只要2元/G/天，价格比自建至少便宜50%（考虑主从架构的备机成本）。同时云端部署极大节省了您前期搭建基础网络设施的成本和后期的维护成本。

- 游戏数据缓存
- 互联网 / APP
- 电子商务

在电子商务网站中，商品分类数据、商品搜索结果的列表数据以及可查看的商品数据和商家基本数据这类数据访问量特别高但不会经常改变。在该场景下，您可以通过云数据库 Memcached 将这类数据缓存起来进行快速读写，提高访问速率。

![](https://qcloudimg.tencent-cloud.cn/raw/af75a2288c7106fded4edd78856c4075.svg)

- 深圳地铁
- 微众银行
- 晶泰科技
- 人民网

[### 产品简介

帮助您快速了解云数据库 Memcached 产品的定位、概述、优势、以及具体功能。](https://cloud.tencent.com/document/product/241/7489)

[### 快速入门

本文将为您介绍云数据库 Memcached 快速入门及示例代码。](https://cloud.tencent.com/document/product/241/1582)

[### 操作指南

本文将为您介绍云数据库 Memcached 访问管理概述及查看监控。](https://cloud.tencent.com/document/product/241/38709)

[### 购买指南

云数据库 Memcached 计费采用按量计费方式，结算周期为月结。](https://cloud.tencent.com/document/product/241/1548)

### 云数据库 Memcached 可以提供事务支持吗？或者腾讯有相应的开发计划吗？

在分布式存储系统上实现事务是非常复杂的问题，即便在学术界也没有相对好的解决方案。云数据库 Memcached 目前无法提供事务特性，开发者必须自行实现回滚操作，以避免影响数据一致性。建议开发者尽量避免对事务的依赖。

### 云数据库 Memcached 是否提供 Memcached 的API？

### 我们的游戏数据可能非常庞大，云数据库 Memcached 能自动扩容到多大容量？

### 云数据库 Memcached 可以自助清理所有数据么？

### 云数据库 Memcached 能提供多大的访问量？需要扩容怎么办？

更多问题请查看 [常见问题](https://cloud.tencent.com/document/product/241/3243)，也可在 [问答社区](https://cloud.tencent.com/developer/ask) 中进行提问 。

按照我们的入门指南，只需点几次鼠标，即可创建您的腾讯云数据库 Memcached 实例。

