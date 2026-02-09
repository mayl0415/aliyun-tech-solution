---
title: "分布式数据库TDSQL"
url: https://cloud.tencent.com/product/tddbms
category: "数据库"
crawled_at: 2026-02-06T17:25:35.504537
---

# 分布式数据库TDSQL

分布式数据库TDSQL是腾讯打造的一款高性能企业级数据库产品，具备强一致高可用、高 SQL 兼容度、分布式水平扩展、完整事务支持、企业级安全等特性，并且通过中国信息安全测评中心安全可靠测评，为客户提供完整可靠的分布式数据库解决方案。

[TDSQL生态认证](https://tpartner.cloud.tencent.com/adapterCertification/index)[私有化版本咨询](https://wj.qq.com/s2/14461826/61ea/)

- [产品公告TDSQL Boundless发布上线](https://cloud.tencent.com/document/product/557/109571)

- TDSQL Boundless
- 其他企业级分布式数据库

- [TDSQL兼容MySQL版 (InnoDB引擎)

  TDSQL InnoDB引擎版基于TXSQL企业级内核优化，是一种支持水平拆分、主从架构的分布式数据库，兼容支持MySQL不同内核版本，是金融类OLTP场景核心交易系统的首选数据库](https://cloud.tencent.com/document/product/557/7700)

  - 兼容MySQL 8.0
  - 兼容MySQL 5.7
- [TDSQL兼容PostgreSQL版

  TDSQL PostgreSQL版针对PostgreSQL 10进行了深度的内核优化，集高扩展性、SQL 高兼容度、完整的分布式事务支持、多级容灾及多维度资源隔离等功能于一身，采用无共享的集群架构，提供容灾、备份、恢复、监控、安全、审计等全套解决方案](https://cloud.tencent.com/document/product/1129)

  - 兼容PostgreSQL 10
- [TDSQL安全可靠版

  TDSQL安全可靠版通过中国信息安全测评中心安全可靠测评，基于TencentOS Server开发，适配海光、鲲鹏服务器， 全面支持国密SM4，满足金融、政务等高安全场景的合规要求。](https://cloud.tencent.com/document/product/557/122958)

  - 支持独享集群形态
  - 兼容MySQL 8.0
  - 兼容MySQL 5.7

![](https://qcloudimg.tencent-cloud.cn/raw/0506bcbe17e1d2af2491c23bbd64d8ab.png)

### 自动水平拆分

TDSQL支持对数据库大表自动水平拆分，系统自动将数据均匀的分布到不同物理节点中，查询也自动聚合返回；数据分布对业务系统透明，业务实际所见为一张逻辑完整的表，无需感知后端的物理架构。

### 领先的分布式架构

TDSQL 提供多种管理方案来进行分布式事务管理，通过分布式事务特性，全局唯一数字序列，JSON 等能力，为开发者提供灵活的开发方案。通过自主专利的分布式事务一致性技术来保证在全分布式环境下的事务一致性。

![](https://qcloudimg.tencent-cloud.cn/raw/89c54d938ee8d84876a8bf12f4908744.png)

### 不停机弹性扩展

当数据库性能或容量不足以支撑业务发展时，在控制台点击，即可自动升级完成。升级过程中，您无需关心分布式系统内的数据迁移，均衡和路由切换。升级完成后访问 IP 不变，仅在自动切换时存在秒级闪断，您仅需确保有重连机制即可。

### 强同步复制

TDSQL 默认采用主从架构，可确保99.999%以上可用性；系统支持强同步复制以提供数据强一致，业务系统写入数据后，只有当数据库从机同步后才给予应用事务应答，确保主从数据完全一致，不会因故障导致数据丢失、错乱，且强同步复制性能已基本等于异步复制。

![](https://qcloudimg.tencent-cloud.cn/raw/be72b0976974f51069cd5d421ae82ad6.png)

### 超高性能

TDSQL 深度定制开发数据库内核，性能远超于同引擎的开源产品；支持读写分离，有效提供读扩展的同时提供开发灵活性；对数据库连接分配逻辑进行了深度优化，在重负载时表现更佳；并配置 NVMe SSD 的硬盘，提供高于 SATA 四倍以上的 IO 配置，帮助您更轻松满足业务性能需求。

![](https://qcloudimg.tencent-cloud.cn/raw/96d856788f528fc2b40d3f247a404951.png)

### 提供公有云和专有云部署

TDSQL 提供多种部署形态。在公有云，提供多租户和独享物理集群两种部署形态，可于控制台简单快速生产 TDSQL 数据库。在专有云，可部署在腾讯专有云 TCE、腾讯云 TStack 中；亦可独立部署，或以数据库一体机方式输出。

![](https://qcloudimg.tencent-cloud.cn/raw/6a7875203eb6e137ab26e896dbd3621d.png)

### 企业级的数据安全

TDSQL 支持一主多从能力，数据强同步一致性。支持三权分立的体系，并能够提供数据透明加密，数据脱敏访问，强制访问控制等多个层级的数据安全保障能力。可扩展支持中国标准的商用密码加密算法，符合等保2.0和密评相关要求。

### 兼容多种数据库引擎

TDSQL 兼容 MySQL、MariaDB、PostgreSQL 协议，高度兼容 Oracle 语法；并提供了高性能联机事务处理(OLTP)能力和海量的联机分析处理(OLAP) 处理能力，可降低业务架构复杂度和成本，是去O的理想选择。

![](https://qcloudimg.tencent-cloud.cn/raw/548310318ffd156ed9fcfa3256251bca.png)

### 安全可靠

TDSQL通过中国信息安全测评中心安全可靠测评，基于TencentOS Server开发，适配海光、鲲鹏服务器， 全面支持国密SM4，满足金融、政务等高安全场景的合规要求。

- 实时高并发事务系统
- 金融级核心交易系统
- HTAP 业务系统
- 物联网类应用系统
- 温/冷数据归档

冷数据存储是一个覆盖各种行业的场景。用户往往需要在存储时间和成本之间做出权衡，且传统方案存在难以检索的困扰。TDSQL 支持 LSM Tree 引擎，提供超高压缩率，让归档成本大幅降低，并提供高并发在线检索能力。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/oB0QUVZ7lQAv7GcxJLMJn.svg)

- 深圳地铁
- 微众银行
- 晶泰科技
- 人民网
- 顺丰速运
- 大众点评
- 58
- 永辉超市
- 新东方
- 印象笔记
- 印象笔记
- 印象笔记
- 印象笔记
- 印象笔记
- 印象笔记
- 印象笔记
- 印象笔记
- 印象笔记

您可以进入  [分布式数据库 TDSQL 控制台](https://console.cloud.tencent.com/tdsqld) 快速创建 TDSQL 实例，轻松开始使用云数据库 TDSQL。

