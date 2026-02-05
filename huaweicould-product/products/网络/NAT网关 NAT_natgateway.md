---
title: "什么是NAT网关"
code: "natgateway"
category: "网络"
source_url: "https://support.huaweicloud.com/productdesc-natgateway/zh-cn_topic_0086739762.html"
crawled_at: "2026-02-05T16:28:51.424470"
---

# 什么是NAT网关

## 产品简介

提供网络地址转换服务

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-natgateway/zh-cn_image_0000001362369170.png)

![图片2](https://support.huaweicloud.com/productdesc-natgateway/zh-cn_image_0000001412979853.png)

![图片3](https://support.huaweicloud.com/productdesc-natgateway/zh-cn_image_0000001690345157.png)

## 详细说明

# 什么是NAT网关

NAT网关可为您提供网络地址转换服务，分为公网NAT网关和私网NAT网关。

#### 视频介绍

本视频介绍什么是NAT网关服务。

[![](https://support.huaweicloud.com/productdesc-natgateway/zh-cn_image_0000002408863449.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/nat_video/1751624867563538570.mp4)

#### 公网NAT网关

公网NAT网关（Public NAT Gateway）能够为虚拟私有云内的云主机（弹性云服务器、裸金属服务器）或者通过云专线/VPN接入虚拟私有云的本地数据中心的服务器，提供最高20Gbit/s能力的网络地址转换服务，使多个云主机可以共享弹性公网IP访问Internet或使云主机提供互联网服务。

公网NAT网关分为SNAT和DNAT两个功能。

* SNAT功能通过绑定弹性公网IP，实现私有IP向公有IP的转换，可实现VPC内跨可用区的多个云主机共享弹性公网IP，安全，高效的访问互联网。

  SNAT架构如[图1](#zh-cn_topic_0086739762__fig198671834111614)所示。

  **图1** SNAT架构图
    
  ![](https://support.huaweicloud.com/productdesc-natgateway/zh-cn_image_0000001362369170.png)
* DNAT功能绑定弹性公网IP，可通过IP映射或端口映射两种方式，实现VPC内跨可用区的多个云主机共享弹性公网IP，为互联网提供服务。

  DNAT架构如[图2](#zh-cn_topic_0086739762__fig19521019227)所示。

  **图2** DNAT架构图
    
  ![](https://support.huaweicloud.com/productdesc-natgateway/zh-cn_image_0000001412979853.png)

#### 私网NAT网关

私网NAT网关（Private NAT Gateway），能够为虚拟私有云内的云主机（弹性云服务器、裸金属服务器）提供私网地址转换服务。您可以在私网NAT网关上配置SNAT、DNAT规则，可将源、目的网段地址转换为中转IP，通过使用中转IP实现VPC内的云主机与其他VPC、云下IDC互访。

私网NAT网关分为SNAT和DNAT两个功能：

* SNAT功能通过绑定中转IP，可实现VPC内跨可用区的多个云主机共享中转IP，访问外部数据中心或其他VPC。
* DNAT功能通过绑定中转IP，可实现IP映射或端口映射，使VPC内跨可用区的多个云主机共享中转IP，为外部私网提供服务。

**中转子网**

中转子网相当于一个中转网络，是中转IP所属的子网。

**中转IP**

您可以在中转子网中创建私网IP，即中转IP，使本端VPC中的云主机可以共享该私网IP（中转IP）访问用户IDC或其他远端VPC。

**中转VPC**

中转子网所在VPC。

**图3** 私网NAT网关
  
![](https://support.huaweicloud.com/productdesc-natgateway/zh-cn_image_0000001690345157.png)

#### 如何访问NAT网关

通过管理控制台、基于HTTPS请求的API（Application Programming Interface）两种方式访问NAT网关。

* 管理控制台方式

  管理控制台是网页形式的，您可以使用直观的界面进行相应的操作。登录管理控制台，从主页选择“NAT网关”。
* API方式

  如果您需要将云平台上的NAT网关集成到您自己的系统，请使用API方式访问NAT网关。具体操作请参见[《NAT网关API参考》](https://support.huaweicloud.com/api-natgateway/nat_api_0047.html)。

#### NAT网关快速入门

* [通过公网NAT网关的SNAT规则访问公网](https://support.huaweicloud.com/qs-natgateway/nat_qs_0001.html)
* [通过公网NAT网关的DNAT规则访问公网](https://support.huaweicloud.com/qs-natgateway/nat_qs_0006.html)
* [通过私网NAT网关实现云上云下互通](https://support.huaweicloud.com/qs-natgateway/nat_qs_0019.html)

####
