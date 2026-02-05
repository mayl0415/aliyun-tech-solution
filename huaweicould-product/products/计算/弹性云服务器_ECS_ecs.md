---
title: "什么是弹性云服务器？"
code: "ecs"
category: "计算"
source_url: "https://support.huaweicloud.com/productdesc-ecs/zh-cn_topic_0013771112.html"
crawled_at: "2026-02-05T16:50:34.324666"
---

# 什么是弹性云服务器？

## 产品简介

可随时自动获取、弹性伸缩的云服务器

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-ecs/zh-cn_image_0234273593.png)

## 详细说明

# 什么是弹性云服务器？

弹性云服务器（Elastic Cloud Server，ECS）是由CPU、内存、操作系统、云硬盘组成的基础的计算组件。弹性云服务器创建成功后，您就可以像使用自己的本地PC或物理服务器一样，在云上使用弹性云服务器。

弹性云服务器的开通是自助完成的，您只需要指定CPU、内存、操作系统、规格、网络配置、登录鉴权方式即可，同时也可以根据您的需求随时调整弹性云服务器的规格，为您打造可靠、安全、灵活、高效的计算环境。

* CPU、内存和规格，请参见[规格清单（x86）](https://support.huaweicloud.com/productdesc-ecs/zh-cn_topic_0159822360.html)、[规格清单（鲲鹏）](https://support.huaweicloud.com/productdesc-ecs/ecs_01_0066.html)。
* 操作系统，请参见[镜像类型](https://support.huaweicloud.com/productdesc-ecs/ecs_01_0049.html)。
* 登录方式，请参见[登录Linux ECS](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0013771089.html)和[登录Windows ECS](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0092494943.html) 。

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-ecs/zh-cn_image_0000002403201581.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/ECS-video/1721371010565589241.mp4)

#### 为什么选择弹性云服务器

* 丰富的规格类型：提供多种类型的弹性云服务器，可满足不同的使用场景，每种类型的弹性云服务器包含多种规格，同时支持规格变更。
* 丰富的镜像类型：可以灵活便捷地使用公共镜像、私有镜像或共享镜像申请弹性云服务器。
* 丰富的磁盘种类：提供高IO、通用型SSD、超高IO、极速型SSD、通用型SSD V2性能的硬盘，满足不同业务场景需求。
* 灵活的计费模式：支持包年/包月、按需计费以及竞价计费等模式购买云服务器，满足不同应用场景，根据业务波动随时购买和释放资源。
* 数据可靠：基于分布式架构的，可弹性扩展的虚拟块存储服务；具有高数据可靠性，高I/O吞吐能力。
* 安全防护：支持网络隔离，安全组规则保护，远离病毒攻击和木马威胁；Anti-DDoS流量清洗、Web应用防火墙、漏洞扫描等多种安全服务提供多维度防护。
* 弹性易用：根据业务需求和策略，自动调整弹性计算资源，高效匹配业务要求。
* 高效运维：提供控制台、远程终端和API等多种管理方式，给您完全管理权限。
* 云端监控：实时采样监控指标，提供及时有效的资源信息监控告警，通知随时触发随时响应。
* 负载均衡：弹性负载均衡将访问流量自动分发到多台云服务器，扩展应用系统对外的服务能力，实现更高水平的应用程序容错性能。

更多选择理由，请参见[产品优势](https://support.huaweicloud.com/productdesc-ecs/ecs_01_0002.html)和[应用场景](https://support.huaweicloud.com/productdesc-ecs/ecs_01_0003.html)。

#### 产品架构

通过和其他产品、服务组合，弹性云服务器可以实现计算、存储、网络、镜像安装等功能：

* 弹性云服务器在不同可用区中部署（可用区之间通过内网连接），部分可用区发生故障后不会影响同一区域内的其他可用区。
* 可以通过虚拟私有云建立专属的网络环境，设置子网、安全组，并通过弹性公网IP实现公网连接。
* 通过镜像服务，可以对弹性云服务器安装镜像，也可以通过私有镜像批量创建弹性云服务器，实现快速的业务部署。
* 通过云硬盘服务实现数据存储，并通过云硬盘备份服务实现数据的备份和恢复。
* 云监控是保持弹性云服务器可靠性、可用性和性能的重要部分，通过云监控，用户可以观察弹性云服务器资源。
* 云备份（Cloud Backup and Recovery，CBR）提供对云硬盘和弹性云服务器的备份保护服务，支持基于快照技术的备份服务，并支持利用备份数据恢复服务器和磁盘的数据。

**图1** ECS产品架构
  
![](https://support.huaweicloud.com/productdesc-ecs/zh-cn_image_0234273593.png "点击放大")

#### 访问方式

云服务平台提供了Web化的服务管理平台，即管理控制台和基于HTTPS请求的API（Application programming interface）管理方式。

* API方式

  如果用户需要将云服务平台上的弹性云服务器集成到第三方系统，用于二次开发，请使用API方式访问弹性云服务器，具体操作请参见[《弹性云服务器API参考》](https://support.huaweicloud.com/api-ecs/ecs_01_0008.html)。
* 控制台方式

  其他相关操作，请使用管理控制台方式访问弹性云服务器。

  如果用户已注册，可直接登录管理控制台，从主页选择“弹性云服务器”。如果未注册，请参见[注册华为账号并开通华为云](https://support.huaweicloud.com/usermanual-account/account_id_001.html)和[实名认证](https://support.huaweicloud.com/usermanual-account/zh-cn_topic_0071343161.html)。

####
