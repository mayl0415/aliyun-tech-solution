---
title: "什么是IAM"
code: "iam"
category: "管理与监管"
source_url: "https://support.huaweicloud.com/productdesc-iam/iam_01_0026.html"
crawled_at: "2026-02-05T16:36:05.839191"
---

# 什么是IAM

## 产品简介

提供身份认证和权限管理功能

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-iam/zh-cn_image_0000001227422723.png)

![图片2](https://support.huaweicloud.com/productdesc-iam/zh-cn_image_0000001176479165.png)

![图片3](https://support.huaweicloud.com/productdesc-iam/zh-cn_image_0000001099461914.png)

## 详细说明

# 什么是IAM

统一身份认证（Identity and Access Management，简称IAM）是华为云提供权限管理的基础服务，可以帮助您安全地控制云服务和资源的访问权限。

IAM无需付费即可使用，您只需要为您账号中的资源进行付费。

#### IAM的优势

**对华为云的资源进行精细访问控制**

您注册华为云后，系统自动创建账号，账号是资源的归属以及使用计费的主体，对其所拥有的资源具有完全控制权限，可以访问华为云所有的云服务。

如果您在华为云购买了多种资源，例如弹性云服务器、云硬盘、裸金属服务器等，您的团队或应用程序需要使用您在华为云中的资源，您可以使用IAM的用户管理功能，给员工或应用程序创建IAM用户，并授予IAM用户刚好能完成工作所需的权限，新创建的IAM用户可以使用自己单独的用户名和密码登录华为云。IAM用户的作用是多用户协同操作同一账号时，避免分享账号的密码。

除了IAM外，还有企业管理服务同样可以进行资源权限管理，相对于IAM，企业管理对资源的控制粒度更为精细，同时还支持企业项目费用的管理，建议结合企业需求选择IAM或是企业管理进行资源权限管理，关于两者的详细区别，请参见：[IAM与企业管理的区别](https://support.huaweicloud.com/iam_faq/iam_01_0101.html)。

![](https://support.huaweicloud.com/productdesc-iam/zh-cn_image_0000001227422723.png)

**跨账号的资源操作与授权**

如果您在华为云购买了多种资源，其中一种资源希望由其它账号管理，您可以使用IAM提供的委托功能。

例如您希望将资源委托给一家专业的代运维公司来运维，通过IAM的委托功能，代运维公司可以使用自己的账号对您委托的资源进行运维。当委托关系发生变化时，您可以随时修改或撤销对代运维公司的授权。下图中账号A即为委托方，账号B为被委托方。

![](https://support.huaweicloud.com/productdesc-iam/zh-cn_image_0000001176479165.png)

**使用企业已有账号登录华为云**

当您希望本企业员工可以使用企业内部的认证系统登录华为云，而不需要在华为云中重新创建对应的IAM用户，您可以使用IAM的身份提供商功能，建立您所在企业与华为云的信任关系，通过联合认证使员工使用企业已有账号直接登录华为云，实现单点登录。

![](https://support.huaweicloud.com/productdesc-iam/zh-cn_image_0000001099461914.png)

#### IAM访问方式

您可以通过以下任何一种方式访问IAM。

* **管理控制台**

  您可以通过基于浏览器的可视化界面，即控制台访问IAM。详情请参考[如何进入IAM控制台](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html#section1)。
* **REST API**

  您可以使用IAM提供的REST API接口以编程方式访问IAM。详情请参考：[API参考](https://support.huaweicloud.com/api-iam/iam_01_0001.html)。

推荐您在使用IAM前，开通云审计服务CTS，方便查看、审计以及回溯IAM的关键操作记录。详情请参考：[IAM支持审计的关键操作](https://support.huaweicloud.com/usermanual-iam/iam_01_0012.html)。

####
