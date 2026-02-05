---
title: "什么是容器镜像服务"
code: "swr"
category: "容器"
source_url: "https://support.huaweicloud.com/productdesc-swr/swr_03_0001.html"
crawled_at: "2026-02-05T16:29:28.997981"
---

# 什么是容器镜像服务

## 产品简介

一种支持容器镜像全生命周期管理的服务

## 详细说明

# 什么是容器镜像服务

#### 产品简介

容器镜像服务（SoftWare Repository for Container，简称SWR）是一种支持镜像全生命周期管理的服务， 提供简单易用、安全可靠的镜像管理功能，帮助您快速部署容器化服务。

通过使用容器镜像服务，您无需自建和维护镜像仓库，即可享有云上的镜像安全托管及高效分发服务，并且可配合[云容器引擎 CCE](https://support.huaweicloud.com/cce/index.html)、[云容器实例 CCI](https://support.huaweicloud.com/cci/index.html)使用，获得容器上云的顺畅体验。

容器镜像服务基础版免费，企业版收费。基础版和企业版的差异详见[基础版及企业版对比](https://support.huaweicloud.com/productdesc-swr/swr_03_0020.html)。企业版的计费项包括购买仓库的费用、制品存储的费用和制品传输流量费用

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-swr/zh-cn_image_0000002366507613.png)](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/SWR/SWR-Introduction.mp4)

#### 产品类型

**容器镜像服务基础版**

基础版面向个人开发者或企业客户临时测试使用，提供基础的云上镜像托管、分发服务，镜像安全扫描功能以及便捷的镜像授权功能，方便用户进行镜像的全生命周期管理。

**容器镜像服务企业版**

企业版面向企业用户，提供企业级的独享安全托管服务，支持托管容器镜像、Helm Chart等符合OCI标准的云原生制品。企业仓库支持大规模、多地域、多场景下云原生制品的高效分发；支持网络访问控制与细粒度权限控制，支持镜像加签、镜像安全扫描，保障数据安全；与云容器引擎CCE、云容器实例CCI无缝集成，帮助企业降低交付复杂度。

#### 计费说明

* 基础版计费项包括存储空间和流量费用，目前均免费提供给您。
* 企业版目前处于公测阶段（华东-上海一、华北-乌兰察布一、华北-北京四、亚太-新加坡、华南-广州、西南-贵阳一、华东二、中国-香港、非洲-约翰内斯堡、土耳其-伊斯坦布尔、西北-克拉玛依）。SWR企业版暂时不收费，但是SWR企业仓库的镜像存储使用的是对象存储服务OBS，会按照OBS的存储收费和流量收费标准进行收费。 关于OBS的收费详情请参考[OBS的计费说明](https://support.huaweicloud.com/price-obs/obs_42_0001.html)。

  如果您是通过VPC终端节点访问SWR企业版，也会按照VPC终端节点的收费标准进行收费 ，关于VPC终端节点的收费详情请参考[VPC终端节点计费说明](https://support.huaweicloud.com/price-vpcep/vpcep_price_1000.html)。其他非通过VPC终端节点方式访问SWR企业版的均不收费。

#### 产品功能

* 镜像全生命周期管理

  容器镜像服务支持镜像的全生命周期管理，包括镜像的上传、下载、删除等。
* 私有镜像仓库

  容器镜像服务提供私有镜像库，并支持细粒度的权限管理，可以为不同用户分配相应的访问权限（读取、编辑、管理）。
* 镜像加速

  容器镜像服务通过华为自主专利的镜像下载加速技术，使CCE集群下载镜像时在确保高并发下能获得更快的下载速度。
* 镜像仓库触发器

  容器镜像服务支持容器镜像版本更新自动触发部署。您只需要为镜像设置一个触发器，通过触发器，可以在每次镜像版本更新时，自动更新使用该镜像部署的应用。

#### 访问方式

华为云提供了Web化的服务管理平台（即管理控制台）和基于HTTPS请求的API（Application programming interface）管理方式。

* API方式

  如果用户需要将容器镜像服务集成到第三方系统，用于二次开发，请使用API方式访问容器镜像服务。具体操作请参见《[容器镜像服务API参考](https://support.huaweicloud.com/api-swr/swr_02_0101.html)》。
* 管理控制台方式

  其他相关操作，请使用管理控制台方式访问容器镜像服务。如果用户已在云平台注册，可直接登录[SWR控制台](https://console.huaweicloud.com/swr/#/swr/dashboard)。

  如果未注册，请参考[如何注册华为云管理控制台的用户](https://support.huaweicloud.com/qs-consolehome/zh-cn_topic_0016739341.html)，进行账号注册。

####
