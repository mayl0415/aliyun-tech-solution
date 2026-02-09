---
title: "Anycast 公网加速 AIA"
url: https://cloud.tencent.com/product/aia
category: "网络"
crawled_at: 2026-02-06T17:28:13.878366
---

# Anycast 公网加速 AIA

Anycast 公网加速（Anycast Internet Acceleration，AIA）是一个覆盖多地的动态加速网络，可以大幅提升您业务的公网访问体验。不同于其他应用层加速服务，AIA 能实现 IP 传输的质量优化和多入口就近接入，减少网络传输的抖动、丢包，最终提升云上应用的服务质量，扩大服务范围，精简后端部署。

[立即申请](https://cloud.tencent.com/apply/p/cs6f207516u)[产品文档](https://cloud.tencent.com/document/product/644)

![](https://qcloudimg.tencent-cloud.cn/raw/c23683d3f2659e660f7594c0761ba455.png)

### 低时延

AIA 用 Anycast 的方式同时把 IP 发布到多个地域，请求包根据传输协议会到达最优的 IP 发布地域，优先进入腾讯云，然后走腾讯云的内网专线到达主机，避开公网的拥堵，达到减少时延的效果。

### 高可靠

公网传输是不可靠的传输，而运营商线路中断导致的不可访问，一般用户只能等待恢复。使用 AIA 后，腾讯云内网、运营商网络、腾讯云 POP 点实现网络多路径和多入口，屏蔽单地域和单线路的故障，提高网络稳定性。

### 降低抖动

公网传输性能不稳定，跨地域访问过程中可能会遇到网络抖动的情况，进而影响服务体验，使用AIA后， 网络请求将就近接入腾讯云的内网专线进行跨地域传输，降低公网抖动给您带来的影响，提升跨地域网络传输的稳定性。

### 简化部署

客户分散在多地又需要就近接入的服务，需要IP不同的多个地域部署机器、配置 DNS 实现负载均衡，十分繁琐。使用 AIA 后，无需每个地域都配置 IP，后端维护一套逻辑即可，各地域请求直接用专线加速到后端机器。

### 全局负载均衡

用 Anycast 的方式同时把 IP 发布到多个地域，请求包根据传输协议会到达最优的 IP 发布地域（通常是最近的地域），这实现了全局的负载均衡；当发生流量型攻击时，由于IP多地发布，也实现了流量分摊的效果。

![](https://qcloudimg.tencent-cloud.cn/raw/ba5d346953b00745ea4deb6ad3e0a2c6.png)

### 易于使用

AIA 兼容常见的 IP 操作，购买一个加速型弹性公网 IP 即可，使用门槛低。支持自助设置外网带宽限速，方便根据成本或主机处理速度设置合适的带宽上限。支持流量监控，用于回溯和分析。支持绑定和解绑，方便后端资源变更。

- 游戏加速
- 视频直播互动
- 金融服务
- 安全服务

安全清洗服务提供商、游戏、大型网站应用经常面临 Syn Flood、ICMP Flood 等各种大流量攻击。普通公网 IP 在单个地域发布，所有攻击流量都集中在一个出入口。使用 AIA 后，IP 在多地同时发布，无需改动 DNS 配置，攻击流量被导流到各个入口就近消化。

![](https://qcloudimg.tencent-cloud.cn/raw/196e118306a97fcc0e08239a237566ff.svg)

[### 产品简介

本文为您提供 Anycast 公网加速的概念、低时延等优势说明。](https://cloud.tencent.com/document/product/644/12612)

[### 快速入门

本文以标准账户类型为例，引导您快速上手 Anycast 公网加速。](https://cloud.tencent.com/document/product/644/12631)

[### 购买指南

本文为您提供 Anycast 公网加速的价格、计费示例说明。](https://cloud.tencent.com/document/product/644/12617)

- 一般常见问题
- 计费

### 加速流量如何计费?

加速流量是 Anycast 弹性公网 IP（Anycast EIP）产生的流量，一个账户下的总加速流量曲线按95方式消峰后，即为结算带宽。

### 加速流量按出方向计费还是按入方向计费？

### Anycast 弹性公网IP（Anycast EIP）是否支持按流量计费？

更多问题请查看 [常见问题](https://cloud.tencent.com/document/product/644/12628)，也可在 [问答社区](https://cloud.tencent.com/developer/ask) 中进行提问 。

按照我们的入门指南 ，只需点几次鼠标，即可创建您的首个 Anycast 公网加速服务。

