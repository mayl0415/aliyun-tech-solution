---
title: "消息队列 Pulsar 版"
url: https://cloud.tencent.com/product/tpulsar
category: "容器与中间件"
crawled_at: 2026-02-06T17:20:53.430842
---

# 消息队列 Pulsar 版

消息队列 Pulsar 版（TDMQ for Apache Pulsar，简称 TDMQ Pulsar 版）是基于 Apache Pulsar 自研的消息中间件，具备极好的云原生和 Serverless 特性，计算存储分离的架构使其在扩缩容方面具备良好的底层优势。目前已应用在腾讯计费绝大部分场景，包括支付主路径、实时对账、实时监控、大数据实时分析等方面。

- [弹性存储能力上线

  产品公告

  提供「固定并发规模 + 弹性存储」的形态，保证技术架构稳定领先的模式下，也可为用户减少存储成本。

  立即前往](https://cloud.tencent.com/document/product/1179/83699)
- [支持外部 Prometheus 接入

  产品公告

  支持将专业集群的监控数据，接入自建的 Prometheus ，使得线上运维更加自动化。

  立即前往](https://cloud.tencent.com/document/product/1179/104661)
- [专业集群支持跨地域容灾

  产品公告

  当发生地域级灾难时，客户能够快速迁移业务，确保业务的连续性。

  立即前往](https://cloud.tencent.com/document/product/1179/102697)

腾讯计费平台核心技术组件之一

提供洪峰抗压以及高可用强一致性的能力

30亿+

每日支撑30亿+消息

80+

每日服务80+渠道

300+

每日支撑300+业务

99.9%+

SLA 不低于99.9%

### 数据强一致

TDMQ Pulsar 版采用 BookKeeper 一致性协议实现数据强一致性，将消息数据备份写到不同物理机上，并且同步刷盘。当某台物理机出故障时，后台数据复制机制能够对数据快速迁移，保证用户数据备份可用。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/7Y0PTlscoQJp-dvFlriWt.png)

### 高性能低延迟

TDMQ Pulsar 版能够高效支持百万级消息生产消费以及海量消息堆积，单集群 QPS 超过10万，同时在时耗方面有保护机制来保证低延迟，帮助您轻松满足业务性能需求。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/6qBm-K0Nuun37B3srwiZV.png)

### 百万级 Topic

TDMQ Pulsar 版计算与存储架构的分离设计，使得 TDMQ Pulsar 版可以轻松支持百万级消息主题。相比于市场上其他 MQ 产品，整个集群不会因为 Topic 数量增加而导致性能急剧下降。

### 丰富的消息类型

TDMQ Pulsar 版提供丰富的消息类型，涵盖普通消息、顺序消息（全局顺序 / 分区顺序）、分布式事务消息、定时消息，满足各种严苛场景下的高级特性需求。

### 消费者数量无限制

TDMQ Pulsar 版的消费者数量不受限于 Topic 的分区个数，并且会按照一定的算法均衡每个消费者的消息量，业务可按需启动对应的消费者数量。

### 隔离控制

提供按租户对 Topic 进行隔离的机制，同时可精确管控各个租户的生产和消费速率，保证租户之间互不影响，消息的处理不会出现资源竞争的现象。

Apache Pulsar

消息队列 Pulsar 版

依赖组件多，运维量大；无 SLA 保障；安全防护能力有限；无法精准掌握配置造成资源浪费

支持按量计费，无需关心配置；免运维，无需关心底层组件；支持通过云 API HTTP 协议收发消息；高 SLA 保障，针对性参数调优

成本

成本

自建无法弹性使用，资源利用率低；自建需一定的人力维护，运维成本高

成本

按量使用，弹性计费成本可控，无需运维专项人力

可扩展性

可扩展性

Broker 节点的扩展较为灵活，但 BookKeeper 集群的扩展手动操作较为复杂，容易误操作影响数据

可扩展性

非常灵活，易于扩展，客户无需关注扩缩容过程，可以充分利用规模效应应对突发的高负载

可用性

可用性

需要自行异地部署保障可用性，需自行设计大流量负载下的集群可用性方案

可用性

多个可用区地域均为跨区部署，消息三副本异地存储，承诺可用性在99.95%以上，提供集群限流优化，防止集群被大流量击垮

安全

安全

需要安装配置开源插件

安全

利用腾讯云安全产品，天然支持

监控告警

监控告警

需要安装配置开源插件

监控告警

利用腾讯云监控告警产品，天然支持

展开

- 异步解耦
- 削峰填谷
- 顺序收发
- 数据同步

如果有多个数据中心存在，需要在多个数据中心之间消费，那么 TDMQ Pulsar 版可以非常方便实现数据中心之间的同步。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/l8AeopOPKCI9vQN2cCTwc.svg)

### 相关云产品

