---
title: "什么是我的凭证"
code: "ca"
category: "用户服务"
source_url: "https://support.huaweicloud.com/usermanual-ca/ca_05_0001.html"
crawled_at: "2026-02-05T16:56:23.953352"
---

# 什么是我的凭证

## 产品简介

集中展示与管理用户的身份凭证信息

## 产品图片

![图片1](https://support.huaweicloud.com/usermanual-ca/zh-cn_image_0000002389884189.png)

![图片2](https://support.huaweicloud.com/usermanual-ca/zh-cn_image_0000002389904837.png)

## 详细说明

# 什么是我的凭证

我的凭证是将用户的身份凭证信息进行集中展示与管理的服务。

当您通过API访问华为云时，需要使用您的身份凭证，例如账号名称、账号ID、IAM用户ID等，您可以在我的凭证新版控制台页面查看相关的身份凭证。同时还可以在我的凭证页面管理您的登录凭证、访问密钥（AK/SK）和多因素认证设备。

#### 约束与限制

如果IAM用户需要查看和修改我的凭证，需要先获取相关的权限，详细的授权项请参考[IAM身份策略授权参考](https://support.huaweicloud.com/api-iam5/iam_02_1124.html)。

#### 查看我的凭证

1. 登录[华为云控制台](https://console.huaweicloud.com)，鼠标移动至右上方的用户名，在下拉列表中选择“我的凭证”。

   **图1** 选择我的凭证
     
   ![](https://support.huaweicloud.com/usermanual-ca/zh-cn_image_0000002389884189.png)
2. 单击右上角“体验新版控制台”，进入新版我的凭证界面。

   **图2** 进入新版我的凭证
     
   ![](https://support.huaweicloud.com/usermanual-ca/zh-cn_image_0000002389904837.png "点击放大")
3. 在“我的凭证”页面，查看[登录凭证](https://support.huaweicloud.com/usermanual-ca/ca_05_0002.html)、[访问密钥](https://support.huaweicloud.com/usermanual-ca/ca_05_0003.html)和[多因素认证设备](https://support.huaweicloud.com/usermanual-ca/ca_05_0005.html)。

   **表1** 我的凭证信息

   | 基本信息 | | 说明 |
   | --- | --- | --- |
   | 身份凭证 | IAM用户名 | IAM用户的登录名，登录华为云时需要提供。 |
   | IAM用户ID | IAM用户在华为云的标识ID，由系统自动生成，无法修改。 |
   | 账号名 | 账号的名称，账号是承担费用的主体（例如一个企业），在注册时自动创建，云服务资源按账号完全隔离。 |
   | 账号ID | 账号在华为云中的标识ID，由系统自动生成，无法修改。 |
   | 登录凭证 | | 登录凭证是您登录控制台时使用的登录密码。可以重新自定义设置登录密码，查看密码过期时间和最近一次修改密码的时间。 |
   | 访问密钥 | | 用户的Access Key/Secret Key (AK/SK)，最多可创建两对。使用API访问系统时需要使用AK/SK进行签名。 |
   | 多因素认证设备 | | 启用多因素认证后，用户进行操作时，除了需要提供用户名和密码外（第一次身份验证），还需要提供验证码、插入硬件设备、提供指纹、PIN码或人脸识别（第二次身份验证），多因素身份认证结合起来将为您的账号和资源提供更高的安全保护。 |

**
