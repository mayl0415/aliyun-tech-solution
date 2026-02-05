---
title: "什么是VPC终端节点？"
code: "vpcep"
category: "网络"
source_url: "https://support.huaweicloud.com/productdesc-vpcep/zh-cn_topic_0131645194.html"
crawled_at: "2026-02-05T16:29:03.578472"
---

# 什么是VPC终端节点？

## 产品简介

提供VPC之间的私密连接通道

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-vpcep/zh-cn_image_0000002498834200.png)

## 详细说明

# 什么是VPC终端节点？

VPC终端节点（VPC Endpoint），能够将VPC私密地连接到终端节点服务（云服务、用户私有服务），使VPC中的云资源无需弹性公网IP就能够访问终端节点服务，提高了访问效率，为您提供更加灵活、安全的组网方式。

#### 产品架构

VPC终端节点由“终端节点服务”和“终端节点”两种资源实例组成。

* 终端节点服务：指将云服务或用户私有服务配置为VPC终端节点支持的服务，可以被终端节点连接和访问。

  更多内容，请参考[终端节点服务](https://support.huaweicloud.com/productdesc-vpcep/vpcep_01_0013.html)。
* 终端节点：用于在VPC和终端节点服务之间建立便捷、安全、私密的连接通道。

  根据终端节点访问的终端节点服务的类型，终端节点分为接口型终端节点和网关型终端节点。
  + **接口型终端节点：**指访问“接口”型终端节点服务的终端节点，是具备私有IP地址的弹性网络接口，作为接口型终端节点服务的通信入口。

    接口型终端节点根据实例类型分为专业型和基础型，不同实例类型的特点如下：
    - **专业型：**新上线终端节点实例类型，目前已在华北三、华东二、中东-利雅得、华东-青岛、非洲-开罗区域开放。单实例带宽规格最大支持10Gbps、支持IPv6双栈等功能。
    - **基础型：**原终端节点实例类型。
  + **网关型终端节点：**指访问“网关”型终端节点服务的终端节点，是作为一个网关，在其上配置路由，用于将流量指向网关型终端节点服务。

  更多内容，请参考[终端节点](https://support.huaweicloud.com/productdesc-vpcep/vpcep_01_0006.html)。

**图1** VPC终端节点组网示意图
  
![](https://support.huaweicloud.com/productdesc-vpcep/zh-cn_image_0000002498834200.png "点击放大")

如[图1](#zh-cn_topic_0131645194__fig9414746114011)所示，建立了“终端节点”到“终端节点服务”的访问通道，实现：

* VPC 1中的云资源（ECS 1）通过内网访问VPC 3中的云资源（ECS 3）。
* VPC 2中的云资源（ECS 2）通过内网访问云服务（如OBS、DNS）。
* 本地数据中心（IDC）通过VPN或者DC的方式与VPC 2连通，实现IDC通过内网访问云服务（如OBS、DNS）。

更多关于VPC终端节点的组网应用信息，请参见[应用场景](https://support.huaweicloud.com/productdesc-vpcep/zh-cn_topic_0131645196.html)。

#### 如何访问VPC终端节点

VPC终端节点提供了Web化的服务管理平台，即管理控制台和基于HTTPS请求的API管理方式。

* 控制台方式

  用户可直接登录管理控制台访问VPC终端节点。

  + 如果用户已注册账户，可直接登录管理控制台，从主页选择“网络 > VPC终端节点”。
  + 如果未注册，请参见[准备工作](https://support.huaweicloud.com/qs-vpcep/vpcep_02_0200.html#section2)中的“注册华为云并实名认证”。

  通过管理控制台上的简单配置，可以快速使用VPC终端节点。
* API方式

  如果用户需要将VPC终端节点集成到第三方系统，用于二次开发，请使用API方式访问VPC终端节点，具体操作请参见[《VPC终端节点API参考》](https://support.huaweicloud.com/api-vpcep/vpcep_01_0000.html)。

####