[消息队列 CKafka 版](https://cloud.tencent.com/product/ckafka)

[消息队列 RocketMQ 版](https://cloud.tencent.com/product/trocket)

[![](https://qcloudimg.tencent-cloud.cn/image/product/2778/32_32/blue.svg)

消息队列 RabbitMQ 版](https://cloud.tencent.com/product/trabbit)

[![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/TeDhqcn6LaCQ4YFBV3Wfr.png)

得益于 TDMQ Pulsar 版高吞吐、低延迟的能力，FiT金融产品业务迁移到TDMQ Pulsar后，消息从生产者到消费者的耗时缩短了大约80%，消息积压情况大大缓解，积压数量减少了70%。](https://cloud.tencent.com/developer/article/2409523)

[![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/e_lMfT7ALQ-I8wpXd1hy5.jpeg)

王者荣耀利用 TDMQ Pulsar 版的 TAG 消息标签过滤能力，减少了业务侧过滤消息的压力；支持按照命名空间维度配置消息生产、消费速率，避免引入分布式限流组件。TDMQ Pulsar 版帮助王者荣耀减少了业务的复杂度，降低了运维成本，并具备灵活的弹性伸缩能力。](https://cloud.tencent.com/developer/article/2422922)

[得益于 TDMQ Pulsar 版高吞吐、低延迟的能力，FiT金融产品业务迁移到TDMQ Pulsar后，消息从生产者到消费者的耗时缩短了大约80%，消息积压情况大大缓解，积压数量减少了70%。](https://cloud.tencent.com/developer/article/2409523)

[王者荣耀利用 TDMQ Pulsar 版的 TAG 消息标签过滤能力，减少了业务侧过滤消息的压力；支持按照命名空间维度配置消息生产、消费速率，避免引入分布式限流组件。TDMQ Pulsar 版帮助王者荣耀减少了业务的复杂度，降低了运维成本，并具备灵活的弹性伸缩能力。](https://cloud.tencent.com/developer/article/2422922)

[得益于 TDMQ Pulsar 版高吞吐、低延迟的能力，FiT金融产品业务迁移到TDMQ Pulsar后，消息从生产者到消费者的耗时缩短了大约80%，消息积压情况大大缓解，积压数量减少了70%。](https://cloud.tencent.com/developer/article/2409523)

[王者荣耀利用 TDMQ Pulsar 版的 TAG 消息标签过滤能力，减少了业务侧过滤消息的压力；支持按照命名空间维度配置消息生产、消费速率，避免引入分布式限流组件。TDMQ Pulsar 版帮助王者荣耀减少了业务的复杂度，降低了运维成本，并具备灵活的弹性伸缩能力。](https://cloud.tencent.com/developer/article/2422922)

上一页

下一页

2023

- 09月

  09-05

  09-05

  已发布

  硅谷开区

  专业版硅谷开区

- 09月

  09-22

  09-22

  已发布

  支持同地域跨账号集群迁移

  支持同地域跨账号集群迁移
  1、不同账号；
  2、虚拟集群迁移到专业集群。

- 11月

  11-03

  11-03

  已发布

  专业版雅加达开区

  专业版雅加达开区

- 11月

  11-27

  11-27

  已发布

  Pulsar 接入控制台全局资源搜索

  Pulsar 接入控制台全局资源搜索，便捷用户快速定位到集群实例

2024

- 01月

  01-15

  01-15

  已发布

  跨地域冷备方案

  Pulsar 支持跨地域冷备方案，提供无需业务改造的接入点快速切换能力。

- 01月

  01-20

  01-20

  已发布

  专线接入支持自定义一级域名

  专线接入场景，支持自定义一级域名，通过用户的自有域名实现对集群的访问。

- 01月

  01-31

  01-31

  已发布

  上海自动驾驶区开区

  Pulsar 专业集群上海自动驾驶专区开区

- 03月

  03-29

  03-29

  已发布

  支持外部 Prometheus 接入

  支持将专业集群的监控数据，接入自建的 Prometheus ，利于用户观测的同时，可以通过监控数据对业务 Workload HPA，使得线上运维更加自动化。

- 03月

  03-29

  03-29

  已发布

  专业集群-弹性存储上线

  专业集群提供「固定并发规模 + 弹性存储」的形态，保证技术架构稳定领先的模式下，也可为用户减少存储成本。

- 08月

  08-20

  2024-08-20

  已发布

  消息过滤支持 SQL 92 语法

  消息队列 Pulsar 版（TDMQ for Apache Pulsar，简称 TDMQ Pulsar 版）是一款基于 Apache Pulsar 自研的消息中间件，具备极好的云原生和 Serverless 特性，兼容 Pulsar 的各个组件与概念，具备计算存储分离，灵活扩缩容的底层优势。

- 08月

  08-27

  2024-08-27

  已发布

  跨地域复制

  消息队列 Pulsar 版（TDMQ for Apache Pulsar，简称 TDMQ Pulsar 版）是一款基于 Apache Pulsar 自研的消息中间件，具备极好的云原生和 Serverless 特性，兼容 Pulsar 的各个组件与概念，具备计算存储分离，灵活扩缩容的底层优势。

- 08月

  08-31

  08-31

  已发布

  消息过滤支持 SQL 92 的过滤语法

  消息过滤支持更加灵活的 SQL 92 的过滤语法

- 08月

  08-31

  08-31

  已发布

  专业集群支持 跨地域消息复制

  TDMQ Pulsar 版专业集群支持消息、元数据两级跨地域复制功能，消息级复制解决用户全球地域的数据统一归档问题，元数据级复制提供解决用户核心业务跨地域容灾的场景。

- 11月

  11-20

  2024-11-20

  已发布

  Pulsar 专业版高规格集群最大支持 128 分区

  消息队列 Pulsar 版（TDMQ for Apache Pulsar，简称 TDMQ Pulsar 版）是一款基于 Apache Pulsar 自研的消息中间件，具备极好的云原生和 Serverless 特性，兼容 Pulsar 的各个组件与概念，具备计算存储分离，灵活扩缩容的底层优势。

- 12月

  12-09

  2024-12-09

  已发布

  消息队列 Pulsar 版专业集群支持创建公网接入点

  消息队列 Pulsar 版（TDMQ for Apache Pulsar，简称 TDMQ Pulsar 版）是一款基于 Apache Pulsar 自研的消息中间件，具备极好的云原生和 Serverless 特性，兼容 Pulsar 的各个组件与概念，具备计算存储分离，灵活扩缩容的底层优势。

2025

- 01月

  01-23

  2025-01-23

  已发布

  消息队列 Pulsar 版专业集群支持自动创建 Topic

  消息队列 Pulsar 版（TDMQ for Apache Pulsar，简称 TDMQ Pulsar 版）是一款基于 Apache Pulsar 自研的消息中间件，具备极好的云原生和 Serverless 特性，兼容 Pulsar 的各个组件与概念，具备计算存储分离，灵活扩缩容的底层优势。

- 06月

  06-24

  2025-06-24

  已发布

  增加生产者、消费者已使用配额百分比指标

  TDMQ Pulsar 版是一款基于 Apache Pulsar 自研的消息中间件，具备极好的云原生和 Serverless 特性，兼容 Pulsar 的各个组件与概念，具备计算存储分离，灵活扩缩容的底层优势。

  查看监控
- 06月

  06-24

  2025-06-24

  已发布

  支持自定义租户名，便于用户迁移上云

  TDMQ Pulsar 版是一款基于 Apache Pulsar 自研的消息中间件，具备极好的云原生和 Serverless 特性，兼容 Pulsar 的各个组件与概念，具备计算存储分离，灵活扩缩容的底层优势。

  新建集群
- 06月

  06-24

  2025-06-24

  已发布

  支持虚拟集群平滑迁移专业集群

  TDMQ Pulsar 版是一款基于 Apache Pulsar 自研的消息中间件，具备极好的云原生和 Serverless 特性，兼容 Pulsar 的各个组件与概念，具备计算存储分离，灵活扩缩容的底层优势。

  集群迁移能力说明
- 10月

  10-10

  2025-10-10

  已发布

  支持降配

  消息队列 Pulsar 版（TDMQ for Apache Pulsar，简称 TDMQ Pulsar 版）是一款基于 Apache Pulsar 自研的消息中间件，具备极好的云原生和 Serverless 特性，兼容 Pulsar 的各个组件与概念，具备计算存储分离，灵活扩缩容的底层优势。

  变更集群规格
- 11月

  11-06

  2025-11-06

  已发布

  专业集群新增支持3.0.0版本

  消息队列 Pulsar 版（TDMQ for Apache Pulsar，简称 TDMQ Pulsar 版）是一款基于 Apache Pulsar 自研的消息中间件，具备极好的云原生和 Serverless 特性，兼容 Pulsar 的各个组件与概念，具备计算存储分离，灵活扩缩容的底层优势。

  集群版本更新记录

2026

- 02月06日

  02-06

[### 产品简介

查看 TDMQ Pulsar 版的基本能力介绍和应用场景。](https://cloud.tencent.com/document/product/1179/44778)

[### 新手指引

帮助您快速了解、创建并使用 TDMQ Pulsar 版服务。](https://cloud.tencent.com/document/product/1179/44814)

[### 计费说明

2021年12月1日起，TDMQ Pulsar 版将结束免费公测，正式开始计费，公测用户额外享有1个月免费期。](https://cloud.tencent.com/document/product/1179/44792)

[### 产品优势

介绍 TDMQ Pulsar 版具备的能力优势。](https://cloud.tencent.com/document/product/1179/44779)

### 如何使用 TDMQ Pulsar 版？

您可以参考 [快速入门](https://cloud.tencent.com/document/product/1179/44814) 和 [操作指南](https://cloud.tencent.com/document/product/1179/52145) 文档，快速上手并使用 TDMQ Pulsar 版。

### TDMQ Pulsar 版有哪些应用场景？

### TDMQ Pulsar 版相对于竞品有哪些优势？

### TDMQ Pulsar 版如何计费？

更多问题请查看 [常见问题](https://cloud.tencent.com/document/product/1179/44823)，也可在 [问答社区](https://cloud.tencent.com/developer/ask) 中进行提问 。

按照我们的[入门指南](https://cloud.tencent.com/document/product/1179/44814) ，只需点几次鼠标，即可创建您的首个腾讯云 TDMQ 集群和主题。

