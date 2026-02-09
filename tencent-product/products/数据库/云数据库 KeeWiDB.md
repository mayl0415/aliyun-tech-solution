---
title: "云数据库 TencentDB for KeeWiDB"
url: https://cloud.tencent.com/product/keewidb
category: "数据库"
crawled_at: 2026-02-06T17:26:39.272656
---

# 云数据库 TencentDB for KeeWiDB

云数据库 KeeWiDB 是腾讯云自研、100%兼容 Redis 协议的新一代分布式KV存储数据库，实现了数据的冷热分级，满足业务高性能、持久化、低成本、大规模的四大诉求，完美的平衡性能和成本之间的冲突。云数据库 KeeWiDB 支持主从热备，提供自动容灾切换、数据备份、故障迁移、实例监控、在线扩容、数据回档等全套的数据库服务。

### 高性能存储

新一代存储引擎采用Hash的存取方式，并与持久内存耦合，在实现数据实时持久化的同时保证单节点最大性能可达18万写入、28万读取、P99延迟小于2ms，同时可水平堆叠，性能线性提升。

![](https://cloudcache.tencent-cloud.com/qcloud/ui/static/tc_portal_icon/80b2304e-b818-4637-ac55-64eee3057f88.png)

### 低成本

基于分级存储架构，由缓存提供热数据的访问，磁盘存储全量数据，且冷热比例可灵活配置。支持数据的冷热分离、自动升热降冷，在保证热数据高性能的同时，将冷数据存储成本大幅降低。

### 开发效率高

兼容 Redis 协议和数据结构，极易上手。而缓存加存储的一体化设计可以彻底解决困扰业界多年的缓存一致性、缓存击穿、缓存雪崩等难题，大大提升业务开发效率。

### 高可用

云数据库 KeeWiDB 通过主备实时同步的架构，提供多副本高可用特性，通过高效的 Gossip 协议可以保障故障自动切换，虚拟 VIP 的方案可以保障后端故障对业务透明。

### 弹性伸缩

云数据库 KeeWiDB 提供缓存资源和磁盘容量的动态调整功能，并且提供集群架构，支持水平扩展，保障可以支持业务的全生命周期，降低业务运营成本。

### 大容量

和 Redis 受限于内存容量不一样，云数据库 KeeWiDB 将数据存储在磁盘，且集群架构支持水平扩展，单实例可提供百TB级别的存储规模，满足客户KV场景超大容量需求。

### 托管部署

只需在管理控制台中单击几下，即可在几分钟内启动并连接到一个可以立即投入生产的云数据库 KeeWiDB 服务。不需要用户自己去安装、部署、运维，减少用户的人力开销。

### 智能运维

通过智能Proxy和引擎层的多路采集，KeeWiDB提供丰富的性能、时延、网络、容量、命中率等监控指标。帮助用户提前预警风险，快速定位和解决问题。

### 数据迁移

借助数据传输服务 DTS，可以将多种场景的源数据迁移到云数据库 KeeWiDB 中，极大简化您的存量数据迁移工作，无需手动操作，实现业务无缝过渡。

- 电商场景
- 游戏全服务
- 视频直播
- 新闻/内容平台
- 画像/推荐业务

当前互联网公司的核心资产是用户，基于用户行为的画像和推荐系统也成为互联网的基础设施，画像、特征、embedding 给企业带来了海量的 KV 存储需求，请求以点读和批量导入为主。KeeWiDB 通过冷热分级存储提供大容量、低成本的 KV 存储能力；通过命令级持久化，实现高速写入，缩短批量导入的窗口时间；通过分布式架构，能够提供百TB 的存储规模。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/VpeakVrNv-7d7xCOqLz-S.png)

[### 购买指南

提供云数据库 KeeWiDB 的产品规格说明，您可以选择适合业务需求的资源。](https://cloud.tencent.com/document/product/1520/80814)

[### 快速入门

提供在控制台快速创建和连接数据库实例的指引。](https://cloud.tencent.com/document/product/1520/80816)

[### 操作指南

提供云数据库 KeeWiDB 实例以及相关产品使用过程中的常用操作指引。](https://cloud.tencent.com/document/product/1520/80820)

[### 产品性能

根据产品规格配置，提供不同数据结构的读写性能。](https://cloud.tencent.com/document/product/1520/80813)

[### 计费模式

说明云数据库 KeeWiDB 的购买方式，以及计费规则。](https://cloud.tencent.com/document/product/1520/80814)

[### 地域和可用区

查看腾讯云在境内外的地域和可用区信息。](https://cloud.tencent.com/document/product/1520/80810)

### 云数据库 KeeWiDB 100%兼容 Redis 吗？

云数据库 KeeWiDB 兼容 Redis 4.0 的协议和数据结构，不支持的命令有：

BLPOP/BRPOP/BRPOPLPUSH、SORT、MOVE、MULTI/EXEC/WATCH/UNWATCH/DISCARD、SWAPDB以及Redis的keyspace notification。

### 云数据库 KeeWiDB 是否支持Lua功能？

更多问题请查看 [常见问题](https://cloud.tencent.com/document/product/1520/80852) 。

按照我们的入门指南，只需点几次鼠标，即可创建您的首个腾讯云 KeeWiDB 实例。

