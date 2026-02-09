---
title: "弹性公网 IP"
url: https://cloud.tencent.com/product/eip
category: "网络"
crawled_at: 2026-02-06T17:28:41.432477
---

# 弹性公网 IP

弹性公网 IP（Elastic IP，EIP）是可以独立购买和持有，且在某个地域下固定不变的公网 IP 地址，可以与 CVM、NAT 网关、弹性网卡和高可用虚拟 IP 等云资源绑定，提供访问公网和被公网访问能力；还可与云资源的生命周期解耦合，单独进行操作；同时提供多种计费模式，您可以根据业务特点灵活选择，以降低公网成本。

### 弹性灵活

弹性公网 IP 是独立的公网 IP 资源，属于您的腾讯云账户。您可随时与 CVM、NAT 网关、弹性网卡和高可用虚拟 IP 等绑定、解绑，灵活使用。此外，还可以动态调整带宽，实时生效。

### 更低成本

弹性公网 IP 提供多种计费模式，包括按流量、按小时带宽、按包月带宽计费等。您还可以将按流量和按小时带宽计费模式的 EIP 加入共享带宽包，提高带宽资源的利用率，大幅降低您的公网使用成本。

### 操作便捷

弹性公网 IP 支持控制台和云 API 两种方式使用。在控制台上，可以通过简单的可视化操作进行申请、绑定、解绑和释放等操作；同时 EIP 提供更加规范和全面 3.0 版本的 API 接口，方便您进行管理和操作。

- 提供公网访问能力
- 容灾

在多活容灾场景中，主云服务器和备用云服务器的应用和资源实时同步。主云服务器与弹性公网 IP 绑定，当主云服务器故障时，可以将弹性公网 IP 与主云服务器解绑并重新绑定到备用云服务器中，将业务使用的公网 IP 从故障的主云服务器平滑迁移到备用云服务器，无需修改 DNS 等映射关系，保证服务的连续性。

![](https://qcloudimg.tencent-cloud.cn/raw/ac40e081e7eae7042233c84f28ab6fa1.svg)

[2021-03

中国香港地域支持的专属线路，避免绕行国际运营商出口，降低网络延时。](https://cloud.tencent.com/document/product/1199/41646#.3Ca-id.3D.22ip-type.22.3Eeip-.E7.9A.84-ip-.E5.9C.B0.E5.9D.80.E7.B1.BB.E5.9E.8B.3C.2Fa.3E)

[2020-12

部分地域支持移动、联通、电信单运营商的 EIP，提供带宽价格低于常规 BGP IP 的价格。](https://cloud.tencent.com/document/product/1199/41646#eip-.E7.9A.84-ip-.E5.9C.B0.E5.9D.80.E7.B1.BB.E5.9E.8B)

[2019-04

每个 EIP 都支持添加标签，您可以使用平台通用的访问管理鉴权实现权限管理。](https://cloud.tencent.com/document/product/598)

[2018-12

您可以在 EIP 控制台找回使用过的、且暂未分配给其他用户的公网 IP。](https://cloud.tencent.com/document/product/1199/41708)

[2018-04

Anycast 公网加速是一个覆盖多地的动态加速网络，可以大幅提升您业务的公网访问体验。](https://cloud.tencent.com/document/product/644)

[2017-12

支持公网网络属性上移到公网 IP，在 IP 上实现计费、限速。](https://cloud.tencent.com/document/product/1199/49090#judge)

[2017-12

EIP 直通后，EIP 在本地可见，配置时无须每次手动加入 EIP 地址，可降低开发成本。](https://cloud.tencent.com/document/product/1199/41709)

上一页

下一页

[### 产品简介

帮助您快速了解弹性公网 IP 产品的定位、概述、优势、以及具体功能。](https://cloud.tencent.com/document/product/1199/41646)

[### 应用场景

本文为您介绍 EIP 的主要应用场景：提供公网访问能力和容灾。](https://cloud.tencent.com/document/product/1199/41647)

[### 快速入门

本文以 EIP 绑定 CVM 为例介绍 EIP 使用生命周期。](https://cloud.tencent.com/document/product/1199/42122)

[### 操作指南

弹性公网 IP（EIP）是可以独立购买和持有的公网 IP 地址资源，您可根据如下操作申请 EIP。](https://cloud.tencent.com/document/product/1199/41698)

[### 最佳实践

本文为您介绍如何将同一账户内的云服务器上的公网 IP 迁移到另一个云服务器上。](https://cloud.tencent.com/document/product/1199/43872)

[### API 文档

弹性公网 IP（EIP） 提供更加规范和全面 3.0 版本的 API 接口文档。](https://cloud.tencent.com/document/product/1199/43341)

### 定价

弹性公网 IP 的费用包括两个部分：IP 资源费用、公网网络费用。

- [计费概述](https://cloud.tencent.com/document/product/1199/41692)
- [计费组成](https://cloud.tencent.com/document/product/1199/51694)
- [公网网络计费模式](https://cloud.tencent.com/document/product/1199/51739)
- [购买方式](https://cloud.tencent.com/document/product/1199/44438)
- [调整配置费用说明](https://cloud.tencent.com/document/product/1199/48123)
- [退费说明](https://cloud.tencent.com/document/product/1199/44366)
- [欠费说明](https://cloud.tencent.com/document/product/1199/41693)

- 一般常见问题
- 计费

### 弹性公网 IP 资源费用如何收取？

弹性公网 IP（EIP）的费用根据非带宽上移和带宽上移不同类型的账户收费不同，计费周期为按小时收费，付费模式为后付费。更多定价详情请参阅 [计费说明](https://cloud.tencent.com/document/product/1199/41692)。

### 弹性公网 IP 如何停止扣费？

更多问题请查看 [常见问题](https://cloud.tencent.com/document/product/1199/41746)，也可在 [问答社区](https://cloud.tencent.com/developer/ask) 中进行提问 。

[负载均衡 CLB

负载均衡提供安全快捷的流量分发服务，访问流量经由 CLB 可以自动分配到云中的多台云服务器上，扩展系统的服务能力并消除单点故障。](https://cloud.tencent.com/product/clb)

[共享流量包 TP

共享流量包是一种预付费公网流量套餐，可自动抵扣多种产品的流量消耗。相比后付费流量，共享流量包单价更低，支持统一查看、分析、管理流量用量。](https://cloud.tencent.com/product/tp)

[NAT 网关

一种支持 IP 地址转换的网络云服务，保护私有网络信息不直接暴露公网；也可以通过 NAT 网关实现海量的公网访问，最大支持 1000 万以上的并发连接数。](https://cloud.tencent.com/product/nat)

[VPN 连接

VPN 连接（VPN Connections）是一种基于网络隧道技术，实现本地数据中心与腾讯云上资源连通的传输服务，快速构建一条安全、可靠的加密通道。](https://cloud.tencent.com/product/vpn)

按照我们的入门指南，只需点几次鼠标，即可创建您的首个腾讯云弹性公网 IP。

