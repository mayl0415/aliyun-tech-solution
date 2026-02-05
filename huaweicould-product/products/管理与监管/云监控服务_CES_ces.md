---
title: "什么是云监控服务？"
code: "ces"
category: "管理与监管"
source_url: "https://support.huaweicloud.com/productdesc-ces/zh-cn_topic_0015479882.html"
crawled_at: "2026-02-05T16:54:31.868269"
---

# 什么是云监控服务？

## 产品简介

提供云上及本地资源的立体化监控平台

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-ces/zh-cn_image_0000001644444449.png)

## 详细说明

# 什么是云监控服务？

云监控服务为用户提供一个针对弹性云服务器、带宽等资源的立体化监控平台。使您全面了解云上的资源使用情况、业务的运行状况，并及时收到异常告警做出反应，保证业务顺畅运行。

#### 产品架构

云监控服务作为一个监控平台，接收来自各类云服务上报的监控指标，同时也支持用户通过API接口，根据云监控服务规定的上报规范，自定义上报监控指标。

所有的监控指标存储在云监控服务的后台指标库中，当云服务资源有监控数据上报给云监控服务时，对应的云服务的监控指标会呈现在云监控服务的默认指标视图中，用户可以直观地在视图上查看资源的各种监控数据，还可以基于监控指标在业务上的重要程度配置不同级别的告警规则，当监控指标数据达到告警阈值后即可触发告警，并通过SMN消息通知服务的各种通知渠道将告警发送给用户。用户收到告警后可以及时对资源异常做出响应。

**图1** 云监控服务架构图
  
![](https://support.huaweicloud.com/productdesc-ces/zh-cn_image_0000001644444449.png "点击放大")

#### 主要功能

云监控服务主要具有以下功能：

* 自动监控：

  云监控服务不需要开通，在创建弹性云服务器等资源后监控服务会自动启动，您可以直接到云监控服务查看该资源运行状态并设置告警规则。有关自动监控的更多信息，请参阅[查看云服务监控看板](https://support.huaweicloud.com/usermanual-ces/ces_01_0234.html)。
* 主机监控：

  通过在弹性云服务器或裸金属服务器中安装云监控服务Agent插件，用户可以实时采集ECS或BMS 1分钟级粒度的监控数据。已上线CPU、内存和磁盘等40余种监控指标。有关主机监控的更多信息，请参阅[主机监控简介](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0078721772.html)。
* 灵活配置告警规则：

  对监控指标设置告警规则时，支持对多个云服务资源同时添加告警规则。告警规则创建完成后，可随时修改告警规则，支持对告警规则进行启用、停止、删除等灵活操作。有关告警规则的更多信息，请参阅[告警规则简介](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0015479880.html)。
* 实时通知：

  通过在告警规则中开启消息通知服务，当云服务的状态变化触发告警规则设置的阈值时，系统通过短信、邮件、语音通知、HTTP、HTTPS、FunctionGraph（函数）、FunctionGraph（工作流）、企业微信、钉钉、飞书或Welink等多种方式实时通知用户，让用户能够实时掌握云资源运行状态变化。有关告警通知的更多信息，请参阅[告警通知](https://support.huaweicloud.com/usermanual-ces/ces_01_0218.html)。
* 监控看板：

  为用户提供在一个监控看板跨服务、跨维度查看监控数据，将用户关注的重点服务监控指标集中呈现，既能满足您总览云服务的运行概况，又能满足排查故障时查看监控详情的需求。有关监控看板的更多信息，请参阅[我的看板简介](https://support.huaweicloud.com/usermanual-ces/ces_01_0211.html)。
* OBS转储：

  云监控服务各监控指标的原始数据的保留周期为两天，超过保留周期后原始数据将不再保存。您可以在对象存储服务（Object Storage Service，以下简称OBS）创建存储桶，然后将原始数据同步保存至OBS，以保存更长时间。有关OBS转储的配置方法，请参阅[配置数据存储](https://support.huaweicloud.com/usermanual-ces/ces_01_0065.html)。
* 资源分组：

  资源分组支持用户从业务角度集中管理其业务涉及到的弹性云服务器、云硬盘、弹性IP、带宽、数据库等资源。从而按业务来管理不同类型的资源、告警规则、告警记录，可以迅速提升运维效率。有关资源分组的更多信息，请参阅[资源分组简介](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0102570567.html)。
* 站点监控：

  站点监控用于模拟真实用户对远端服务器的访问，从而探测远端服务器的可用性、连通性等问题。有关站点监控的更多信息，请参阅[站点监控简介](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0090332134.html)。
* 事件监控：

  事件监控提供了事件类型数据上报、查询和告警的功能。方便您将业务中的各类重要事件或对云资源的操作事件收集到云监控服务，并在事件发生时进行告警。有关事件监控的更多信息，请参阅[事件监控简介](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0109974074.html)。
* 数据转储：

  当您需要通过分布式消息服务Kafka的控制台或使用开源Kafka客户端查询云服务的监控指标时，可以使用云监控服务提供的数据转储功能。数据转储可以实时将云服务监控数据转储到分布式消息服务Kafka中。有关数据转储的更多信息，请参阅[数据转储简介](https://support.huaweicloud.com/usermanual-ces/ces_01_0184.html)。
* 广域网质量监控

  广域网质量监控通过遍布全球的互联网终端探测节点，发送模拟真实用户访问的探测请求，帮助客户监控通过全国各省市运营商广域网络到客户服务站点的访问情况。有关广域网质量监控的更多信息，请参阅[广域网质量监控简介](https://support.huaweicloud.com/usermanual-ces/ces_08_0002.html)。

#### 介绍视频

由于不同版本的功能特性可能存在差异，相关视频仅供参考，具体请以实际环境为准。

[![](https://support.huaweicloud.com/productdesc-ces/zh-cn_image_0000002327017048.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/CES/1703474261584357357.mp4)

####
