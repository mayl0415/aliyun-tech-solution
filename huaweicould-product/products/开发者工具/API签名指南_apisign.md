---
title: "概述"
code: "apisign"
category: "开发者工具"
source_url: "https://support.huaweicloud.com/devg-apisign/api-sign-provide01.html"
crawled_at: "2026-02-05T16:55:23.770169"
---

# 概述

## 产品简介

使用签名认证调用通过网关开放的API

## 详细说明

# 概述

本手册将介绍如何使用AK/SK签名认证方式调用通过API网关开放的云服务API，提供[AK/SK签名认证算法详解](https://support.huaweicloud.com/devg-apisign/api-sign-algorithm.html)与[AK/SK签名认证操作指导](https://support.huaweicloud.com/devg-apisign/api-sign-provide.html)，以及Java、Go、Python、C等[多种不同语言的签名SDK和调用示例](https://support.huaweicloud.com/devg-apisign/api-sign-sdk.html)。

* 部分云服务开放的API，不通过API网关，签名认证流程请先参考云服务自身提供的API参考手册。
* 各云服务API参考手册中的“如何调用API”章节，介绍了认证方法。
* SDK打包在示例中，可单独获取SDK，然后参考示例与各语言的API调用说明部分，将SDK集成到您的应用中。
* 如果本手册的多语言签名示例没有涵盖您使用的编程语言，请根据[AK/SK签名认证算法详解](https://support.huaweicloud.com/devg-apisign/api-sign-algorithm.html)，自主实现请求的签名。
* API调用的另一种认证方式为Token认证，Token认证的说明与示例包含在各云服务的API参考手册中的“认证鉴权”章节。
* AK/SK签名认证方式，仅支持Body体大小为12M以内，12M以上的请求，需使用Token认证。
* 云服务具体的API在各云服务的API参考手册中列明。
* 客户端须注意本地时间与时钟服务器的同步，避免请求消息头X-Sdk-Date的值出现较大误差。

  API网关除了校验时间格式外，还会校验该时间值与网关收到请求的时间差，如果时间差超过15分钟，API网关将拒绝请求。

####
