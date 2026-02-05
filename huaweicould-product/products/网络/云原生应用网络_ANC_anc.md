---
title: "什么是云原生应用网络"
code: "anc"
category: "网络"
source_url: "https://support.huaweicloud.com/productdesc-anc/anc_01_0002.html"
crawled_at: "2026-02-05T16:52:00.475269"
---

# 什么是云原生应用网络

## 产品简介

连通任意VPC和服务的逻辑网络

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-anc/public_sys-resources/notice_3.0-zh-cn.png)

![图片2](https://support.huaweicloud.com/productdesc-anc/zh-cn_image_0000001999326281.png)

![图片3](https://support.huaweicloud.com/productdesc-anc/zh-cn_image_0000002384820158.png)

![图片4](https://support.huaweicloud.com/productdesc-anc/zh-cn_image_0000002179635861.png)

## 详细说明

# 什么是云原生应用网络

#### 什么是云原生应用网络

云原生应用网络（Application Native Cloud，ANC）是一种面向应用的全域互联服务，用于连接、保护和监控应用程序的服务。您可以将ANC与单个虚拟私有云（Virtual Private Cloud，VPC）关联，也可以与多个跨账号或跨区域的VPC关联。当您将ANC与VPC关联后，VPC中的任何客户端只要拥有所需的访问权限，即可连接到与ANC关联的服务端。

服务端是与ANC关联的一个或多个服务，服务是一种可独立部署并且可跨区域的软件单元，用于实现特定任务或功能，包含路由规则、成员组等组件。使用ANC会极大的简化网络复杂度，只需要创建一个ANC，创建好服务，并将服务和VPC关联到ANC，即可以实现VPC与服务的跨区域、跨账号通信。

![](https://support.huaweicloud.com/productdesc-anc/public_sys-resources/notice_3.0-zh-cn.png) 

**云原生应用网络功能目前处于****邀测状态****，如果您需要使用该功能，请[提交工单](https://console.huaweicloud.com/ticket/#/ticketindex/createIndex)申请开通。**

#### 产品架构

**云原生应用网络**

一个连通任意VPC和服务的逻辑网络，可以关联多个跨区域、跨账号的服务和VPC。当服务路由规则允许，VPC客户端可以直接访问该服务。客户端是部署在VPC中并与ANC关联的任何资源。如果获得授权，与同一ANC关联的客户端和服务可以相互通信。

**虚拟私有云**

与ANC关联的VPC，作为客户端可以访问关联ANC的服务。

**服务**

一种可独立部署的软件单元，包含路由规则、成员组等组件。用户可以通过ANC，根据定义的路由规则，访问服务中的资源（成员）。

**成员组**

运行应用程序或服务的资源集合。运行应用程序或服务的资源也称为成员，成员可以是云服务器实例、辅助弹性网卡或弹性负载均衡实例等。

**路由规则**

服务默认组件，用于将请求转发至成员组中的一个成员。每条规则由优先级和权重组成。

在[图1](#anc_01_0002__fig1280632916530)中，客户端可以与两个服务通信，因为客户端VPC和服务与同一个云原生应用网络关联。

**图1** ANC产品架构图
  
![](https://support.huaweicloud.com/productdesc-anc/zh-cn_image_0000001999326281.png "点击放大")

#### 使用ANC构建网络

[图2](#anc_01_0002__fig498191815014)和[图3](#anc_01_0002__fig497493019148)分别展示了不使用和使用ANC构建的网络拓扑，详细的对比说明如[表1](#anc_01_0002__table79811718195013)所示。

**图2** 未使用ANC构建网络
  
![](https://support.huaweicloud.com/productdesc-anc/zh-cn_image_0000002384820158.png "点击放大")

**图3** 使用ANC构建网络
  
![](https://support.huaweicloud.com/productdesc-anc/zh-cn_image_0000002179635861.png "点击放大")

**表1** 网络拓扑对比说明

| 对比项 | 不使用ANC | 使用ANC | ANC价值 |
| --- | --- | --- | --- |
| 客户端VPC与目的端地址冲突 | 采用VPC终端节点，将VPC-C01中待访问的后端资源ECS-C创建为终端节点服务，并在VPC-C02中购买终端节点。  实现客户端VPC-A01通过访问VPC-C02终端节点，访问终端节点服务VPC-C01中ECS-C。 | * 将VPC-A01客户端关联至ANC。 * 将目的端的资源ECS-C加入服务中，将服务关联至ANC。   即可实现VPC-A01客户端跨区域直接访问服务中的资源ECS-C。 | 无需规划地址和路由，地址冲突自动转换。 |
| 访问多个跨区域的资源 | 所有区域需要互通的VPC均需配置企业路由器ER，并且接入云连接CC中。 | * 将VPC-A01客户端关联至ANC。 * 将目的端的资源ECS-B和ECS-C加入服务中，将服务关联至ANC。   即可实现VPC-A01客户端跨区域访问服务中的资源ECS-B和ECS-C。 | * 无需在云连接中接入所有网络实例，简化网络拓扑。 * 支持ANC跨账号、跨区域和跨VPC无感互联，免去繁复配置，降低维护难度。 |

通过对比，可以看出，使用ANC构建的网络拓扑更简洁，可扩展性高，同时网络维护工作也更简单。

####
