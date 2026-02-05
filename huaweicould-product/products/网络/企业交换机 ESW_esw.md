---
title: "什么是企业交换机"
code: "esw"
category: "网络"
source_url: "https://support.huaweicloud.com/productdesc-esw/esw_pd_0002.html"
crawled_at: "2026-02-05T16:29:11.086618"
---

# 什么是企业交换机

## 产品简介

云上与云下的大二层连接通道

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-esw/zh-cn_image_0000002521838521.png)

## 详细说明

# 什么是企业交换机

企业交换机（Enterprise Switch，简称ESW）可以在虚拟私有云（Virtual Private Cloud, VPC）内提供大二层互联等增强网络转发能力，助力企业客户灵活构建大规模、高性能、高可靠的云上/云下网络。

企业交换机当前仅支持二层连接网关特性，该特性提供一种虚拟隧道网关，可基于虚拟专用网络（Virtual Private Network, VPN）或者云专线（Direct Connect, DC）建立云上与云下之间的二层网络，解决云上和云下网络二层互通问题，允许您在不改变子网、IP规划的前提下将数据中心或私有云主机业务部分迁移上云。

您通过VPN或者云专线连接云上和云下互联网数据中心（Internet Data Center, IDC），此时建立的是三层网络，要求云上与云下子网网段不能重叠。

当云下IDC与云上VPC子网网段重叠，并且需要云上与云下服务器在该重叠子网网段内通信时，您需要建立二层网络，企业交换机可以帮助您实现该需求。

企业交换机作为VPC的隧道网关，与云下IDC侧隧道网关对应，基于VPN或者云专线三层网络，在VPC与云下IDC之间建立二层网络，组网示意图如[图1](#esw_pd_0002__fig344310401286)所示，图中展示云专线的场景，如果是VPN场景，将云专线连接组件替换为VPN连接组件即可，您需要将VPC子网接入到企业交换机中，并指定企业交换机与IDC侧的隧道网关建立连接，使VPC子网与IDC侧子网建立二层通信。

**图1** 云下和云上二层网络组网
  
![](https://support.huaweicloud.com/productdesc-esw/zh-cn_image_0000002521838521.png "点击放大")

####
