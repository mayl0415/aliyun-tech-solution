---
title: "什么是云证书与管理服务"
code: "ccm"
category: "安全与合规"
source_url: "https://support.huaweicloud.com/productdesc-ccm/ccm_01_0001.html"
crawled_at: "2026-02-05T16:36:00.309243"
---

# 什么是云证书与管理服务

## 产品简介

SSL证书和私有证书管理

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-ccm/zh-cn_image_0000002414506286.png)

## 详细说明

# 什么是云证书与管理服务

云证书与管理服务（Cloud Certificate & Manager，CCM）是一个提供海量证书颁发和管理证书全生命周期的服务。目前，它提供有SSL证书管理（SSL Certificate Manager，SCM）和私有证书管理（Private Certificate Authority，PCA）功能。

**图1** 云证书与管理服务

![](https://support.huaweicloud.com/productdesc-ccm/zh-cn_image_0000002414506286.png)

#### 什么是SSL证书管理

SSL证书管理（SSL Certificate Manager，SCM）是一个SSL（Secure Sockets Layer）证书管理平台。它是由华为云联合全球知名数字证书服务机构（CA，Certificate Authority），在华为云平台上为您提供一站式SSL证书的全生命周期管理，实现网站的可信认证与安全数据传输。

* 什么是SSL证书？

  SSL证书是一种遵守SSL协议的服务器数字证书，由受信任的根证书颁发机构颁发。

  SSL证书采用SSL协议进行通信，SSL证书部署到服务器后，服务器端的访问将启用HTTPS协议。您的网站将会通过HTTPS加密协议来传输数据，可帮助服务器端和客户端之间建立加密链接，从而保证数据传输的安全。
* 华为云SSL证书管理与HTTPS的关系

  您可以通过华为云SSL证书管理购买SSL证书，并向CA机构提交证书申请，CA机构审核通过后将会签发证书。签发后，您需要将SSL证书下载并安装到web服务器中或一键部署至华为云其他云产品中，安装或部署完成后，您的web服务器或云产品将会通过HTTPS加密协议来传输数据。
* SSL证书的作用
  + 网站身份验证，确保数据发送到正确的客户端和服务器。
  + 在客户端和服务器端之间建立加密通道，保证数据在传输过程中不被窃取或篡改。

#### 什么是私有证书管理

私有证书管理（Private Certificate Authority，PCA）是一个私有CA和私有证书管理平台。您可以通过简单的可视化操作，建立自己完整的CA层次体系并使用它签发证书，实现了在组织内部签发和管理自签名私有证书。主要用于对组织内部的应用身份认证和数据加解密。

私有CA颁发的证书仅在您的组织内受信任，在Internet上不受信任。

####
