---
title: "NAT 网关"
url: https://cloud.tencent.com/product/nat
category: "网络"
crawled_at: 2026-02-06T17:28:00.501118
---

# NAT 网关

NAT 网关（NAT Gateway）提供 IP 地址转换服务，为腾讯云内资源提供高性能的 Internet 访问服务。通过 NAT 网关，在腾讯云上的资源可以更安全的访问 Internet，保护私有网络信息不直接暴露公网；您也可以通过 NAT 网关实现海量的公网访问，最大支持1000万以上的并发连接数；NAT 网关还支持 IP 级流量管控，可实时查看流量数据，帮助您快速定位异常流量，排查网络故障。

### 海量并发

NAT 网关支持海量并发，最大可支持1000万的并发连接数，有效应对海量的公网访问，如视频服务、物联网、大数据分析等场景，满足您对公网的海量访问需求。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/0Qp91pPmUDJD7G_m-7-hO.png)

### 高性能访问

对 Internet 访问频率高、带宽需求大的业务，NAT 网关可以支持5Gbps以上的转发能力，并且可同时绑定10个弹性 IP，轻松应对峰值流量、为大规模公网应用提供支撑。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/PlCtSx5aNl6YOm8cnrgVD.png)

### 可视化管理

NAT 网关支持流量管控功能，通过图表直观展现网关性能状态，通过多维度监控、对故障设定预警，帮助您及时定位和解决问题。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/i5wUmw2J2nC3Q_nr-8vwp.png)

### 稳定高可用

腾讯云 NAT 网关底层通过双机热备、自动容灾等高可靠设计，将服务可用性提升至高达99.99% ，为您业务稳定运行保驾护航。

### 成本更优

基于不同业务需求，腾讯云提供多种规格的 NAT 网关，您可根据业务的需求选择相应的服务，同时 NAT 网关支持共享带宽包，灵活搭配帮您降低业务成本。

### 服务集成

NAT 网关支持与腾讯云的其他服务集成，如 BGP 高防，共享带宽包等， 致力为您构筑端到端的云上网络解决方案。

- 海量请求访问公网
- 安全访问公网

NAT 网关的 SNAT 功能，可为 CVM 主动访问公网提供安全的地址转换，避免 CVM 的公网 IP 因直接暴露在 Internet 而产生的网络安全隐患。同时，使用 NAT 网关还可以避免 CVM 被外界主动连接，保障云上资源安全。

![](https://mc.qcloudimg.com/static/img/178aec28d46760a6bf66d4e549a77220/image.svg)

2016

- 05月

  05-20

  05-20

  已发布

  NAT 网关新产品上线

  高性能、双机热备、大带宽网关，满足您的海量 Internet 访问诉求。

2022

- 03月

  03-23

  03-23

  已发布

  NAT 网关控制台对所绑定的 EIP 展示优化、管理优化

  新增支持展示 EIP 计费类型，带宽上限等信息，支持调整 EIP 的带宽上限。

2023

- 06月

  06-01

  06-01

  已发布

  新购标准型 NAT 网关价格下调15%

  自2023年06月01日起，新购标准型 NAT 网关，实例费和 CU 费价格均下调15%。此次降价长期有效，如后续有调整会提前发布公告通知。

2024

- 09月

  09-02

  2024-09-02

  公测中

  标准型NAT网关支持网关流控

  标准型NAT网关是可用性更强、稳定性更高的NAT网关。

- 11月

  11-02

  2024-11-02

  已发布

  标准型NAT网关支持网关流控

  标准型NAT网关是可用性更强、稳定性更高的NAT网关。

2026

- 02月06日

  02-06

- 一般常见问题
- 计费
- 网络
- 地域和可用区
- 安全性

### 在何处可以找到有关安全性的更多信息？

腾讯云提供安全组、加密登录、弹性 IP 等各种网络与安全性服务保障您的实例安全、高效、自由地对内对外提供服务。 如需有关云服务器的安全性更多信息，请参阅 [网络与安全性概述](https://cloud.tencent.com/document/product/213/5220)。

### 如何防止他人查看我的系统？

### 出现安全问题如何排查？

更多问题请查看 [常见问题](https://cloud.tencent.com/document/product/552/18626)，也可在 [问答社区](https://cloud.tencent.com/developer/ask) 中进行提问 。

[负载均衡 CLB

负载均衡提供安全快捷的流量分发服务，访问流量经由 CLB 可以自动分配到云中的多台云服务器上，扩展系统的服务能力并消除单点故障。](https://cloud.tencent.com/product/clb)

[共享流量包 TP

共享流量包是一种预付费公网流量套餐，可自动抵扣多种产品的流量消耗。相比后付费流量，共享流量包单价更低，支持统一查看、分析、管理流量用量。](https://cloud.tencent.com/product/tp)

[VPN 连接

VPN 连接（VPN Connections）是一种基于网络隧道技术，实现本地数据中心与腾讯云上资源连通的传输服务，快速构建一条安全、可靠的加密通道。](https://cloud.tencent.com/product/vpn)

[弹性公网 IP

弹性公网 IP支持在某个地域下固定不变的公网 IP 地址，可与 CVM、NAT 网关、弹性网卡和高可用虚拟 IP 等云资源绑定，提供访问公网和被公网访问能力。](https://cloud.tencent.com/product/eip)

按照我们的入门指南，只需点击几次鼠标，即可创建您的首个 NAT 网关。

