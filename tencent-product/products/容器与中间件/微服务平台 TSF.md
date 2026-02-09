---
title: "微服务平台 TSF"
url: https://cloud.tencent.com/product/tsf
category: "容器与中间件"
crawled_at: 2026-02-06T17:21:20.648411
---

# 微服务平台 TSF

微服务平台（Tencent Service Framework，TSF）是一个围绕应用和微服务的 PaaS 平台，提供一站式应用全生命周期管理能力和服务注册配置治理，提供多维度应用和服务的监控数据，助力服务性能优化。

[产品文档](https://cloud.tencent.com/document/product/649)

### 拥抱开源社区

拥抱 Spring Cloud 和 Istio 开源社区，提供高可用、可扩展、灵活的微服务技术中台商业版支持。支持原生 Spring Cloud 应用无需修改直接接入并获得服务注册发现、服务治理、可观测性能力。支持通过 Service Mesh 模式无需修改直接接入不同语言应用。

### 应用全生命周期管理

提供从创建应用到运行应用的全生命周期管理，支持创建、部署、回滚、扩容、下线、启动和停止应用。提供虚拟机和容器两种部署方式，满足不同客户的使用需求。

### 高性能服务注册和配置中心

提供高性能注册与配置中心，支持金融级高可用架构。注册中心采用多副本数据存储与自动故障转移机制，确保服务实例毫秒级注册发现与健康状态实时同步。配置中心支持动态推送、实时生效及版本回滚，配置变更可触发回调方法实现业务逻辑无缝更新。

### 细粒度服务治理

提供服务和 API 级别的服务治理能力，支持控制台上配置服务路由、服务限流、服务鉴权等规则，实现细粒度的服务治理。

### 灵活运维

配合应用性能观测平台（APM）和腾讯云日志平台（CLS），提供应用和服务级别的日志、监控、调用链、服务依赖拓扑，满足不同纬度的运维需求。

### 跨可用区高可用

支持同城跨可用区容灾和就近路由，规避单可用区可能存在的不可抗力风险，提高服务的高可用性和容灾能力。

- [应用管理

  应用管理是一个围绕应用和微服务的 PaaS 平台，提供一站式应用全生命周期管理能力和数据化运营支持，提供多维度应用和服务的监控数据，帮助企业创建和管理云资源，助力企业充分聚焦核心业务本身。](https://cloud.tencent.com/product/msas)

  - 应用全托管
  - 极致弹性
  - 稳定性保障
  - 持续集成
- [注册配置治理

  开源增强

  TSF 注册配置治理使用开源增强的Polaris（北极星），Polaris是腾讯开源的注册中心、配置中心和治理中心，致力于解决分布式或者微服务架构中的服务可见、故障容错、流量控制和安全问题。北极星在腾讯内部的服务注册数量超过百万，日接口调用量超过十万亿，通用性和稳定性都得到了大规模的验证。](https://cloud.tencent.com/product/srag)

  - 注册发现
  - 配置管理
  - 流量控制
  - 故障容错

- 应用全生命周期管理
- 微服务架构
- 高可用和单元化

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/athw1F03FCAn2eoyJ5K6a.png)

### 简介

单元化架构通过核心数据水平拆分、应用服务的无状态设计将相同领域的业务服务划分为一个个独立部署单元，单元内业务闭环。有效解决服务的弹性伸缩、故障隔离、异地多活等微服务应用的高可用问题。
结合腾讯云单元化管理平台（Tencent Cloud Unit Architecture，简称 TCUA），用户可以实现接入层、应用层、数据层等全链路异地多活单元化。基于单元化架构，地域多活实现单元流量闭环，具备水平扩展和跨地域快速扩建能力。通过灵活的全局流量调配机制，可快速实现跨数据中心的单元灰度和分钟级容灾切换，在保证业务持续高可用的同时助力企业降本增效。
该能力当前仅在私有化场景售卖。

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

[2021-07-14

容器部署应用场景支持 service 可选能力，节约集群内 IP 资源。](https://cloud.tencent.com/document/product/649/15525)

[2021-07-14

优先保留 yaml 模板中设置的调度策略，如果未设置则按照集群资源调度，可能调度到某一可用区。](https://cloud.tencent.com/document/product/649/15525)

[2021-07-14

1.22版本后依赖 TSF Spring Cloud SDK 开发的普通应用与微服务网关应用支持上报 SDK 版本。](https://cloud.tencent.com/document/product/649/55599)

[2021-06-18

优化排障路径，支持服务检索和统计等能力，增强排障的易用性和便捷性。](https://cloud.tencent.com/document/product/649/45975)

[2021-06-18

从1.32版本 SDK 开始，TSF 微服务网关 SDK 支持兼容使用开源网关功能。](https://cloud.tencent.com/document/product/649/57430)

[2021-06-18

服务监听允许程序监听特定服务的上下线情况，从而触发对应业务逻辑。](https://cloud.tencent.com/document/product/649/57431)

[2021-05-20

新计费模式用户支持在控制台上直接调整规格降低节点数量。](https://cloud.tencent.com/document/product/649/55652)

[2021-05-20

强化 TSF 监控下钻能力，支持从命名空间到服到部署组、节点、接口级别的逐步下钻。](https://cloud.tencent.com/document/product/649/15544)

[2021-05-20

支持全链路灰度发布的泳道中部署组的监控能力。](https://cloud.tencent.com/document/product/649/43465)

[2021-05-20

优化接口监控能力，添加服务监控指标同环比。](https://cloud.tencent.com/document/product/649/45975)

[2021-04-27

支持单元化部署架构的网关监控能力。](https://cloud.tencent.com/document/product/649/55289)

[2021-04-27

支持查看容器集群创建和部署组发布事件，方便用户进行异常定位。](https://cloud.tencent.com/document/product/649/13684)

上一页

下一页

[### 产品简介

帮助您快速了解腾讯云微服务平台产品的定位、概述、优势、以及具体功能。](https://cloud.tencent.com/document/product/649/13005)

[### 新手指引

帮助您快速了解、创建并登录腾讯云微服务平台。](https://cloud.tencent.com/document/product/649/45359)

[### 快速入门

本文为您介绍 TSF 资源管理的重要概念和入门使用 TSF 的基础流程。](https://cloud.tencent.com/document/product/649/55491)

[### 开发指南

该章节包含了您在开发过程中常用的的通用操作内容。](https://cloud.tencent.com/document/product/649/55488)

[### 最佳实践

当用户需要上线新的功能时，希望使用灰度发布的手段在小范围内进行新版本发布测试。](https://cloud.tencent.com/document/product/649/33916)

[### 视频专区

为广大用户提供了多种类型的视频教程，为服务开发者提供了专业的云技术学习平台。](https://cloud.tencent.com/document/product/649/42878)

### 定价

腾讯微服务平台 TSF 于2020年10月12日晚21点进行计费方式的优化。相比原有计费模式，新的计费模式支持更加灵活，价格更加优惠，降价幅度最多可达75%。

- [购买指南](https://cloud.tencent.com/document/product/649/30023)
- [计费概述](https://cloud.tencent.com/document/product/649/48614)
- [购买方式](https://cloud.tencent.com/document/product/649/44393)
- [续费与调整规格说明](https://cloud.tencent.com/document/product/649/55652)
- [退费说明](https://cloud.tencent.com/document/product/649/44394)
- [资源回收说明]( https://cloud.tencent.com/document/product/649/44395)
- [计费模式迁移说明](https://cloud.tencent.com/document/product/649/49039)

- 一般常见问题
- 应用管理问题
- 子账号协作者使用问题

### 协作者身份使用 TSF 报 4102 无权限错误？

协作者在使用微服务平台 TSF 前，需要主账号将协作者与 tsf\_PassRole 策略关联，具体操作请参考 [协作者和子账号使用微服务平台 TSF](https://cloud.tencent.com/document/product/649/16869)。

### 创建策略时出现 resouce 字段格式错误如何解决?

更多问题请查看 [常见问题](https://cloud.tencent.com/document/product/649/43058)，也可在 [问答社区](https://cloud.tencent.com/developer/ask) 中进行提问 。

按照我们入门指南 ，只需点几次鼠标，即可部署您的第一个微服务。

