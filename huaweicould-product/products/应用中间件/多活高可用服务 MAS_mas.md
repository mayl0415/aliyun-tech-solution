---
title: "什么是多活高可用服务"
code: "mas"
category: "应用中间件"
source_url: "https://support.huaweicloud.com/productdesc-mas/mas_01_0000.html"
crawled_at: "2026-02-05T16:32:27.105127"
---

# 什么是多活高可用服务

## 产品简介

提供端到端业务故障切换及容灾演练能力

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-mas/zh-cn_image_0000001223293458.png)

![图片2](https://support.huaweicloud.com/productdesc-mas/public_sys-resources/note_3.0-zh-cn.png)

## 详细说明

# 什么是多活高可用服务

企业在应用发展的过程中会面临诸多难题，如：

* 使用单个AZ/Region无法满足高可靠诉求；
* 系统容量达到瓶颈或者访问时延无法达到要求；
* 云厂商技术绑定，无法获得先进技术和价格优势；
* 业务爆炸式增长带来的技术瓶颈。

多活高可用服务（Multi-Site High Availability Service，简称MAS）源自华为消费者多活应用高可用方案，提供从流量入口、数据到应用层的端到端的业务故障切换及容灾演练能力，保障故障场景下的业务快速恢复，提升业务连续性。

MAS=多活接入服务+应用层SDK+数据同步管道+统一管控中心；完整可落地方案=技术产品（MAS）+咨询服务+生态伙伴+容灾规范。

MAS产品优势如下：

1. 业务级高可用保障。
2. 流量、业务、数据端到端可用。
3. 秒级RTO、RPO，保证业务连续性。
4. 低成本容灾演练能力。

MAS核心能力包括：

* 端到端（管理-流量-应用-数据）仲裁和多活容灾管控。
* 安全可靠的数据同步管道。
* 可落地的多活容灾标准规范。
* 咨询+专业实施服务。

MAS架构如[图1](#mas_01_0000__fig639219225340)所示。

**图1** MAS服务架构示图
  
![](https://support.huaweicloud.com/productdesc-mas/zh-cn_image_0000001223293458.png)

![](https://support.huaweicloud.com/productdesc-mas/public_sys-resources/note_3.0-zh-cn.png) 

* 区域（Region）：从地理位置和网络时延维度划分，同一个Region内共享弹性计算、块存储、对象存储、VPC网络、弹性公网IP、镜像等公共服务。Region分为通用Region和专属Region，通用Region指面向公共租户提供通用云服务的Region；专属Region指只承载同一类业务或只面向特定租户提供业务服务的专用Region。
* 可用区（AZ，Availability Zone）：一个AZ是一个或多个物理数据中心的集合，有独立的风火水电，AZ内逻辑上再将计算、网络、存储等资源划分成多个集群，一个Region中的多个AZ间通过高速光纤相连，以满足用户跨AZ构建高可用性系统的需求。
* 软件开发工具包（SDK）：SDK 的全称是 Software Development Kit，是一种被用来辅助开发某类软件而编写的特定软件包。
* RPO（Recovery Point Objective）：即数据恢复点目标，主要指的是业务系统所能容忍的数据丢失量。
* RTO（Recovery Time Objective）：即恢复时间目标，主要指的是所能容忍的业务停止服务的最长时间，也就是从灾难发生到业务系统恢复服务功能所需要的最短时间周期。

####
