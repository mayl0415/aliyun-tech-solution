---
title: "什么是企业路由器"
code: "er"
category: "网络"
source_url: "https://support.huaweicloud.com/productdesc-er/er_01_0002.html"
crawled_at: "2026-02-05T16:29:07.486087"
---

# 什么是企业路由器

## 产品简介

提供高可靠的集中路由管理能力

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-er/zh-cn_image_0000001197260771.png)

![图片2](https://support.huaweicloud.com/productdesc-er/zh-cn_image_0000001609638497.png)

## 详细说明

# 什么是企业路由器

企业路由器（Enterprise Router, ER）可以连接虚拟私有云（Virtual Private Cloud, VPC）或本地网络来构建中心辐射型组网，是云上大规格、高带宽、高性能的集中路由器。企业路由器使用边界网关协议（Border Gateway Protocol, BGP），支持路由学习、动态选路以及链路切换，极大的提升网络的可扩展性及运维效率，从而保证业务的连续性。

* 您可以将虚拟私有云接入企业路由器，快速打通云上网络，具体可参见[通过企业路由器实现同区域VPC互通](https://support.huaweicloud.com/qs-er/er_01_0062.html)。
* 您可以将两个及以上企业路由器接入云连接（Cloud Connect, CC）的中心网络中，构成ER对等连接，实现云上跨区域网络互通，具体请参见[通过企业路由器和云连接中心网络实现跨区域VPC互通](https://support.huaweicloud.com/bestpractice-er/er_03_0002.html)。
* 您可以将云专线（Direct Connect, DC）或者虚拟专用网络（Virtual Private Network, VPN）接入企业路由器，打通线下互联网数据中心（Internet Data Center, IDC）和云上网络，具体可参见[通过企业路由器和云专线构建混合云组网（全域接入网关DGW）](https://support.huaweicloud.com/bestpractice-er/er_03_0020.html)。
* 您可以通过企业路由器、虚拟私有云VPC和云防火墙（Cloud Firewall，CFW）构建组网，实现云上VPC间的流量防护，包括实时入侵检测与防御、全局统一访问控制、全流量分析可视化、日志审计与溯源分析等，具体可参见[通过企业路由器和云防火墙构建组网](https://support.huaweicloud.com/usermanual-cfw/cfw_01_0206.html)。

[图1](#er_01_0002__fig577816251223)和[图2](#er_01_0002__fig1956811222317)分别展示了不使用和使用企业路由器构建的网络拓扑，详细的对比说明如[表1](#er_01_0002__table1592841615355)所示。

**图1** 不使用企业路由器构建网络
  
![](https://support.huaweicloud.com/productdesc-er/zh-cn_image_0000001197260771.png)

**图2** 使用企业路由器构建网络
  
![](https://support.huaweicloud.com/productdesc-er/zh-cn_image_0000001609638497.png)

**表1** 网络拓扑对比说明

| 对比项 | 不使用企业路由器 | 使用企业路由器 | 企业路由器价值 |
| --- | --- | --- | --- |
| 同区域多个VPC互通 | * 同区域4个VPC需要建立6个对等连接实现互通。 * 4个VPC路由表中各需要配置3条对端VPC的路由，共需要配置12条路由。 | * 将同区域4个VPC接入ER中，ER可以在接入的所有VPC中转发流量。 * ER可以自动学习VPC网段到路由表中，只需要在4个VPC路由表中配置到ER的路由。 | * 免去大量的对等连接配置。 * 减少路由条目配置及维护工作量。 |
| 多个VPC跨区域互通 | 所有区域需要互通的VPC均需要接入云连接中。 | 只需要将每个区域的ER接入云连接中心网络中。 | * 无需在云连接中接入所有网络实例，简化网络拓扑。 * 支持路由学习，无需手工配置路由，快速构建组网。 |
| 线下IDC和云上多个VPC互通 | 需要为每个和IDC互通的VPC建立专线或者VPN。 | 将专线接入ER，多个VPC可以共享专线或者VPN。 | * 支持路由学习，免去繁复配置，降低维护难度。 * 多条链路之间联动，实现负载分担或互为主备。 |

通过对比，可以看出，使用企业路由器构建的网络拓扑更简洁，可扩展性高，同时网络维护工作也更简单。

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-er/zh-cn_image_0000002513478332.png)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/support/er-video/1766995271993917981.mp4)

####
