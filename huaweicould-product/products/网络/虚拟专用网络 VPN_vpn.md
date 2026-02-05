---
title: "什么是虚拟专用网络"
code: "vpn"
category: "网络"
source_url: "https://support.huaweicloud.com/productdesc-vpn/vpn_01_0031.html"
crawled_at: "2026-02-05T16:28:57.393352"
---

# 什么是虚拟专用网络

## 产品简介

数据中心与华为云的IPsec加密连接通道

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-vpn/public_sys-resources/note_3.0-zh-cn.png)

![图片2](https://support.huaweicloud.com/productdesc-vpn/figure/zh-cn_image_0000002123240318.png)

![图片3](https://support.huaweicloud.com/productdesc-vpn/figure/zh-cn_image_0000002158481877.png)

## 详细说明

# 什么是虚拟专用网络

#### 产品概述

虚拟专用网络（Virtual Private Network，以下简称VPN），用于在企业用户本地网络、数据中心与云上网络之间搭建安全、可靠、高性价比的加密连接通道。

![](https://support.huaweicloud.com/productdesc-vpn/public_sys-resources/note_3.0-zh-cn.png) 

不支持在中国大陆和非中国大陆之间建立VPN跨境连接。在埃及使用VPN时，需要向相关机构申请备案，请[提交工单](https://console.huaweicloud.com/ticket/?locale=zh-cn#/ticketindex/serviceTickets)申请备案。

VPN分为站点入云VPN（Site-to-Cloud VPN，以下简称S2C VPN）和终端入云VPN（Point-to-Cloud VPN，以下简称P2C VPN），站点入云VPN基于IPsec协议，终端入云VPN基于SSL协议，两者适用于不同的应用场景。

**站点入云VPN由VPN网关、对端网关和VPN连接组成。**

* VPN网关提供了VPC的公网出口，与用户数据中心的对端网关对应。
* VPN连接通过加密技术，将VPN网关与对端网关相关联，使数据中心与VPC通信，更快速、更安全地构建混合云环境。

站点入云VPN组网图如[图 站点入云VPN组网图](#ZH-CN_TOPIC_0000001542333914__fig480412619539)所示。

**图1** 站点入云VPN组网图
  
![](https://support.huaweicloud.com/productdesc-vpn/figure/zh-cn_image_0000002123240318.png "点击放大")

**终端入云VPN由VPN网关、服务端和客户端组成。**

* VPN网关提供了VPC的公网出口，并绑定对应服务端。
* 服务端实现数据包的封装和解封装，设置和客户端通信的通信端口、加密算法、连通网段。
* 客户端与服务端建立VPN连接，实现对云上资源或服务的远程访问。

终端入云VPN组网图如[图 终端入云VPN组网图](#ZH-CN_TOPIC_0000001542333914__fig17860182755415)所示。

**图2** 终端入云VPN组网图
  
![](https://support.huaweicloud.com/productdesc-vpn/figure/zh-cn_image_0000002158481877.png "点击放大")

#### 组成部分

站点入云VPN

* **VPN网关**：虚拟专用网络在云上的虚拟网关，与用户本地网络、数据中心的对端网关建立安全私有连接。
* **对端网关**：用户数据中心的VPN设备或软件应用程序。控制台上创建的对端网关是云上虚拟对象，用于记录用户数据中心实体设备的配置信息。
* **VPN连接**：VPN网关和对端网关之间的安全通道，使用IKE和IPsec协议对传输数据进行加密。

终端入云VPN

* **VPN网关：**虚拟专用网络在云上的虚拟网关，与客户端建立安全私有连接。
* **服务端**：虚拟网关提供SSL服务的功能模块，用于配置管理及客户端的连接认证。
* **客户端**：用户终端设备上部署的VPN客户端软件。

#### 访问方式

VPN服务提供了Web化的服务管理平台，即管理控制台。用户可以登录管理控制台访问VPN服务。

* 如果用户已注册账户，可直接登录管理控制台，在主页选择“网络 > 虚拟专用网络”。
* 如果未注册，请参见[准备工作](https://support.huaweicloud.com/qs-vpn/vpn_qs_00002.html)中的“注册账号并开通华为云”。

####
