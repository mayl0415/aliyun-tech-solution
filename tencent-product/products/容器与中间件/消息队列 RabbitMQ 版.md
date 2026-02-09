---
title: "消息队列 TDMQ for RabbitMQ 版"
url: https://cloud.tencent.com/product/trabbit
category: "容器与中间件"
crawled_at: 2026-02-06T17:20:46.063267
---

# 消息队列 TDMQ for RabbitMQ 版

消息队列 TDMQ for RabbitMQ® 版（TDMQ for RabbitMQ，简称 TDMQ RabbitMQ 版）是一款分布式高可用的消息队列服务，支持AMQP 0-9-1 协议，完全兼容开源 RabbitMQ 的各个组件与概念，同时具备计算存储分离，灵活扩缩容的底层优势。（RabbitMQ 是Broadcom, Inc. 在美国和其他国家的商标）

- [产品公告RabbitMQ Serverless 版本正式发布](https://cloud.tencent.com/document/product/1495/119443)
- [技术实践自建 RabbitMQ 集群迁移上云](https://cloud.tencent.com/document/product/1495/65411)

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/AVWjW5keigqrF3w0zGsXW.png)

### 兼容开源

支持 AMQP 0-9-1 版本标准协议，完全支持 RabbitMQ 开源社区和 Queue、Exchange、Vhost 组件。一键迁移开源 RabbitMQ 元数据，实现迁移上云 0 成本。

### 功能完备

TDMQ RabbitMQ 版支持原生 RabbitMQ 的各类消息模型。支持死信交换机与备用交换机，用户无需担心由于消息过期、路由失败等因素造成的消息丢失。支持优先级队列，保证消息按优先级顺序消费。

### 稳定可靠

TDMQ RabbitMQ 版的持久化机制保证服务重启后元数据与消息内容不丢失。消息采用三副本存储策略，某台物理机故障时，能够实现数据的快速迁移，保证用户数据3个备份可用，服务可用性不低于99.99%。

### 高扩展性

TDMQ RabbitMQ 版相比于开源 RabbitMQ 版支持更高的队列数量，可扩展能力强，底层系统可根据业务规模自动弹性伸缩，扩容、缩容集群规模，对用户透明。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/JfXCqBNGA9X-e7viX5Vxb.png)

### 易用免运维

提供 API 访问接口，支持开源所有语言和版本的 SDK。提供腾讯云平台整套运维服务，实时监控告警，帮助用户快速发现并解决问题，保证服务的可用性。

1w亿

每日支撑1w亿+消息

1000+

每日服务超过1000个业务

99.95%

SLA 服务可用性不低于99.95%

10万

集群生产消费性能高达10万 TPS

## TDMQ RabbitMQ 版专享特惠

自建开源 RabbitMQ 集群

消息队列 RabbitMQ 版

跨AZ高可用部署

跨AZ高可用部署

支持但较为繁琐，需要自行设计部署方案和参数

跨AZ高可用部署

支持跨 AZ 高可用部署，成熟的故障恢复方案

在线升级

在线升级

不支持，需要手动操作，可能影响业务运行

在线升级

支持产品化水平/垂直扩容，按需升级集群规格

开箱即用

开箱即用

开源控制台可以看到部分监控指标

开箱即用

提供成熟化的部署、监控方案，开箱即用

监控告警

监控告警

开源控制台可以看到部分监控指标，若需要集成节点 CPU 利用率等其他指标，需要自行搭建并维护开源监控系统

监控告警

支持实例、节点、vhost、queue、exchange 等多维度监控告警。支持智能巡检，自动化运维，提供极致排障体验。

管控操作权限控制

管控操作权限控制

管控操作权限难以精细化控制

管控操作权限控制

控制台操作基于腾讯云 CAM 控制权限，安全合规

操作可追溯

操作可追溯

不支持

操作可追溯

管控操作对接操作审计，可回溯

展开

- 秒杀
- 优先级消息
- 延迟消息
- 消息广播
- 灵活路由

随着微服务架构的流行，服务拆分得较细，服务的数据会以消息的形式，使用精心设计的分发策略发送到不同的队列中去。这时可以充分地利用 RabbitMQ 灵活的消息路由的能力，将消息分发到目标 Queue 中。可以使用的场景：

日志处理场景，可以将日志按类型投递到不同的 Queue。例如 Error 单独一个处理队列，优先处理。

电商物流系统的物流信息按地域分发给不同的消费端进行处理。

复杂路由场景

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/3egmtpo_JBuXDdalt0pzq.svg)

### 相关云产品

