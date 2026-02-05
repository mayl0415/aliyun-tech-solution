---
title: "数据湖探索简介"
code: "dli"
category: "大数据"
source_url: "https://support.huaweicloud.com/productdesc-dli/dli_01_0378.html"
crawled_at: "2026-02-05T16:31:23.581235"
---

# 数据湖探索简介

## 产品简介

流处理、批处理的融合处理分析服务

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-dli/zh-cn_image_0000002363625685.png)

## 详细说明

# 数据湖探索简介

#### 什么是数据湖探索

数据湖探索（Data Lake Insight，简称DLI）是完全兼容[Apache Spark](https://spark.apache.org/)、[Apache Flink](https://flink.apache.org/)生态，提供一站式的流处理、批处理、交互式分析的Serverless融合处理分析服务。用户不需要管理任何服务器，即开即用。

DLI支持标准SQL、Spark SQL、Flink SQL，支持多种接入方式，并兼容主流数据格式。数据无需复杂的抽取、转换、加载，使用SQL或程序就可以对云上[CloudTable](https://support.huaweicloud.com/productdesc-cloudtable/cloudtable_01_0002.html)、[RDS](https://support.huaweicloud.com/productdesc-rds/zh-cn_topic_dashboard.html)、[DWS](https://support.huaweicloud.com/productdesc-dws/dws_01_0002.html)、[CSS](https://support.huaweicloud.com/productdesc-css/css_04_0001.html)、[OBS](https://support.huaweicloud.com/productdesc-obs/zh-cn_topic_0045829060.html)、[ECS](https://support.huaweicloud.com/productdesc-ecs/zh-cn_topic_0013771112.html)自建数据库以及线下数据库的异构数据进行探索。

#### 视频简介

视频介绍什么是数据湖探索服务。

[![](https://support.huaweicloud.com/productdesc-dli/zh-cn_image_0000002339215629.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/dli-video/1739254996490328901.mp4)

#### DLI计算引擎

DLI提供了多种计算引擎，Spark引擎、Flink引擎，分别适用于不同的数据处理场景。

Spark更适合大规模数据的批处理和复杂分析，而Flink则在实时流处理方面表现出色。

* [Spark引擎](#)
* [Flink引擎](#)

* **功能特点**：

  Spark是用于大规模数据处理的统一分析引擎，聚焦于查询计算分析。

  DLI在开源Spark基础上进行了大量的性能优化与服务化改造，不仅兼容Apache Spark生态和接口，性能较开源提升了2.5倍，在小时级即可实现EB级数据查询分析。

  DLI的Spark引擎支持大规模数据的批处理和交互式分析，提供高性能的分布式计算能力。
* **适用场景**：
  + 适用于需要进行大规模数据批处理和复杂数据分析的场景。
  + 适合对历史数据进行深度挖掘和分析，例如数据仓库中的数据查询和报表生成。

* **功能特点**
  + Flink是一款分布式计算引擎，既可以用于批处理，也可以用于流处理。
  + DLI在开源Flink基础上进行了特性增强和安全增强，提供了数据处理所需的Stream SQL特性。
  + 支持实时流处理，能够处理大规模的实时数据流，支持事件时间处理和状态管理
* **适用场景**
  + 适用于需要实时处理数据流的场景，例如实时监控系统、实时推荐系统。
  + 适合对实时数据进行快速分析和响应，例如金融交易监控、物联网设备数据处理。

#### 核心功能

DLI详细的功能清单请参考[DLI功能总览](https://support.huaweicloud.com/productdesc-dli/dli_01_0698.html)。

**表1** DLI核心功能

| 功能分类 | 功能描述 |
| --- | --- |
| DLI是基于Serverless架构的数据处理和分析服务 | DLI是无服务器化的大数据查询分析服务，使用DLI服务您只需为实际使用的弹性计算资源付费，无需维护和管理云服务器。   * 计算资源按量计费：真正的按使用量（扫描量/CU时）计费，不运行作业时0费用。 * 自动扩缩容：根据业务负载，对计算资源进行预估和自动扩缩容。 |
| DLI支持多种类型的计算引擎 | 完全兼容Apache Spark、Apache Flink等生态，支持标准SQL、Spark SQL、Flink SQL，兼容CSV、JSON、Parquet和ORC主流数据格式。   * **Spark**是用于大规模数据处理的统一分析引擎，聚焦于查询计算分析。DLI在开源Spark基础上进行了大量的性能优化与服务化改造，不仅兼容Apache Spark生态和接口，性能较开源提升了2.5倍，在小时级即可实现EB级数据查询分析。 * **Flink**是一款分布式的计算引擎，可以用来做批处理，即处理静态的数据集、历史的数据集；也可以用来做流处理，即实时地处理一些实时数据流，实时地产生数据的结果。DLI在开源Flink基础上进行了特性增强和安全增强，提供了数据处理所必须的Stream SQL特性。 |
| DLI支持多种连接方式 | DLI提供了多种连接方式满足不同的用户需求和使用场景。  DLI支持的链接方式：   * 控制台方式 * API方式 * SDK方式 * 客户端工具 * 使用DataArts服务提交DLI作业 * 对接BI工具的可视化分析   更多DLI连接方式的介绍请参考[DLI支持的开发工具](https://support.huaweicloud.com/productdesc-dli/dli_07_0028.html)。 |
| DLI支持对接多种数据源的跨源分析 | * Spark跨源连接：可通过DLI访问CloudTable，DWS，RDS和CSS等数据源。具体内容请参考[《数据湖探索用户指南》](https://support.huaweicloud.com/usermanual-dli/dli_01_0426.html)。 * Flink跨源支持与多种云服务连通，形成丰富的流生态圈。数据湖探索的流生态分为云服务生态和开源生态：   + 云服务生态：数据湖探索在Flink SQL中支持与其他服务的连通。用户可以直接使用SQL从这些服务中读写数据。如DIS、OBS、CloudTable、MRS、RDS、SMN、DCS等。   + 开源生态：通过增强型跨源连接建立与其他VPC的网络连接后，用户可以在数据湖探索的租户授权的队列中访问所有Flink和Spark支持的数据源与输出源，如Kafka、Hbase、ElasticSearch等。 具体内容请参见[《数据湖探索开发指南》](https://support.huaweicloud.com/devg-dli/dli_09_0162.html)。 |
| DLI支持的三大基本作业类型 | * SQL作业支持SQL查询功能：可为用户提供标准的SQL语句。具体内容请参考[《数据湖探索SQL语法参考》](https://support.huaweicloud.com/sqlref-spark-dli/dli_08_0071.html)。 * Flink作业支持Flink SQL在线分析功能：支持Window、Join等聚合函数，用SQL表达业务逻辑，简便快捷实现业务。具体内容请参考[Flink OpenSource SQL语法参考](https://support.huaweicloud.com/sqlref-flink-dli/dli_08_15012.html)。 * Spark作业提供全托管式Spark计算特性：用户可通过交互式会话(session)和批处理(batch)方式提交计算任务，在全托管Spark队列上进行数据分析。具体内容请参考[《数据湖探索API参考》](https://support.huaweicloud.com/api-dli/dli_02_0194.html)。 |
| DLI支持存算分离 | 用户将数据存储到OBS后，DLI可以直接和OBS对接进行数据分析。存算分离的架构下，使得存储资源和计算资源可以分开申请和计费，降低了成本并提高了资源利用率。  存算分离场景下，DLI支持OBS在创建桶时数据冗余策略选择单AZ或者多AZ存储，两种存储策略区别如下：   * 选择多AZ存储，数据将冗余存储至多个AZ中，可靠性更高。选择多AZ存储的桶，数据将存储在同一区域的多个不同AZ。当某个AZ不可用时，仍然能够从其他AZ正常访问数据，适用于对可靠性要求较高的数据存储场景。建议优选使用多AZ存储的策略。 * 选择单AZ存储，数据仅存储在单个AZ中，但相比多AZ更加便宜。收费详情请参见[OBS产品价格详情](https://www.huaweicloud.com/pricing.html?tab=detail#/obs)。 |
| DLI通过弹性资源池实现对资源的统一的管理和调度 | 弹性资源池后端采用CCE集群的架构，支持异构，对资源进行统一的管理和调度。  详细内容可以参考DLI用户指南的[弹性资源池和队列简介](https://support.huaweicloud.com/usermanual-dli/dli_01_0504.html)。 |

#### DLI产品结构

DLI的产品结构如下：

**图1** DLI Serverless架构
  
![](https://support.huaweicloud.com/productdesc-dli/zh-cn_image_0000002363625685.png "点击放大")

DLI产品架构中包括以下核心模块：

**表2** DLI架构核心模块简介

| 模块名称 | 功能说明 |
| --- | --- |
| 生态工具 | 数据湖探索（DLI）通过其强大的Serverless架构和多模引擎支持，能够满足不同行业的多样化需求，推动各行业的数字化转型和创新。 |
| 计算引擎 | * Spark：支持大规模数据的批处理和交互式分析，提供高性能的分布式计算能力。 * Flink：支持实时流处理，能够处理大规模的实时数据流，支持事件时间处理和状态管理。 |
| 统一资源管理 | * 资源解耦：DLI采用存算分离架构，将计算资源和存储资源解耦，您可以根据实际需求灵活调整计算资源和存储资源的配比，提高资源利用率，降低成本。 * 弹性伸缩：DLI计算资源基于容器化Kubernetes，具有弹性伸缩能力。能够根据作业需求自动调整资源配置，响应作业需求。 * 多租户支持：支持计算资源按租户隔离，确保不同租户之间的资源独立。每个租户可以独立管理自己的计算资源，实现资源的精细化管理，帮助企业实现部门间的数据共享和权限管理。 * 计算资源按量付费：您只需为实际使用的计算资源付费，无需预先购买和管理服务器，提高资源的使用效率。 |
| 统一元数据管理 | * 多源元数据整合：DLI支持对多种数据源的元数据进行统一管理，包括云上数据源（如OBS、RDS、DWS、CSS等）和云下数据源（如自建数据库、Redis等）。您无需将数据搬迁到统一的数据湖中，即可实现对不同数据源的元数据的管理和分析。 * 元数据同步：DLI提供的元数据管理功能确保元数据的实时性和一致性。 * 元数据查询与管理：DLI提供标准SQL接口，用户可以使用SQL语句查询和管理元数据。支持对元数据的增删改查操作，方便用户进行数据治理和分析。 * 数据安全与权限管理：支持数据目录、数据库和表的权限管理。用户可以对不同租户和用户组设置不同的权限，确保数据的安全性和合规性。 |
| 存储服务 | 使用OBS、数据库存储用于数据分析的结构化或非结构化数据，提供数据的持久化存储服务。 |
| 数据源连接 | * 支持对接云上数据源，例如OBS：对象存储服务，用于存储和管理非结构化数据。RDS关系型数据库服务，用于存储和管理结构化数据。DWS数据仓库服务，用于高效的数据查询和分析。 * 支持对接云下数据源，例如自建数据库场景，如MySQL、PostgreSQL、HDFS数据。 |
| 数据应用 | 支持对接业界主流BI工具、 灵活满足数据展示需求。 |

#### 如何访问DLI

云服务平台提供了Web化的服务管理平台，既可以通过管理控制台和基于HTTPS请求的API（Application programming interface）管理方式来访问DLI，又可以通过JDBC客户端连接DLI服务端。

更多DLI连接方式请参考[DLI支持的开发工具](https://support.huaweicloud.com/productdesc-dli/dli_07_0028.html)。

* 管理控制台方式

  提交SQL作业、Spark作业或Flink作业，均可以使用管理控制台方式访问DLI服务。

  登录管理控制台，从主页选择“EI企业智能”>“EI大数据”>“数据湖探索”。

* API方式

  如果用户需要将云平台上的DLI服务集成到第三方系统，用于二次开发，可以使用API方式访问DLI服务。

  具体操作请参见[《数据湖探索API参考》](https://support.huaweicloud.com/api-dli/dli_02_0174.html)。
* JDBC

  DLI支持使用JDBC连接服务端进行数据查询操作。具体内容请参考[《数据湖探索开发指南》](https://support.huaweicloud.com/devg-dli/dli_09_0125.html)。
* 数据治理中心DataArts Studio

  数据治理中心DataArts Studio具有数据全生命周期管理、智能数据管理能力的一站式治理运营平台，支持行业知识库智能化建设，支持大数据存储、大数据计算分析引擎等数据底座，帮助企业快速构建从数据接入到数据分析的端到端智能数据系统，消除数据孤岛，统一数据标准，加快数据变现，实现数字化转型。

  在DataArts Studio管理中心控制台创建数据连接即可访问DLI，进行数据分析。

  关于DataArts Studio的操作指导请参考《[数据治理中心产品文档](https://support.huaweicloud.com/dataartsstudio/index.html)》。

####
