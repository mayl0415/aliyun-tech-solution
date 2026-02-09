---
title: "Prometheus 监控服务"
url: https://cloud.tencent.com/product/tmp
category: "容器与中间件"
crawled_at: 2026-02-06T17:22:16.023635
---

# Prometheus 监控服务

Prometheus 监控服务（TencentCloud Managed Service for Prometheus，TMP）是基于开源 Prometheus 构建的高可用、全托管的服务，与腾讯云容器服务（TKE）高度集成，兼容开源生态丰富多样的应用组件，结合腾讯云可观测平台-告警管理和 Prometheus Alertmanager 能力，为您提供免搭建的高效运维能力，减少开发及运维成本。

- 中国内地区域
- 港澳台及其他境外区域
- 金融区域

体验版

高性价比

上海金融/北京金融

- 可选地域上海金融/北京金融
- 存储时长1个月
- 数据上报量额度10亿次/月
- 免费指标存储额度20亿次/月
- 有效期1个月

高性价比

### 轻量

与开源 Prometheus 监控服务相比，Prometheus 监控服务的整体结构更加轻量化，您创建 Prometheus 监控服务实例后，即可开始使用。Agent 仅占用1G以内内存即可完成数据抓取。

### 稳定可靠

Prometheus 监控服务仅占用 MB 级用户资源，相比开源 Prometheus，占用更低资源。同时，结合腾讯云云存储服务及自身的副本能力，可减少系统中断运行次数，为您提供可用性更强的服务。

![](https://cloudcache.tencent-cloud.com/qcloud/tcloud_dtc/static/tc_portal_icon/03aeb22c-0014-42a9-9764-a79c79b080d1.png)

### 开放

Prometheus 监控服务提供了开箱即用的 Grafana 服务，同时也集成了丰富的 Kubernetes 基础监控以及常用服务监控的 Dashboard，用户开通后即可快速使用。

### 低成本

Prometheus 监控服务提供了原生的 Prometheus 监控服务，在您购买 Prometheus 监控服务的实例之后，可以快速与腾讯云容器服务 TKE 集成，为运行在 Kubernetes 之上的服务提供监控服务，免去搭建运维及开发成本。

### 扩展性

Prometheus 监控服务的数据存储能力无上限，不受限于本地磁盘。可以结合腾讯云自研的分片和调度技术，实现动态扩缩，满足用户的弹性需求，同时支持负载均衡。解决开源 Prometheus 无法水平扩展的痛点。

### 兼容性

100%兼容 Prometheus 开源协议，支持核心 API、自定义多维数据模型、灵活的查询语言 PromQL 和通过动态服务或静态配置发现采集目标。您可以轻松迁移及接入。

- 一体化监控场景
- 应用服务监控场景
- CVM 监控场景

当您的服务部署在 CVM 上时，几乎每次服务的扩缩容都要修改 Prometheus 的抓取配置。针对这类场景，结合腾讯云平台提供的标签能力和 Prometheus Agent 对腾讯云标签的发现能力，用户只需合理的对 CVM 关联标签即可方便的管理监控目标对象， 免去了需要不断手动更新配置的维护成本，例如：

服务 A 同时部署在 2 台 CVM 上，并对其所在的 CVM 关联标签（服务名：A）；

由于需要进行业务活动，原有 CVM 数量不满足业务活动需求，需再扩容 3 台 CVM，这时只需要对这 3 台 CVM 关联标签（服务名：A）。成功关联后，Agent 就会自动发现新增的3台 CVM，主动抓取监控指标；

活动过后缩容下线 3 台 CVM，服务发现功能会自动感知服务下线，停止抓取监控指标。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/b2EmggpMA3iaHRmkNecwA.svg)

[Grafana 服务

提供安全、免运维的 Grafana 能力，内建腾讯云多种数据源插件，如 Prometheus 监控服务、日志服务、容器服务等，最终实现数据的统一可视化。](https://cloud.tencent.com/product/tcmg)

[应用性能监控

包含指标、链路、日志的一站式应用性能监控服务，开源协议平滑接入，有效加速故障排查，定位架构瓶颈。](https://cloud.tencent.com/product/apm)

[前端性能监控

可用于 Web 和小程序的前端真实体验监控服务，基于腾讯内部多年实践，一行代码、无侵接入，实现页面性能和前端质量的实时可观测。](https://cloud.tencent.com/product/rum)

[云拨测

零代码、覆盖全球全地域、以真实终端用户使用场景为视角，模拟真实用户最后一公里的可用性探测服务。](https://cloud.tencent.com/product/cat)

[云压测

是一款分布式性能测试服务，可模拟海量用户的真实业务场景，全方位验证系统可用性和稳定性。支持百万并发和多协议压测，兼容原生 JMeter。](https://cloud.tencent.com/product/pts)

[事件总线

一款安全，稳定，高效的云上事件连接器，目前已接入 100+ 云上服务，助力分布式事件驱动架构的快速构建。](https://cloud.tencent.com/product/eb)

[### 产品概述

介绍 Prometheus 监控服务的产品功能、产品优势等。](https://cloud.tencent.com/document/product/248/87371)

[### 快速入门

介绍如何快速使用 Prometheus 监控服务。](https://cloud.tencent.com/document/product/248/87643)

[### 购买指南

介绍 Prometheus 监控服务的计费模式、实例价格等。](https://cloud.tencent.com/document/product/248/87089)

[### 自定义监控

通过 Prometheus 监控服务自定上报指标监控数据，对应用或者服务内部的一些状态进行监控。](https://cloud.tencent.com/document/product/248/87379)

### 最佳实践

Prometheus 为您提供典型应用场景下的实践案例，有效协助您在更多场景下使用 Prometheus 监控服务。

- [自建的 K8S 接入 Prometheus](https://cloud.tencent.com/document/product/248/87472)
- [跨云 K8S 接入 Prometheus](https://cloud.tencent.com/document/product/248/87473)
- [自建 Prometheus 迁入](https://cloud.tencent.com/document/product/248/87468)
- [云服务器场景下自定义接入](https://cloud.tencent.com/document/product/248/87469)
- [容器场景监控](https://cloud.tencent.com/document/product/248/87470)

### Prometheus 监控服务与开源 Prometheus 有什么区别？

Prometheus 监控服务完全兼容开源生态，并与腾讯云产品监控数据打通，帮助用户快速搭建监控体系（自定义监控，组件监控，基础监控等），支持 Grafana 并预设了常用的监控 Dashboard，支持丰富的 Exporter 并预设了常见的告警模板；很好解决了开源社区 Prometheus 高可用搭建困难， Prometheus 性能可扩展性差，运维消耗人力等痛点。

### Prometheus 监控服务是否支持自定义上报数据？

### Prometheus 监控服务的监控数据是怎么采集的？

### Prometheus 监控服务支持哪些云产品？

### 一个 Exporter 数据太多了如何处理？

更多问题请查看 [常见问题](https://cloud.tencent.com/document/product/248/87463)，也可在 [问答社区](https://cloud.tencent.com/developer/ask) 中进行提问 。

### 扫码关注【腾讯云可观测】公众号，获得更多产品动态

关于任何腾讯云可观测平台的使用问题，欢迎加右侧官方客户群咨询。我们的研发团队将竭诚为您服务。

