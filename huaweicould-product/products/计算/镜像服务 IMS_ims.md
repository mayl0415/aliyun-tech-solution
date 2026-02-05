---
title: "什么是镜像服务"
code: "ims"
category: "计算"
source_url: "https://support.huaweicloud.com/productdesc-ims/zh-cn_topic_0013901609.html"
crawled_at: "2026-02-05T16:27:14.081666"
---

# 什么是镜像服务

## 产品简介

提供完善的镜像管理能力

## 详细说明

# 什么是镜像服务

#### 镜像与镜像服务

镜像是用于创建服务器或磁盘的模板，包含操作系统、业务数据或应用软件。

[镜像服务](https://www.huaweicloud.com/product/ims.html)（Image Management Service）提供镜像的生命周期管理能力。用户可以灵活地使用公共镜像、私有镜像或共享镜像申请弹性云服务器和裸金属服务器。同时，用户还能通过已有的云服务器或使用外部镜像文件创建私有镜像，实现业务上云或云上迁移。

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-ims/zh-cn_image_0000002375106889.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/IMS/IMSProductIntroductioncn.mp4)

#### 镜像类型

镜像分为公共镜像、私有镜像、共享镜像、市场镜像。公共镜像为系统默认提供的镜像，私有镜像为用户自己创建的镜像，共享镜像为其他用户共享的私有镜像。

[图1](#zh-cn_topic_0013901609__fig1939514032416)以动图的形式展示了各类型镜像间的关系。

**图1** 镜像类型
  
![](https://support.huaweicloud.com/productdesc-ims/zh-cn_image_0277911455.gif "点击放大")

| 镜像类型 | 说明 |
| --- | --- |
| 公共镜像 | 常见的标准操作系统镜像，所有用户可见，包括操作系统以及预装的公共应用。公共镜像具有高度稳定性，皆为正版授权，请放心使用，您也可以根据实际需求自助配置应用环境或相关软件。  官方公共镜像支持的操作系统类型包括：Huawei Cloud EulerOS、Windows、CentOS、Debian、openSUSE、Fedora、Ubuntu、EulerOS、AlmaLinux、Rocky Linux、CoreOS等。  说明：  Windows操作系统为市场镜像，该服务由第三方提供。为方便用户选用，在公共镜像中提供入口。  更多关于公共镜像的介绍，请参见“[公共镜像概述](https://support.huaweicloud.com/usermanual-ims/ims_01_0101.html)”。 |
| 私有镜像 | 包含操作系统或业务数据、预装的公共应用以及用户的私有应用的镜像，仅用户个人可见。  私有镜像包括系统盘镜像、数据盘镜像、ISO 镜像和整机镜像，其中：   * 系统盘镜像：包含用户运行业务所需的操作系统、应用软件的镜像。系统盘镜像可以用于创建云服务器，迁移用户业务到云。 * 数据盘镜像：只包含用户业务数据的镜像。数据盘镜像可以用于创建云硬盘，将用户的业务数据迁移到云上。 * ISO 镜像：将外部镜像的ISO文件注册到云平台的私有镜像。ISO镜像是特殊的镜像，只能发放用作临时过渡的云服务器。 * 整机镜像：也叫全镜像，包含用户运行业务所需的操作系统、应用软件和业务数据的镜像。整机镜像基于差量备份制作，相比同样磁盘容量的系统盘镜像和数据盘镜像，创建效率更高。 |
| 共享镜像 | 由其他用户共享而来的私有镜像。  更多关于共享镜像的使用，请参见“[共享镜像](https://support.huaweicloud.com/usermanual-ims/ims_01_0305.html)”。 |
| 市场镜像 | 提供预装操作系统、应用环境和各类软件的优质第三方镜像。无需配置，可一键部署，满足建站、应用开发、可视化管理等个性化需求。  市场镜像通常由具有丰富云服务器维护和配置经验的服务商提供，并且经过华为云云商店和服务商的严格测试和审核，可保证镜像的安全性。 |

#### 镜像服务的功能

镜像服务主要有以下功能：

* 提供常见的主流操作系统公共镜像。
* 由现有运行的弹性云服务器，或由外部导入的方式来创建私有镜像。
* 管理公共镜像，例如：按操作系统类型/名称/ID搜索，查看镜像ID、系统盘大小等详情，查看镜像支持的特性（用户数据注入、磁盘热插拔等）。
* 管理私有镜像，例如：修改镜像属性，共享镜像，复制镜像等。
* 通过镜像创建弹性云服务器。

关于以上功能的细节，请单击[创建私有镜像](https://support.huaweicloud.com/productdesc-ims/ims_01_0004.html)了解更多。

#### 访问方式

公有云提供了Web化的服务管理平台（即管理控制台）和基于HTTPS请求的API（Application programming interface）管理方式。

* API方式

  如果用户需要将镜像服务集成到第三方系统，用于二次开发，请使用API方式访问镜像服务。具体操作请参见《[镜像服务API参考](https://support.huaweicloud.com/api-ims/ims_03_0101.html)》。
* 管理控制台方式

  其他相关操作，请使用管理控制台方式访问镜像服务。如果用户已在云平台注册，可直接登录[IMS控制台](https://console.huaweicloud.com/ecm/?#/ims/manager/imageList/selfImage)。

  如果未注册，请参见“[注册华为账号并开通华为云](https://support.huaweicloud.com/usermanual-account/account_id_001.html)”。

####
