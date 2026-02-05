---
title: "什么是主机迁移服务"
code: "sms"
category: "迁移"
source_url: "https://support.huaweicloud.com/productdesc-sms/sms_01_0002.html"
crawled_at: "2026-02-05T16:36:58.942518"
---

# 什么是主机迁移服务

## 产品简介

把数据中心或其他云上的主机迁移到华为云

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-sms/zh-cn_image_0000002259896516.png)

![图片2](https://support.huaweicloud.com/productdesc-sms/public_sys-resources/note_3.0-zh-cn.png)

## 详细说明

# 什么是主机迁移服务

主机迁移服务是一种高效、安全的P2V/V2V迁移解决方案，旨在帮助用户将X86物理服务器以及私有云、公有云平台上的虚拟机无缝迁移到华为云。支持的目的端服务器包括弹性云服务器 ECS、Flexus L实例、Flexus X实例、专属主机以及专属云。

主机迁移服务支持热迁移技术，确保源端业务在迁移过程中无需停机，持续稳定运行。 通过主机迁移服务，您可以轻松实现服务器中应用程序与数据的高效迁移，无需担心业务中断问题。操作流程简便流畅，让您能够快速完成云端部署升级，拓展业务发展空间。

#### 视频介绍

[![](https://support.huaweicloud.com/productdesc-sms/zh-cn_image_0000002335736868.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/sms video/1734579291586187630.mp4)

#### 主机迁移服务工作原理

主机迁移服务的工作原理图如[图1](#sms_01_0002__fig030120448379)所示。

**图1** 主机迁移服务工作原理
  
![](https://support.huaweicloud.com/productdesc-sms/zh-cn_image_0000002259896516.png "点击放大")

主机迁移服务的工作原理如下，其中第[1](#sms_01_0002__li17237354266)步、第[3](#sms_01_0002__li1323714520263)步和第[7](#sms_01_0002__li1768374152715)步需要用户操作，其余步骤由主机迁移服务自动完成。

1. 用户在源端服务器上安装迁移Agent。
2. 源端服务器上的迁移Agent向主机迁移服务注册自身连接状态并将源端服务器信息上报到主机迁移服务，完成迁移可行性检查。
3. 用户在主机迁移服务控制台设置目的端并开始迁移。
4. 迁移Agent获取并执行主机迁移服务发送的迁移指令。
5. 迁移源端服务器系统盘。
6. 迁移源端服务器数据盘。
7. 启动目的端。

![](https://support.huaweicloud.com/productdesc-sms/public_sys-resources/note_3.0-zh-cn.png) 

* **源端**：指的是您计划进行迁移的X86架构的物理服务器，或者位于私有云、公有云平台上的虚拟机。
* **目的端**：目的端指迁移后承载源端数据和应用程序，成为新的业务运行环境的服务器。在迁移过程中，源端服务器的数据会按照迁移策略进行传输，并覆盖目的端原有的数据。目的端可以选择华为云上已有服务器（支持弹性云服务器 ECS、Flexus L实例、Flexus X实例、专属主机以及专属云），也可以通过SMS服务新建服务器（仅支持新建ECS服务器）。
* **服务端**：指主机迁移服务。

#### 如何访问主机迁移服务

公有云提供了Web化的服务管理平台，即管理控制台和基于HTTPS请求的API（Application programming interface）管理方式。

* 管理控制台

  请使用管理控制台方式访问主机迁移服务。可直接登录管理控制台，从主页选择“主机迁移服务”。

* API方式

  通过调用API的方式访问主机迁移服务，具体操作请参见[《主机迁移服务API参考》](https://support.huaweicloud.com/api-sms/sms_api_0001.html)。

####
