---
title: "消息队列 CMQ 版"
url: https://cloud.tencent.com/product/tcmq
category: "容器与中间件"
crawled_at: 2026-02-06T17:21:06.982790
---

# 消息队列 CMQ 版

消息队列 CMQ 版（TDMQ for CMQ，简称 TDMQ CMQ 版）是一款分布式高可用的消息队列服务，它能够提供可靠的，基于消息的异步通信机制，能够将分布式部署的不同应用（或同一应用的不同组件）中的信息传递，存储在可靠有效的 CMQ 队列中，防止消息丢失。TDMQ CMQ 版支持多进程同时读写，收发互不干扰，无需各应用或组件始终处于运行状态。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/xkN161u5_x702IiF4LrAV.png)

### 高性能

高效支持亿级消息收发和推送，单集群 QPS 超过 10 万，满足您的业务之间的消息收发需求。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/tRwqWbFg47UXJqH6nBxDG.png)

### 高可用

三副本存储，当某节点出故障时，后台数据复制机制能够对数据快速迁移，可靠保证达99.999999%，业务连续可用性99.95%承诺。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/AaMTHaGCuPoimTaFkKQzO.png)

### 横向扩展

底层系统根据业务规模，自动弹性扩展消息队列的队列数量和存储容量，对上层业务无感知。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/OJnToUPnq0WqdLthkUa5_.png)

### 安全可靠

支持密钥鉴权，并基于腾讯云平台多维度的安全防护，抵御网络攻击，保护您的业务隐私。同时支持腾讯云 CAM 账号权限管理，支持基于细粒度资源访问控制权限，细化管理。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/4j9cc89VviyRWBRSa2fPq.png)

### 易用免运维

提供 API 访问接口和 java，C++ 等多种 SDK，简化开发成本，方便上云。支持多维度的监控告警功能，无须关心底层资源的运维，专注您的业务开发。

- 消息永不丢失
- 消息安全可靠
- 同城容灾

TDMQ CMQ 版支持多可用区部署。 消息 body 的存储，可根据业务特性选择同步落盘（强一致性）或异步落盘（最终一致性）的不同策略。 当主节点 MQ 数据由于不可抗力因素彻底丢失时，主备节点的 RPO 在 5min 以内。灾难恢复切换后，存在数据的差异，可关联其他 DB 做对账等处理，补回数据。 金融级的容灾方案为 Webank、财付通等核心业务保驾护航。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/kRFLHC5MAkk5EjpIf_V6c.svg)

### 相关云产品

[![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/16IZHjktUb4IvJBkDtrDW.svg)

云服务器 CVM](https://cloud.tencent.com/product/cvm)

[![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/mNvdqlF4pkRj6lrjcZMOz.svg)

云数据库 MySQL](https://cloud.tencent.com/product/cdb)

[### 产品简介

介绍 TDMQ CMQ 版的基础能力，应用场景和接入方式。](https://cloud.tencent.com/document/product/1496/60989)

[### 新手指引

帮助您快速了解，创建并使用 TDMQ CMQ 版服务。](https://cloud.tencent.com/document/product/1496/61006)

[### 计费说明

2022年5月11日起，TDMQ CMQ 版正式商业化，开始计费。](https://cloud.tencent.com/document/product/1496/72347)

[### 产品优势

介绍相比传统开源 MQ 应用，腾讯云 TDMQ CMQ 版具备的优势。](https://cloud.tencent.com/document/product/1496/60991)

### 如何使用 TDMQ CMQ 版？

您可以参考 [快速入门](https://cloud.tencent.com/document/product/1496/61006) 和 [操作指南](https://cloud.tencent.com/document/product/1496/61015)，快速上手并使用 TDMQ CMQ 版。

### TDMQ CMQ 版有哪些应用场景？

### TDMQ CMQ 版如何计费？

更多问题请查看 [常见问题](https://cloud.tencent.com/document/faq)，也可在 [问答社区](https://cloud.tencent.com/developer/ask) 中进行提问 。

按照我们的[入门指南](https://cloud.tencent.com/document/product/1496/61006) ，只需点几次鼠标，即可创建您的首个腾讯云 TDMQ CMQ 版队列和主题。

