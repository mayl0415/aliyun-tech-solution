---
title: "什么是裸金属服务器"
code: "bms"
category: "计算"
source_url: "https://support.huaweicloud.com/productdesc-bms/bms_01_0001.html"
crawled_at: "2026-02-05T16:26:45.903443"
---

# 什么是裸金属服务器

## 产品简介

高性能、高安全的云上物理服务器

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-bms/zh-cn_image_0290913715.png)

![图片2](https://support.huaweicloud.com/productdesc-bms/public_sys-resources/note_3.0-zh-cn.png)

## 详细说明

# 什么是裸金属服务器

#### 裸金属服务器介绍

裸金属服务（Bare Metal Server，BMS）是一款兼具弹性云服务器和物理机性能的计算类服务，为您和您的企业提供专属的云上物理服务器，为核心数据库、关键应用系统、高性能计算、大数据等业务提供卓越的计算性能以及数据安全。租户可灵活申请，按需使用。

裸金属服务器的开通是自助完成的，您只需要指定具体的服务器类型、镜像、所需要的网络配置等，即可在30min内获得所需的裸金属服务器。服务器供应、运维工作交由华为云，您可以专注于业务创新。

#### 产品架构

通过和其他服务组合，裸金属服务器可以实现计算、存储、网络、镜像安装等功能：

* 裸金属服务器在不同可用区中部署（可用区之间通过内网连接），部分可用区发生故障后不会影响同一区域内的其他可用区。
* 可以通过虚拟私有云（Virtual Private Cloud，VPC）建立专属的网络环境，设置子网、安全组，并通过弹性公网IP实现外网链接（需带宽支持）。
* 通过镜像服务，可以对裸金属服务器安装镜像，也可以通过私有镜像批量创建裸金属服务器，实现快速的业务部署。
* 通过云硬盘服务实现数据存储，并通过云硬盘备份服务实现数据的备份和恢复。
* 云监控是保持裸金属服务器可靠性、可用性和性能的重要部分，通过云监控，用户可以观察裸金属服务器资源。
* 云备份提供对云硬盘和裸金属服务器的备份保护服务，支持基于快照技术的备份服务，并支持利用备份数据恢复服务器和磁盘的数据。

**图1** BMS产品架构
  
![](https://support.huaweicloud.com/productdesc-bms/zh-cn_image_0290913715.png "点击放大")

#### 裸金属服务器与物理机、虚拟机的功能对比

裸金属服务器与物理机、虚拟机的对比如[表1](#bms_01_0001__table2456835219)所示。其中，Y表示支持，N表示不支持，N/A表示不涉及。

![](https://support.huaweicloud.com/productdesc-bms/public_sys-resources/note_3.0-zh-cn.png) 

无特性损失、无性能损失：裸金属服务器具备物理机的一切特性和优势，您的应用可以直接访问裸金属服务器的处理器和内存，无任何虚拟化开销。

**表1** 特性对比

| 功能分类 | 功能 | 裸金属服务器 | 物理机 | 虚拟机 |
| --- | --- | --- | --- | --- |
| 下发方式 | 自动化发放 | Y | N | Y |
| 计算 | 无特性损失 | Y | Y | N |
| 无性能损失 | Y | Y | N |
| 资源无争抢 | Y | Y | N |
| 存储 | 拥有本地存储 | Y | Y | N |
| 使用云硬盘（系统盘）启动 | Y | N | Y |
| 使用镜像，免操作系统安装 | Y | N | Y |
| 网络 | 使用虚拟私有云网络 | Y | N | Y |
| 物理机集群和虚拟机集群之间通过VPC通信 | Y | N | Y |
| 管控 | 远程登录等用户体验和虚拟机一致 | Y | N | Y |
| 支持监控以及关键操作审计 | Y | N | Y |

#### 常用概念

* 云上的物理计算资源，即运行在华为云数据中心的裸金属服务器，请查看[实例](https://support.huaweicloud.com/productdesc-bms/bms_01_0003.html#bms_01_0003__section19818434175418)。
* 描述裸金属服务器所在的数据中心，请查看[区域和可用区](https://support.huaweicloud.com/productdesc-bms/bms_01_0004.html)。
* 裸金属服务器由不同的CPU、内存、存储和网络等组成，请查看[实例类型](https://support.huaweicloud.com/productdesc-bms/bms_01_0003.html#bms_01_0003__section998171914438)。
* 裸金属服务器运行环境的模板，其中包含了特定的操作系统和一些预装的应用软件，请查看[镜像](https://support.huaweicloud.com/productdesc-bms/bms_pd_0005.html)。
* 裸金属服务器网络类型及各自使用场景，请查看[网络](https://support.huaweicloud.com/productdesc-bms/bms_pd_0089.html)。
* 实例对内和对外的服务地址，即[私有IP地址](https://support.huaweicloud.com/usermanual-bms/bms_01_0078.html)和[弹性公网IP地址](https://support.huaweicloud.com/usermanual-bms/bms_01_0011.html)。

#### 访问方式

云服务平台提供了Web化的服务管理系统（即管理控制台）和基于HTTPS请求的API（Application Programming Interface）管理方式。

* API方式

  如果用户需要将云服务平台上的裸金属服务器集成到第三方系统，用于二次开发，请使用API方式访问裸金属服务器。
* 管理控制台方式

  其他相关操作，请使用管理控制台方式访问裸金属服务器。如果用户已注册公有云，可直接登录[BMS控制台](https://console.huaweicloud.com/ecm/?#/bms/manager/bmsInfo/vmList)。

  如果未注册，请参见[注册华为账号并开通华为云](https://support.huaweicloud.com/usermanual-account/account_id_001.html)和[实名认证](https://support.huaweicloud.com/usermanual-account/zh-cn_topic_0071343161.html)。

####
