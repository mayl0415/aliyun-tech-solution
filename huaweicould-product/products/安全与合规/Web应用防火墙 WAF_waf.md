---
title: "什么是Web应用防火墙"
code: "waf"
category: "安全与合规"
source_url: "https://support.huaweicloud.com/productdesc-waf/waf_01_0045.html"
crawled_at: "2026-02-05T16:35:33.475101"
---

# 什么是Web应用防火墙

## 产品简介

识别恶意请求特征和防御未知威胁

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-waf/zh-cn_image_0000002385865706.png)

![图片2](https://support.huaweicloud.com/productdesc-waf/zh-cn_image_0000002447855137.png)

![图片3](https://support.huaweicloud.com/productdesc-waf/zh-cn_image_0000002419305049.png)

## 详细说明

# 什么是Web应用防火墙

Web应用防火墙（Web Application Firewall，WAF）是一种专门的Web应用程序安全防护工具。它部署在Web应用前端，通过分析检测互联网与Web应用之间的HTTP(S)流量，根据预定义的防护规则，识别并拦截SQL注入、跨站脚本攻击、网页木马上传、命令/代码注入、文件包含、敏感文件访问、第三方应用漏洞攻击、CC攻击、恶意爬虫扫描、跨站请求伪造等Web攻击，保护Web服务器、Web应用程序本身及其承载的敏感数据的安全。

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-waf/zh-cn_image_0000002338491780.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/WAF/1714463695152562664.mp4)

#### 防护原理

网站接入WAF后，所有访问互联网的HTTP(S)请求，包括攻击者的攻击请求、用户的正常业务请求，都会经过WAF检测，WAF过滤攻击请求后，将正常业务请求转发给Web服务器。Web服务器处理请求后，将数据返回给WAF，WAF进行内容过滤（例如脱敏）后，最终返回给用户。

**图1** WAF防护原理
  
![](https://support.huaweicloud.com/productdesc-waf/zh-cn_image_0000002385865706.png "点击放大")

#### 防护体系

为实现安全防护，华为云WAF采用层层检测的设计方案，构建智能多层防护体系，为您的Web应用提供立体化防护。

WAF支持以下防护体系：

* 针对**IP黑白名单**、**地理位置**、**IDC信誉库**、**特定访问请求**的防护：通过最简单、有效的方式，过滤恶意IP或请求。
* 针对**扫描攻击**、**BOT攻击**、**CC攻击**的自动化攻击防护：通过限制自动化攻击，保证服务稳定。
* 针对**常见攻击**的防护：利用规则库检测OWASP攻击，防御常见Web攻击。
* 针对**页面内容**的防护：通过检测响应报文，实现安全防护。
* 针对**大模型应用**的防护：通过检测大模型输入输出内容，确保大模型应用安全合规。

**图2** WAF防御体系
  
![](https://support.huaweicloud.com/productdesc-waf/zh-cn_image_0000002447855137.png "点击放大")

#### 防护对象

WAF支持防护域名（包括泛域名、一级域名、二级域名等各级域名）、IP（包括公网IP、私网IP）。不同接入方式，支持的防护对象不同。

* **云模式-CNAME接入**：域名，华为云、非华为云或本地部署的Web业务
* **云模式-ELB接入**：域名或IP（公网IP/私网IP），华为云的Web业务
* **独享模式接入**：域名或IP（公网IP/私网IP），华为云的Web业务

#### 如何使用WAF

为适应各类业务需要，WAF提供云模式、独享模式两种模式，云模式-CNAME接入、云模式-ELB接入、独享模式接入三种接入方式。您可以根据实际情况，参考[图3](#waf_01_0045__fig1820064413172)，快速使用WAF。更多信息，请参考[入门指引](https://support.huaweicloud.com/qs-waf/index.html)。

**图3** 快速使用WAF
  
![](https://support.huaweicloud.com/productdesc-waf/zh-cn_image_0000002419305049.png "点击放大")

####
