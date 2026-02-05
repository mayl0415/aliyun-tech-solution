---
title: "什么是云数据库 GeminiDB"
code: "nosql"
category: "数据库"
source_url: "https://support.huaweicloud.com/productdesc-nosql/nosql_introduction.html"
crawled_at: "2026-02-05T16:52:19.625540"
---

# 什么是云数据库 GeminiDB

## 产品简介

云原生多模NoSQL，兼容Redis®/Influx

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-nosql/public_sys-resources/note_3.0-zh-cn.png)

## 详细说明

# 什么是云数据库 GeminiDB

云数据库 GeminiDB是一款基于计算存储分离架构的分布式多模NoSQL数据库服务。在云计算平台高性能、高可用、高可靠、高安全、可弹性伸缩的基础上，提供了一键部署、备份恢复、监控报警等服务能力。

云数据库 GeminiDB目前兼容Redis、DynamoDB、Cassandra、HBase、InfluxDB和MongoDB主流NoSQL接口，并提供高读写性能，具有高性价比，适用于IoT、气象、互联网、游戏等领域。

![](https://support.huaweicloud.com/productdesc-nosql/public_sys-resources/note_3.0-zh-cn.png) 

GeminiDB Mongo接口的版本已进入EOS（End of Service & support）阶段，自该版本停止服务后：

* GeminiDB Mongo接口将不再允许创建该版本的实例。
* GeminiDB Mongo接口对于已有的该版本实例，将不再提供任何技术支持，包括新功能更新、漏洞修复、补丁升级，以及工单指导和在线排查等客户支持服务。
* GeminiDB Mongo接口不再适用于GeminiDB Mongo的服务等级协议（SLA）保障。

#### 如何选择接口

不同接口的适用场景及功能存在差异，您可以根据业务需要选择接口产品。

**表1** 场景说明

| **接口名称** | **兼容接口** | **使用场景** | **说明** |
| --- | --- | --- | --- |
| [GeminiDB Redis接口](https://support.huaweicloud.com/redisug-nosql/nosql_05_0053.html) | 兼容Key-Value接口：Redis | GeminiDB提供高并发、低延迟业务访问。具备极致弹性扩缩容能力，从容应对业务高峰。常见的用户场景包括游戏、广告RTA、推荐系统、电商、教育等。 | GeminiDB Redis是一款100%兼容Redis协议的弹性KV数据库，支持远超内存的容量和极致的性能。它具有稳定低延迟、高性价比、无需备节点，全主架构、具备4:1超高数据压缩等优势，支持Hash Field过期、布隆过滤器、数据极速导入、内存加速等企业级特性。 |
| [GeminiDB兼容DynamoDB接口](https://support.huaweicloud.com/dynamodbug-nosql/nosql_dynamodb_0003.html) | 兼容Key-Value接口：DynamoDB | GeminiDB兼容DynamoDB接口适用于高并发web应用、物联网、电商和零售等场景的可灵活扩展的KV数据库，提供稳定低时延、海量数据存储/查询能力。 | GeminiDB兼容DynamoDB接口对外提供DynamoDB格式的HTTPS服务。同时还能保持原有的CQL协议，可以通过SDK/CLI访问数据库服务。在协议层面完全支持AWS DynamoDB，用户可以在不改造业务代码的情况下，平滑地迁移至GeminiDB。 |
| [GeminiDB Cassandra接口](https://support.huaweicloud.com/cassandraug-nosql/nosql_05_0013.html) | 兼容宽列接口：Cassandra | GeminiDB CassandraGeminiDB Cassandra接口支持TB级别存储及近百万级QPS，提供强一致性级别，可适配各类应用场景，尤其是大规模集群部署：例如工业制造和气象业、互联网等海量数据存储的场景。 | GeminiDB Cassandra 接口 是一款基于华为自研的计算存储分离架构，兼容Cassandra生态的云原生NoSQL数据库，支持类SQL语法CQL。具有安全可靠、超强读写、弹性扩展、便捷管理等特点。 |
| [GeminiDB兼容Hbase接口](https://support.huaweicloud.com/hbaseug-nosql/nosql_hbase_004.html) | 兼容宽列接口：HBase | GeminiDB兼容HBase接口适用于大规模数据存储、实时查询、高可靠性和可伸缩性要求的场景，特别适用于与Hadoop和大数据处理技术集成的环境中。 | GeminiDB兼容HBase接口是一款兼容HBase生态的分布式NoSQL数据库，具有高性能、高可靠性、强大的扩展性和灵活的伸缩性等特点。 |
| [GeminiDB Influx接口](https://support.huaweicloud.com/influxug-nosql/nosql_05_0039.html) | 兼容时间序列型接口：InfluxDB | GeminiDB Influx接口广泛应用于资源监控，业务监控分析，物联网设备实时监控，工业生产监控，生产质量评估和故障回溯等。 | GeminiDB Influx 接口是一款基于华为自研的计算存储分离架构，兼容InfluxDB生态的云原生NoSQL时序数据库。提供大并发的时序数据读写，压缩存储和类SQL查询，并且支持多维聚合计算和数据可视化分析能力。具有高写入、灵活弹性、高压缩率和高查询等特点。 |
| [GeminiDB Mongo接口](https://support.huaweicloud.com/mongoug-nosql/nosql_05_0023.html) | 兼容文档型接口：MongoDB | GeminiDB Mongo接口近百万级QPS，开源3倍性能提升，支持存海量文档、图片、IoT/车联网数据、社交视频/语音等，适用于互联网、物联网、游戏、金融等领域。 | GeminiDB Mongo 接口是一款基于华为自研的计算存储分离架构，兼容MongoDB生态的云原生NoSQL数据库。具有企业级性能、灵活弹性、高可靠、可视化管理等特点。 |

####
