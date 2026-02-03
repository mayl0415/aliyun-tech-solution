---
title: Flink 与 Hologres 搭建实时数仓
source_url: https://www.aliyun.com/solution/tech-solution/flink-hologres
collected_at: 2026-02-03
---

Flink 与 Hologres 搭建实时数仓

暂无数据

- [解决方案首页](/solution/tech-solution/)

本方案将 Hologres 与 Flink 深度集成，提供一体化的实时数仓联合解决方案，实现了数仓分层之间实时数据的高效流动，解决实时数仓分层问题。本方案能够支撑实时推荐、实时风控等多种实时数仓应用场景，满足企业的实时分析需求，具有中间层数据可查、支持数仓分层复用和架构简单等优势。

适用客户

- 有需要数据实时处理、高并发查询能力的业务场景
- 寻求简化数据架构与降低运维成本的用户

[立即部署](https://www.aliyun.com/solution/tech-solution-deploy/2400021)

## 通过 Hologres 与 Flink 深度集成满足企业的实时分析需求

**高性能**

Hologres 与 Flink 原生深度集成，通过内置连接器，支持源表、结果表、维度表多种场景，支持海量数据高性能的实时写入与更新，数据写入即可查询。

**高可用**

Hologres 提供了主从多实例部署方式或计算组实例实现资源强隔离，从而保证 Flink 对 Hologres Binlog 的数据拉取不影响线上服务。

**低运维**

全链路通过 Flink 和 Hologres 完成，Hologres 提供对外提供在线服务和 OLAP 查询，每层数据可复用、可查，只需一套系统就能满足业务需求，降低运维压力和运维成本。

## Flink+Hologres 搭建实时数仓

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4234091671/CAEQYxiBgIDty43BzxkiIDgzZTE5NzJhNTlhYjQ5M2RiNTM3NzNlYzkxN2M4NTVk4610830_20240822162121.273.svg)

通过 Flink 将数据源写入 Hologres，形成 ODS 层。Flink 订阅 ODS 层的 Binlog 进行加工，形成 DWD 层再次写入 Hologres。Flink 订阅 DWD 层的 Binlog，通过计算形成 DWS 层，再次写入 Hologres。最后由 Hologres 对外提供应用查询。

**部署时长：**90 分钟

**预估费用：**35 元假设您选择的是本方案示例的资源规格，且资源运行时间不超过 1.5 小时，数据源 3 张表约 20 条数据。具体价格与您选择的资源规格、数据量、运行时长等有关，请以控制台显示的实际报价以及最终账单为准。）

**相关云产品**

- [实时数仓 Hologres](https://www.aliyun.com/product/hologres)
- [云数据库 RDS MySQL 版](https://www.aliyun.com/product/rds/mysql)
- [实时计算 Flink版](https://www.aliyun.com/product/bigdata/sc)

[立即部署](https://www.aliyun.com/solution/tech-solution-deploy/2400021)

## 技术方案的广泛应用场景

  ### 实时报表查询

  持各个业务方快速查询交易数据、行为数据、用户画像标签等报表。

  ### 实时推荐

  基于实时用户行为数据，分析用户行为和兴趣，为用户提供针对性的推荐。

  ### 实时监控

  通过对业务数据进行实时处理和分析，实现对业务的实时监控，及时发现业务异常和问题。

## 阿里云为您提供云产品免费试用

[立即部署](https://www.aliyun.com/solution/tech-solution-deploy/2400021)

上一篇：无

下一篇：无

该文章对您有帮助吗？

反馈
