---
title: "华为账号使用的安全最佳实践"
code: "securityInfo"
category: "安全与合规"
source_url: "https://support.huaweicloud.com/bestpractice-securityInfo/securityInfo_01_0029.html"
crawled_at: "2026-02-05T16:54:26.081894"
---

# 华为账号使用的安全最佳实践

## 产品简介

租户安全排查与加固建议

## 产品图片

![图片1](https://support.huaweicloud.com/bestpractice-securityInfo/public_sys-resources/note_3.0-zh-cn.png)

![图片2](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001142816820.png)

![图片3](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001183134541.png)

![图片4](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001182892843.png)

![图片5](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001183138183.png)

![图片6](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001136699518.png)

![图片7](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001182942511.png)

![图片8](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001137022550.png)

## 详细说明

# 华为账号使用的安全最佳实践

为保障您的华为账号安全，帮助您安全地访问华为云资源，请您遵循安全使用IAM的建议。

#### 开启登录保护

开启登录保护后，您或者您账号中的用户登录时还需要通过虚拟MFA、短信或邮件验证，再次确认登录者身份，可以进一步提高账号安全性，有效避免钓鱼式攻击或者用户密码意外泄露。

1. 为账号开启登录保护，如[表1](#securityInfo_01_0029__zh-cn_topic_0000001180411223_table3852315591)所示。

   **表1** 用户角色

   | 用户角色 | 操作指导 |
   | --- | --- |
   | 华为账号 | [进入华为帐号中心](https://id1.cloud.huawei.com/CAS/portal/login.html?lang=zh-cn)。选择“帐号与安全 > 安全验证 > 双重验证”，单击“开启”。 |
   | 华为云账号 | [进入安全设置](https://support.huaweicloud.com/usermanual-iam/iam_07_0001.html#iam_07_0001__zh-cn_topic_0179263545_section113256158575)。选择“敏感操作 > 登录保护”，单击“立即设置”，选择“开启”。 |

   ![](https://support.huaweicloud.com/bestpractice-securityInfo/public_sys-resources/note_3.0-zh-cn.png) 

   * 华为云账号是您首次使用华为云时，在华为云控制台创建的账号，该账号是您的华为云资源归属、资源使用计费的主体，对其所拥有的资源及云服务具有完全的访问权限。
   * 华为账号是您访问华为各网站的统一“身份标识”，您只需注册华为账号，即可访问所有华为服务。
2. 依次为账号下的**所有**IAM用户开启登录保护。
   1. 选择“统一身份认证服务 > 用户”，单击IAM用户所在行的“安全设置”。

      **图1** 用户列表
        
      ![](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001142816820.png "点击放大")
   2. 单击“登录保护”区域的![](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001135071138.gif)。

      **图2** 安全设置
        
      ![](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001183134541.png "点击放大")
   3. 在弹出的“登录保护”对话框，根据需要，选择“验证方式”为“手机”、“邮件地址”或“虚拟MFA”，单击“确定”。

      **图3** 登录保护界面
        
      ![](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001182892843.png "点击放大")

#### 开启敏感操作保护

开启敏感操作保护后，您或者您账号中的用户进行[敏感操作](https://support.huaweicloud.com/usermanual-iam/iam_07_0002.html#section4)时，例如删除资源、生成访问密钥等，需要输入密码和验证码进行验证，可以避免误操作带来的风险和损失。

1. 管理员[进入安全设置](https://support.huaweicloud.com/usermanual-iam/iam_07_0001.html#iam_07_0001__zh-cn_topic_0179263545_section113256158575)。
2. 选择“敏感操作 > 操作保护”，单击“立即启用”。

   **图4** 敏感操作
     
   ![](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001183138183.png "点击放大")

3. 在“操作保护”所在行，单击“开启”，您可以选择“操作员验证”或“指定人员验证”。
   * 操作员验证：触发敏感操作的账号或IAM用户进行二次验证。
   * 指定人员验证：账号及IAM用户触发的敏感操作均由指定人员进行验证。支持手机号、邮件地址，不支持虚拟MFA验证。

   **图5** 敏感操作保护设置
     
   ![](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001136699518.png "点击放大")

4. 单击“确定”，开启操作保护。

#### 设置登录验证策略

设置登录验证策略，例如会话超时、账号锁定策略、最近登录提示、登录验证提示，可以进一步提高账号安全性，避免账号忘记退出或钓鱼式攻击带来的用户密码意外泄露。

1. 管理员[进入安全设置](https://support.huaweicloud.com/usermanual-iam/iam_07_0001.html#iam_07_0001__zh-cn_topic_0179263545_section113256158575)。
2. 选择“登录验证策略”，按照下图策略进行配置。

   **图6** 登录验证策略配置图
     
   ![](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001182942511.png "点击放大")

   ![](https://support.huaweicloud.com/bestpractice-securityInfo/public_sys-resources/note_3.0-zh-cn.png) 

   用户可自行修改“登录验证提示”的自定义验证消息。

#### 设置密码策略

设置密码策略，例如密码最小长度、密码中同一字符连续出现的最大次数、密码不能与历史密码相同，保证使用复杂程度高的强密码，可以进一步提高账号安全性。

1. 管理员[进入安全设置](https://support.huaweicloud.com/usermanual-iam/iam_07_0001.html#iam_07_0001__zh-cn_topic_0179263545_section113256158575)。
2. 选择“密码策略”，按照下图策略进行配置。

   **图7** 密码策略配置图
     
   ![](https://support.huaweicloud.com/bestpractice-securityInfo/zh-cn_image_0000001137022550.png "点击放大")

####