[消息队列 CKafka 版](https://cloud.tencent.com/product/ckafka)

[消息队列 RocketMQ 版](https://cloud.tencent.com/product/trocket)

[![](https://qcloudimg.tencent-cloud.cn/image/product/2777/32_32/blue.svg)

消息队列 Pulsar 版](https://cloud.tencent.com/product/tpulsar)

- 飞书深诺
- 领星
- 光宇游戏
- 上海家化

2023

- 03月

  03-15

  03-15

  已发布

  支持指定接入点IP

  选择 VPC 网络接入时，支持指定 IP，当变更接入方式时可以通过指定 IP 来保持 IP 不发生变化。

- 03月

  03-15

  03-15

  已发布

  支持SSL/TLS传输加密

  选择 VPC 网络接入时，支持SSL/TLS传输加密。

- 03月

  03-15

  03-15

  已发布

  创建用户时支持选择角色

  创建用户时支持选择角色，不用角色适用不同的权限范围。

- 03月

  03-15

  03-15

  已发布

  接入外部监控 Prometheus

  提供 Prometheus 抓取节点的监控指标，包括Queue、Channel、Connection等基本监控度量指标，以及 broker JMX 暴露出的度量指标。

- 03月

  03-15

  03-15

  已发布

  支持消息查询

  如果消息收发异常或有遗漏等问题，您可以使用 TDMQ RabbitMQ 版控制台的消息查询功能，便于及时分析和定位问题。

- 03月

  03-15

  03-15

  已发布

  支持跨三可用区部署

  支持跨3AZ部署，可用性更高。

- 04月

  04-18

  04-18

  已发布

  支持事件中心

  事件中心将 TDMQ RabbitMQ 版所生成的事件数据进行统一管理、存储、分析和展示，方便您查看和分析。

- 04月

  04-18

  04-18

  已发布

  创建队列支持参数细化

  创建队列时支持设置节点、持久化等参数。

- 04月

  04-18

  04-18

  已发布

  支持 Quorum 队列

  Quorum 队列提供队列复制的能力，保障数据的高可用和安全性。使用 Quorum 队列可以在 RabbitMQ 节点间进行队列数据的复制，从而达到在一个节点宕机时，队列仍然可以提供服务的效果。

- 04月

  04-18

  04-18

  已发布

  支持3.11.8版本

  兼容开源3.11.8版本 RabbitMQ。

- 09月

  09-26

  09-26

  已发布

  公网带宽支持升配

  支持在3Mbps的免费额度的基础上升配公网带宽，包年包月付费。暂不支持单独退订和降配。

- 09月

  09-26

  09-26

  已发布

  在开启内网访问地址时支持指定 IP

  在开启内网访问地址时支持指定 IP。保持控制台客户端接入的 VPC 中 amqp 地址和 web 控制台的地址相同

- 09月

  09-26

  09-26

  已发布

  支持集群智能巡检

  主动排查集群问题和隐患，并基于专家经验沉淀给出问题解决方案，自动归纳健康检查结果生成报告。智能巡检能力能够为用户提取关键信息、高效定位问题、提供专业解决建议，实现运维体验闭环。

- 09月

  09-26

  09-26

  已发布

  overflow behavior 取消默认值

  创建 queue 时，overflow behavior 为非必填项，且无默认值

- 11月

  11-25

  11-25

  已发布

  公网带宽支持降配

  支持降配公网带宽

- 11月

  11-25

  11-25

  已发布

  公网带宽支持查看监控

  支持查看公网带宽使用情况监控

- 11月

  11-25

  11-25

  已发布

  支持插件管理

  在插件管理页面查看集群默认开启的插件

2024

- 01月

  01-29

  01-29

  已发布

  元数据迁移上云产品化

  迁移上云功能支持导入集群元数据，方便用户进行集群迁移。

- 01月

  01-29

  01-29

  已发布

  集群监控展示推荐 TPS 峰值

  集群监控展示推荐 TPS 峰值，协助用户判断集群使用情况

- 01月

  01-29

  01-29

  已发布

  默认开启镜像队列

  购买页选择多节点时，默认开启镜像队列。部分节点宕机时队列内数据不会丢失，保证可用性。

- 03月

  03-14

  03-14

  已发布

  Vhost和用户命名取消“.”字符限制

  Vhost和用户命名取消“.”字符限制

- 03月

  03-14

  03-14

  已发布

  新增开区地域

  新增重庆地域

- 03月

  03-14

  03-14

  已发布

  集群列表支持通过“路由IP地址”搜索集群实例

  集群列表支持通过“路由IP地址”搜索集群实例

- 03月

  03-14

  03-14

  已发布

  支持节点异常告警

  支持节点异常告警

- 03月

  03-14

  03-14

  已发布

  新增集群监控指标“打开的Channel总数”

  新增集群监控指标“打开的Channel总数”

- 04月

  04-26

  04-26

  已发布

  新建Vhost可开启镜像队列

  将默认选择开启，用户也可以取消勾选开启

- 04月

  04-26

  04-26

  已发布

  迁移上云任务支持按时间排序

  迁移上云任务支持按时间排序

- 04月

  04-26

  04-26

  已发布

  新建Quorum类型队列时添加策略和新高级配置参数

  新增死信策略，新增高级配置参数：Delivery limit, Initial cluster size, Leader locator

- 04月

  04-26

  2024-04-26

  已发布

  RabbitMQ 新建Vhost 时支持开启镜像队列，提升集群的可靠性和容错能力

  消息队列 RabbitMQ 版（TDMQ for RabbitMQ，简称 TDMQ RabbitMQ 版）是一款分布式高可用的消息队列服务，支持AMQP 0-9-1 协议，完全兼容开源 RabbitMQ 的各个组件与概念，同时具备计算存储分离，灵活扩缩容的底层优势。

- 05月

  05-23

  05-23

  已发布

  RabbitMQ 云控制台从 TDMQ 中拆分

  RabbitMQ 控制台菜单单独作为一级产品展示，增加概览页、资源独立管理页（Vhost、Exchange、Queue）、监控大盘独立管理页。

- 05月

  05-23

  05-23

  已发布

  智能巡检增加镜像队列、持久化指标

  智能巡检增加针对 Vhost 镜像队列、Exchange 持久化、Queue 持久化的智能巡检指标

- 05月

  05-23

  05-23

  已发布

  优化插件页面为列表展示

  在集群详情页顶部，选择插件管理页签，可进入插件管理列表。

- 05月

  05-23

  05-23

  已发布

  购买页价格展示集群、存储等计费详情

  购买页价格展示集群、存储等计费详情

- 05月

  05-23

  05-23

  已发布

  Exchange、Queue 管理页面增加 Features 属性

  Exchange、Queue 管理页面增加 Features 属性

- 05月

  05-23

  05-23

  已发布

  监控新增延迟消息数量指标

  在集群 和 Exchange 维度的监控新增延时消息数量指标，并支持配置告警。

- 08月

  08-20

  08-20

  已发布

  提供默认告警模板

  为用户提供默认告警模板，便于用户快速有效配置重要告警项。对于新增集群，会自动配置默认告警策略。

- 08月

  08-20

  08-20

  已发布

  支持按量计费模式

  新增售卖形态：按量计费，采用后付费模式，按资源使用量计算费用

- 08月

  08-20

  08-20

  已发布

  包年包月与按量计费相互转换

  两种计费模式之间可以相互转换，用户可以按需选择

- 08月

  08-20

  08-20

  已发布

  支持创建自定义策略

  用户可以选择创建镜像策略还是自定义创建策略，自定义策略提供字段快捷选项。

- 08月

  08-20

  2024-08-20

  已发布

  RabbitMQ 购买页支持公网开通能力

  消息队列 RabbitMQ 版（TDMQ for RabbitMQ，简称 TDMQ RabbitMQ 版）是一款分布式高可用的消息队列服务，支持AMQP 0-9-1 协议，完全兼容开源 RabbitMQ 的各个组件与概念，同时具备计算存储分离，灵活扩缩容的底层优势。

- 09月

  09-30

  2024-09-30

  已发布

  RabbitMQ 新增对曼谷一区、孟买地域的支持

  消息队列 RabbitMQ 版（TDMQ for RabbitMQ，简称 TDMQ RabbitMQ 版）是一款分布式高可用的消息队列服务，支持AMQP 0-9-1 协议，完全兼容开源 RabbitMQ 的各个组件与概念，同时具备计算存储分离，灵活扩缩容的底层优势。

- 12月

  12-09

  2024-12-09

  已发布

  消息队列 RabbitMQ 版新增路由绑定关系相关的云 API

  消息队列 RabbitMQ 版（TDMQ for RabbitMQ，简称 TDMQ RabbitMQ 版）是一款分布式高可用的消息队列服务，支持AMQP 0-9-1 协议，完全兼容开源 RabbitMQ 的各个组件与概念，同时具备计算存储分离，灵活扩缩容的底层优势。

- 12月

  12-09

  2024-12-09

  已发布

  消息队列 RabbitMQ 版新增队列相关的云 API

  消息队列 RabbitMQ 版（TDMQ for RabbitMQ，简称 TDMQ RabbitMQ 版）是一款分布式高可用的消息队列服务，支持AMQP 0-9-1 协议，完全兼容开源 RabbitMQ 的各个组件与概念，同时具备计算存储分离，灵活扩缩容的底层优势。

2025

- 06月

  06-24

  2025-06-24

  已发布

  开源托管版集群支持内网流量监控指标

  TDMQ RabbitMQ 版是一款腾讯自主研发的消息队列服务，支持 AMQP 0-9-1 协议，完全兼容开源 RabbitMQ 的各个组件与概念，同时具备计算存储分离，灵活扩缩容的底层优势。

  查看监控
- 06月

  06-24

  2025-06-24

  已发布

  TDMQ RabbitMQ Serverless 版本正式上线

  TDMQ RabbitMQ 版是一款分布式高可用的消息队列服务，支持AMQP 0-9-1 协议，完全兼容开源 RabbitMQ 的各个组件与概念。

  Serverless 版介绍
- 06月

  06-24

  2025-06-24

  已发布

  开源托管版集群支持防误删能力

  TDMQ RabbitMQ 版是一款腾讯自主研发的消息队列服务，支持 AMQP 0-9-1 协议，完全兼容开源 RabbitMQ 的各个组件与概念，同时具备计算存储分离，灵活扩缩容的底层优势。

  销毁集群
- 07月

  07-14

  2025-07-14

  已发布

  开源托管版新增支持 3.13 镜像版本

  消息队列 TDMQ RabbitMQ 版是一款腾讯自主研发的消息队列服务，支持 AMQP 0-9-1 协议，完全兼容开源 RabbitMQ 的各个组件与概念，同时具备计算存储分离，灵活扩缩容的底层优势。

  创建集群
- 10月

  10-10

  2025-10-10

  已发布

  Serverless 版支持消息轨迹能力

  消息队列 RabbitMQ 版（TDMQ for RabbitMQ，简称 TDMQ RabbitMQ 版）是一款腾讯自主研发的消息队列服务，支持 AMQP 0-9-1 协议，完全兼容开源 RabbitMQ 的各个组件与概念，同时具备计算存储分离，灵活扩缩容的底层优势。

  查询消息
- 10月

  10-10

  2025-10-10

  已发布

  Serverless 版支持公网

  消息队列 RabbitMQ 版（TDMQ for RabbitMQ，简称 TDMQ RabbitMQ 版）是一款腾讯自主研发的消息队列服务，支持 AMQP 0-9-1 协议，完全兼容开源 RabbitMQ 的各个组件与概念，同时具备计算存储分离，灵活扩缩容的底层优势。

  配置公网访问

2026

- 01月

  01-13

  01-13

  已发布

  消息队列 TDMQ RabbitMQ 托管版上海自动驾驶专区，4核16G、8核32G节点规格涨价，涨价幅度33.3%

  消息队列 TDMQ RabbitMQ 托管版上海自动驾驶专区，4核16G、8核32G节点规格涨价，涨价幅度33.3%

- 02月06日

  02-06

[### 产品简介

查看 TDMQ RabbitMQ 版的基本能力介绍和应用场景。](https://cloud.tencent.com/document/product/1495/61820)

[### 新手指引

帮助您快速了解、创建并使用 TDMQ RabbitMQ 版服务。](https://cloud.tencent.com/document/product/1495/81854)

[### 计费说明

介绍 TDMQ RabbitMQ 版专享集群的计费方式、计费组成等信息。](https://cloud.tencent.com/document/product/1495/61827)

[### 产品优势

介绍 TDMQ RabbitMQ 版具备的能力优势。](https://cloud.tencent.com/document/product/1495/61821)

### 如何使用 TDMQ RabbitMQ 版？

您可以参考 [快速入门](https://cloud.tencent.com/document/product/1495/81854) 和 [操作指南](https://cloud.tencent.com/document/product/1495/81857)，快速上手并使用 TDMQ RabbitMQ 版。

### TDMQ RabbitMQ 版有哪些应用场景？

### TDMQ RabbitMQ 版如何计费？

更多问题请查看 [常见问题](https://cloud.tencent.com/document/product/1495/61841)，也可在 [问答社区](https://cloud.tencent.com/developer/ask) 中进行提问 。

按照我们的[入门指南](https://console.cloud.tencent.com/trabbitmq)，只需点几次鼠标，即可创建您的首个腾讯云 TDMQ RabbitMQ 版集群。

