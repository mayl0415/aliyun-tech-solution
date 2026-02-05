---
title: "什么是资源访问管理"
code: "ram"
category: "管理与监管"
source_url: "https://support.huaweicloud.com/productdesc-ram/ram_01_0001.html"
crawled_at: "2026-02-05T16:36:34.897301"
---

# 什么是资源访问管理

## 产品简介

提供安全的跨账号共享资源的能力

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-ram/zh-cn_image_0000002139533461.png)

## 详细说明

# 什么是资源访问管理

#### 简介

资源访问管理（Resource Access Manager，简称RAM）服务为用户提供安全的跨账号共享资源的能力。如果您有多个华为云账号，您可以创建一次资源，并使用RAM服务将该资源共享给其他账号使用，这样您就不需要在每个账号中创建重复的资源。支持共享的云服务和资源类型请参见：[支持共享的云服务和资源类型](https://support.huaweicloud.com/productdesc-ram/ram_01_0007.html)。

如果您的账号由[组织](https://support.huaweicloud.com/productdesc-organizations/org_01_0011.html)管理，则您可以直接与组织、OU或成员账号共享资源，还可以输入账号ID与账号共享，无论账号是否属于组织。

#### 产品功能

**资源共享管理**

使用RAM服务，资源所有者可以集中管理资源的共享。资源所有者可以将指定资源共享给指定对象（包括组织、OU以及账号），资源所有者还可以随时更新或删除资源共享实例。

资源使用者可以接受或拒绝共享邀请，查看当前正在使用的共享信息，以及在共享资源使用结束后退出共享。

**共享信息查询**

资源所有者可以查询当前已经共享的资源信息，以及资源使用者的相关信息。

资源使用者可以查询当前正在使用的共享资源信息，以及资源所有者信息。

**与组织共享资源**

RAM启用与组织共享资源功能后，资源所有者可以将指定资源共享给组织、OU或成员账号，组织内的账号默认接受该共享邀请。

#### 工作原理

当资源所有者共享资源给另一个账号时，其实是资源所有者将该资源的访问权限授予另一个账号，且授予的权限是在配置资源共享实例时选择的共享权限。资源使用者对该共享资源的操作权限，取决于共享中配置的资源共享权限。

RAM的工作原理如下图所示：

**图1** RAM工作原理
  
![](https://support.huaweicloud.com/productdesc-ram/zh-cn_image_0000002139533461.png "点击放大")

#### 访问方式

通过管理控制台、基于HTTPS请求的API（Application Programming Interface）两种方式访问RAM。

* 管理控制台方式

  您可以通过基于浏览器的可视化界面，即控制台访问RAM。登录[RAM管理控制台](https://console.huaweicloud.com/ram/?&locale=zh-cn#/ownedShares/list)。
* API方式

  如果用户需要将云平台上的RAM集成到第三方系统，用于二次开发，请使用API方式访问RAM，具体操作请参见[《资源访问管理API参考》](https://support.huaweicloud.com/api-ram/ram_04_0002.html)。

####
