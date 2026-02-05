---
title: "什么是云专线"
code: "dc"
category: "网络"
source_url: "https://support.huaweicloud.com/productdesc-dc/zh-cn_topic_0032053183.html"
crawled_at: "2026-02-05T16:28:54.427403"
---

# 什么是云专线

## 产品简介

搭建本地数据中心与VPC间的专属连接通道

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-dc/zh-cn_image_0000002521851529.png)

![图片2](https://support.huaweicloud.com/productdesc-dc/zh-cn_image_0000002521971541.png)

## 详细说明

# 什么是云专线

云专线（Direct Connect）用于搭建用户本地数据中心与华为云VPC之间高速、低时延、稳定安全的专属连接通道，充分利用华为云服务优势的同时，继续使用现有的IT设施，实现灵活一体，可伸缩的混合云计算环境。

云专线组网图如[图1](#zh-cn_topic_0032053183__fig1527872118518)所示。

**图1** 云专线组网图
  
![](https://support.huaweicloud.com/productdesc-dc/zh-cn_image_0000002521851529.png "点击放大")

#### 介绍视频

通过视频了解华为云云专线服务的主要功能，以及如何实现云下数据中心与云上VPC互通。

[![](https://support.huaweicloud.com/productdesc-dc/zh-cn_image_0000002507357625.png)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/DC-Video/1761553585005782986.mp4)

#### 为什么选择云专线

* 网络质量：专用网络进行数据传输，网络性能高，延迟低，用户使用体验更佳。
* 安全性：用户使用云专线接入华为云上VPC，使用专享私密通道进行通信，网络隔离，满足各类用户对高网络安全性方面的需求。
* 传输带宽：华为云专线单线路最大支持100Gbps带宽连接，满足各类用户带宽需求。

#### 组网方案

用户通过多线路（不同运营商），接入不同的华为云接入点，以实现多链路互备，保障高可靠性。

![](https://support.huaweicloud.com/productdesc-dc/zh-cn_image_0000002521971541.png "点击放大")

#### 组成部分

* [物理连接](https://support.huaweicloud.com/qs-dc/dc_03_0003.html)

  物理连接是用户本地数据中心与接入点的运营商物理网络的专线连接。物理连接提供两种专线接入方式：

  + 标准专线接入：指用户独占端口资源的物理连接，此种类型的物理连接由用户创建，并支持用户创建多个虚拟接口。
  + 托管专线接入：指多个用户共享端口资源的物理连接，此种类型的物理连接由合作伙伴为用户创建，为用户分配VLAN和带宽资源，并且只允许用户创建一个虚拟接口。
* [虚拟网关](https://support.huaweicloud.com/qs-dc/dc_03_0004.html)

  虚拟网关是实现物理连接访问VPC的逻辑接入网关，虚拟网关会关联用户访问的VPC，一个虚拟网关只能关联一个VPC，多条物理连接可以通过同一个虚拟网关实现专线接入，访问同一个VPC。
* [全域接入网关](https://support.huaweicloud.com/usermanual-dc/dc_04_1501.html)

  全域接入网关（Global DC Gateways，DGW），为用户搭建IDC和云上多个Region VPC之间的专属连接通道，用户可用一条物理连接打通全球任意地域的云计算资源，实现IDC和全网算力、存储资源高速互访。

  一个全域接入网关只能接入同一个接入点的物理连接，多个接入点专线接入时，需要创建多个全域接入网关。
* [虚拟接口](https://support.huaweicloud.com/qs-dc/dc_03_0005.html)

  虚拟接口是用户本地数据中心通过专线访问VPC的入口，用户创建虚拟接口关联物理连接和虚拟网关，连通用户网关和虚拟网关，实现云下数据中心和云上VPC的互访。

#### 访问方式

云专线服务提供了Web化的服务管理平台，即管理控制台。

用户可直接登录管理控制台访问云专线服务。

* 如果用户已注册账户，可直接登录管理控制台，在主页选择“网络 > 云专线”。
* 如果未注册，请参见[入门指引](https://support.huaweicloud.com/qs-dc/zh-cn_topic_0145790541.html)中的“注册华为云并实名认证”。

####
