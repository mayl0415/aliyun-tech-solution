---
title: "什么是云解析服务？"
code: "dns"
category: "网络"
source_url: "https://support.huaweicloud.com/productdesc-dns/zh-cn_topic_0035467690.html"
crawled_at: "2026-02-05T16:29:20.118732"
---

# 什么是云解析服务？

## 产品简介

提供高可用，高扩展的DNS服务和管理服务

## 详细说明

# 什么是云解析服务？

云解析服务（Domain Name Service，DNS）提供高可用、高扩展的DNS服务，把人们常用的域名（如www.example.com）转换成用于计算机连接的IP地址（如 192.1.2.3）。云解析服务可以让您直接在浏览器中输入域名，访问网站或Web应用程序。

云解析服务默认开通，并且可以免费使用。

#### 介绍视频

通过视频了解华为云DNS解析器的主要功能，以及如何实现云下数据中心访问云上DNS或云上服务器访问云下业务域名。

[![](https://support.huaweicloud.com/productdesc-dns/zh-cn_image_0000002376308429.png)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/DNS-Video/video-helpcenter/1749432372378180235.mp4)

#### 基本功能

云解析服务为您提供以下解析服务类型：

* [公网域名解析](https://support.huaweicloud.com/productdesc-dns/zh-cn_topic_0035920135.html)

  云解析服务将公网域名与IP地址相关联，为您提供基于Internet网络的域名解析服务，实现通过域名直接访问网站或者Web应用程序。

* [内网域名解析](https://support.huaweicloud.com/productdesc-dns/dns_pd_0005.html)

  云解析服务将在VPC内生效的内网域名与私网IP地址相关联，为华为云上资源提供VPC内的域名解析服务。
* [反向解析](https://support.huaweicloud.com/productdesc-dns/dns_pd_0006.html)

  云解析服务支持通过IP地址反向获取该IP地址指向的域名，通常用于自建邮件服务器的场景，是提高邮箱IP和域名信誉度的必要设置。
* [混合云解析](https://support.huaweicloud.com/productdesc-dns/dns_pd_1030.html)

  通过DNS解析器实现云下数据中心访问云上DNS或云上服务器访问云下业务域名，把DNS服务100网段地址下沉到客户VPC内，避免混合云组网网段冲突问题。

#### 产品优势

云解析服务具有以下优势：

* **高性能**

  云解析服务采用自研的新一代高性能解析加速服务，单节点支持千万级并发，为您提供高效稳定的解析服务。
* **安全防护**

  云解析服务基于华为自研Anti-DDoS设备以及多年防护经验，可以有效应对各类DDoS攻击。
* **轻松访问云上资源**

  云解析服务支持为云服务器创建内网域名，既支持云服务器之间通过内网域名互相访问，也支持云服务器通过内网DNS访问云上资源，无需经过Internet，访问时延小，性能高。

  您可以参考[为云服务器配置内网域名](https://support.huaweicloud.com/bestpractice-dns/dns_bestprac_0002.html)为您的云服务器创建域名。
* **平滑切换无感知**

  支持将使用中的网站域名迁移至华为云云解析服务进行解析。在域名转入时，我们可以提前创建域名，并设置解析记录，使您网站的DNS服务实现平滑切换，用户访问体验不中断。

  DNS服务平滑切换的详细内容请参考[迁移域名到华为云进行域名解析](https://support.huaweicloud.com/bestpractice-dns/dns_bestprac_0007.html)。
* **核心数据安全隔离**

  对于保存核心数据的云服务器，不绑定弹性IP，使用内网DNS为其提供域名解析服务，这样，既保证了核心数据的安全性，又实现了对核心数据的访问。

#### 如何使用云解析服务

云解析服务提供了Web化的服务管理平台，即管理控制台和基于HTTPS请求的API管理方式。

* **控制台方式**

  用户可直接登录管理控制台访问云解析服务。

  + 如果用户已注册账户，可直接登录[云解析服务控制台](https://console.huaweicloud.com/dns/?#/dns/dashboard)。
  + 如果未注册，请参见[入门指引](https://support.huaweicloud.com/qs-dns/dns_qs_0001.html)中的“注册华为云并实名认证”。

  通过管理控制台上的简单配置，可以快速地让DNS服务开始提供域名解析工作。
* **API方式**

  如果用户需要将云解析服务集成到第三方系统，用于二次开发，请使用API方式访问云解析服务，具体操作请参见[《云解析服务API参考》](https://support.huaweicloud.com/api-dns/dns_api_10000.html)。

####
