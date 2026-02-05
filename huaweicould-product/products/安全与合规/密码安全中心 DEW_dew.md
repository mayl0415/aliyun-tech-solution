---
title: "什么是密码安全中心"
code: "dew"
category: "安全与合规"
source_url: "https://support.huaweicloud.com/productdesc-dew/dew_01_0093.html"
crawled_at: "2026-02-05T16:35:48.813889"
---

# 什么是密码安全中心

## 产品简介

云上数据加密和密钥托管服务

## 详细说明

# 什么是密码安全中心

数据是企业的核心资产，每个企业都有自己的核心敏感数据。这些数据都需要被加密，从而保护它们不会被他人窃取。

密码安全中心（Data Encryption Workshop, DEW）是一个综合的云上数据加密服务。它提供密钥管理（KMS）、凭据管理（CSMS）、密钥对管理（KPS）、专属加密(DHSM）、云平台密码系统服务（CPCS）等微服务，安全可靠地为您解决数据安全、密钥安全、密钥管理复杂等问题。其密钥由硬件安全模块（Hardware Security Module，HSM） 保护，并与多个华为云服务集成。您也可以借此服务开发自己的加密应用。

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-dew/zh-cn_image_0000002485358925.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/DEW/1703069525074827359.mp4)

#### 服务介绍

**表1** 服务介绍

| 名称 | 定义 | 更多信息 |
| --- | --- | --- |
| 密钥管理服务  （Key Management Service, KMS） | 密钥管理是一种安全、可靠、简单易用的密钥托管服务，帮助您轻松创建和管理密钥，保护密钥的安全。  KMS通过使用硬件安全模块（Hardware Security Module，HSM）保护密钥安全，HSM模块满足FIPS 140-2 Level 3安全要求。帮助用户轻松创建和管理密钥，所有的用户密钥都由HSM中的根密钥保护，避免密钥泄露。 | [密钥概述](https://support.huaweicloud.com/usermanual-dew/dew_01_7775.html) |
| 云凭据管理服务  （Cloud Secret Management Service，CSMS） | 凭据管理是一种安全、可靠、简单易用的凭据托管服务。  用户或应用程序通过凭据管理服务，创建、检索、更新、删除凭据，轻松实现对敏感凭据的全生命周期和统一管理，有效避免程序硬编码或明文配置等问题导致的敏感信息泄密以及权限失控带来的业务风险。 | [创建凭据](https://support.huaweicloud.com/usermanual-dew/dew_01_9993.html) |
| 密钥对管理服务  （Key Pair Service, KPS） | 密钥对管理是一种安全、可靠、简单易用的SSH密钥对托管服务，帮助用户集中管理SSH密钥对，保护SSH密钥对的安全。  KPS是利用HSM产生的硬件真随机数来生成密钥对，并提供了一套完善和可靠的密钥对的管理方案，帮助用户轻松创建、导入和管理SSH密钥对。生成的SSH密钥对的公钥文件均保存在KPS中，私钥文件由用户自己下载保存在本地，从而保障了SSH密钥对的私有性和安全性。 | [创建密钥对](https://support.huaweicloud.com/usermanual-dew/dew_01_0034.html) |
| 专属加密  （Dedicated Hardware Security Module，Dedicated HSM） | 专属加密是一种云上数据加密的服务，可处理加解密、签名、验签、产生密钥和密钥安全存储等操作。  Dedicated HSM为您提供经国家密码管理局检测认证的加密硬件，帮助您保护弹性云服务器上数据的安全性和完整性，满足监管合规要求。同时，用户能够对专属加密实例生成的密钥进行安全可靠的管理，也能使用多种加密算法来对数据进行可靠的加解密运算。 | [专属加密](https://support.huaweicloud.com/usermanual-dew/dew_01_0079.html) |
| 密码系统服务  （Cloud Platform Cryptosystem Service，CPCS） | 云平台密码系统服务是一种云上的一站式密码服务管理平台。  CPCS为您提供经国家密码管理局检测认证的密码服务，自动部署，简易管理，实时监控，简化了密码应用改造建设流程，提高了商用密码应用安全性评估（密评）效率，可以让用户的应用系统快速通过密评。 | [密码系统服务](https://support.huaweicloud.com/productdesc-dew/dew_01_0367.html) |

####
