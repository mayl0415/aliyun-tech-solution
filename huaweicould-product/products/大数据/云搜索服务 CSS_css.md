---
title: "什么是云搜索服务"
code: "css"
category: "大数据"
source_url: "https://support.huaweicloud.com/productdesc-css/css_04_0001.html"
crawled_at: "2026-02-05T16:31:29.300986"
---

# 什么是云搜索服务

## 产品简介

提供多条件检索与分析能力

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-css/figure/zh-cn_image_0000002473930140.png)

## 详细说明

# 什么是云搜索服务

#### 什么是云搜索服务

云搜索服务（Cloud Search Service，简称CSS）是华为云ELK生态的一系列软件集合，是一个基于Elasticsearch、OpenSearch且完全托管的在线分布式搜索服务，为用户提供更丰富、更灵活的检索和分析功能，可处理结构化、非结构化文本及基于AI向量的多条件检索、统计和报表等功能。CSS服务兼容Elasticsearch、OpenSearch、Logstash、Kibana、OpenSearch Dashboards、Cerebro等软件，支持自动部署，可快速创建集群，拥有免运维、完善的监控体系等特点，能让用户更专注于业务逻辑的实现，适用于日志分析、智能客服、知识库问答、个性化推荐等多种业务场景。

* **Elasticsearch**

  基于开源Elasticsearch构建的托管分布式搜索引擎服务，支持结构化与非结构化数据的多条件检索、统计分析和报表生成。CSS服务基于开源Elasticsearch实现了内核增强，完全兼容Elasticsearch生态工具链，无缝对接ELK（Elasticsearch/Logstash/Kibana）技术栈。适用于日志分析、业务数据检索、实时数据可视化等场景，尤其适合需要完善的数据分析生态和社区支持的用户。Elasticsearch搜索引擎的深入介绍请参见[《Elasticsearch：权威指南》](https://www.elastic.co/guide/cn/elasticsearch/guide/current/index.html)。
* **OpenSearch**

  基于开源OpenSearch构建的托管分布式搜索引擎服务，作为Elasticsearch的技术演进方向，继承其核心能力并扩展新特性。CSS服务基于开源OpenSearch实现了内核增强，完全兼容OpenSearch生态工具链，适配云原生技术趋势。适用于需要弹性扩展能力、持续功能迭代及长期技术演进保障的用户。OpenSearch搜索引擎的深入介绍请参见[《OpenSearch Documentation》](https://opensearch.org/docs/latest/)。
* **向量数据库**

  CSS向量数据库是云搜索服务推出的一款高性能向量检索服务，其核心基于自主研发的向量搜索引擎，能够提供业界领先的千亿级向量检索服务。CSS向量数据库基于Elasticsearch/OpenSearch的向量检索功能，面向图像、视频、语料等非结构化数据的特征向量检索场景，提供高性能、高精度的最近邻或近似近邻检索服务。典型应用场景包括：以图搜图/视频、相似商品推荐、语义文本检索、跨模态检索（如用文本搜图片）等。
* **Logstash**

  基于开源Logstash提供的服务器端数据处理管道服务，专注于数据采集、解析、转换与输出，是ELK生态中数据接入的核心组件。支持从多种数据源采集数据，经过数据处理输出至目的端。适用于日志管理、数据集成和实时数据处理场景。Logstash工具的深入介绍请参见[《Logstash Documentation》](https://www.elastic.co/guide/en/logstash/current/index.html)。
* **Kibana**

  Kibana是Elasticsearch官方提供的可视化分析平台，适用于需要深度数据分析和交互式可视化的场景。CSS服务的Elasticsearch集群默认集成开箱即用的Kibana工具，无需安装部署即可一键启动。Kibana不仅提供丰富的仪表盘构建能力和可视化工具，还深度整合了Elasticsearch的统计分析功能，支持从数据探索到业务洞察的全流程分析。
* **OpenSearch Dashboards**

  OpenSearch Dashboards是专为OpenSearch设计的可视化分析平台，适用于需要深度数据分析和交互式可视化的场景。CSS服务的OpenSearch集群默认集成开箱即用的OpenSearch Dashboards工具，无需安装部署即可一键启动。OpenSearch Dashboards不仅提供丰富的仪表盘构建能力和可视化工具，还深度整合了OpenSearch的统计分析功能，支持从数据探索到业务洞察的全流程分析。
* **Cerebro**

  Cerebro是Elasticsearch/OpenSearch管理的专业工具，适用于需要实时监控和高效运维的场景。CSS服务的Elasticsearch和OpenSearch集群默认集成开箱即用的Cerebro工具，无需安装部署即可一键启动。Cerebro可以快速查看集群的健康状态、节点分布、索引详情等关键信息。对于日常运维场景（如分片调整、索引管理、性能监控等），推荐选择Cerebro，其直观的集群拓扑视图和丰富的管理功能可显著提升运维效率，同时降低操作复杂度，适用于开发、运维及数据分析等多角色用户。

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-css/figure/zh-cn_image_0000001975746540.png)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/support/css-video/CSS_Introduction_zh.mp4)

#### 产品功能

* 生态兼容

  兼容Elasticsearch、OpenSearch生态，支持原生接口。
* 多数据源接入

  无缝对接FTP/OBS/Hbase/Kafka等多种数据源。
* 弹性扩缩容

  按需申请，支持灵活调整资源，业务不中断。
* 备份与恢复

  支持自动备份快照，按需恢复快照到本集群或其他集群，提高数据可靠性。

更多产品功能请参见[产品功能](https://support.huaweicloud.com/productdesc-css/css_04_0003.html)。

#### 产品架构

CSS服务产品结构如[图1](#ZH-CN_TOPIC_0000001981470313__fig1689810315118)所示。CSS服务集合了Elasticsearch、OpenSearch和向量数据库三大搜索引擎，通过自主研发的内核增强、管理增强能力，实现具有高性能、高可用、高性价比的云搜索服务。

**图1** CSS产品架构
  
![](https://support.huaweicloud.com/productdesc-css/figure/zh-cn_image_0000002473930140.png "点击放大")

#### 访问方式

华为云提供了Web化的服务管理平台，即管理控制台和基于HTTPS请求的API（Application programming interface）管理方式。

* API方式

  如果用户需要将华为云上的云搜索服务集成到第三方系统，用于二次开发，请使用API方式访问CSS集群，具体操作请参见[《云搜索服务API参考》](https://support.huaweicloud.com/api-css/css_03_0001.html)。
* 控制台方式

  其他相关操作，请使用管理控制台方式访问云搜索服务。如果用户已注册华为云，可直接登录管理控制台，在服务列表搜索“云搜索服务”。如果未注册，请参见[注册华为云并实名认证](https://support.huaweicloud.com/usermanual-account/account_id_001.html)。

#### CSS服务快速入门

* [使用Elasticsearch搜索数据](https://support.huaweicloud.com/qs-css/index.html)
* [使用OpenSearch搜索数据](https://support.huaweicloud.com/qs-css/css_08_0003.html)
* [使用Logstash迁移数据](https://support.huaweicloud.com/qs-css/css_08_0004.html)

####
