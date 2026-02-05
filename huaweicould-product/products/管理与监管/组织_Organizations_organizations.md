---
title: "什么是组织云服务"
code: "organizations"
category: "管理与监管"
source_url: "https://support.huaweicloud.com/productdesc-organizations/org_01_0011.html"
crawled_at: "2026-02-05T16:54:38.227659"
---

# 什么是组织云服务

## 产品简介

提供多账号关系的管理能力

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-organizations/zh-cn_image_0000001463480469.png)

## 详细说明

# 什么是组织云服务

#### 简介

组织（以下简称Organizations）云服务为企业用户提供多账号关系的管理能力。Organizations支持用户将多个华为云账号整合到创建的组织中，并可以集中管理组织下的所有账号。用户可以在组织中统一治理策略，帮助用户更好地满足业务的安全性和合规性需求。

Organizations服务为**免费服务**，不收取任何费用。用户只需要对各账号中使用的其他云服务或者资源实例付费。

#### 产品架构

Organizations服务的产品架构可以分为：组织的组成元素、组织策略、可信服务。

**图1** Organizations服务的产品架构
  
![](https://support.huaweicloud.com/productdesc-organizations/zh-cn_image_0000001463480469.png "点击放大")

#### 组织的组成元素

* **组织**

  为管理多账号关系而创建的实体。一个组织由**管理账号**、**成员账号**、**根组织单元**、**组织单元**（Organizational Unit，以下简称OU）四个部分组成。一个组织有且仅有一个管理账号，若干个成员账号，以及由一个根组织单元和多层级组织单元组成的树状结构。成员账号可以关联在根组织单元或任一层级的组织单元。
* **根组织单元**

  当您开通Organizations云服务并创建组织后，系统会为您自动生成根组织单元。根组织单元位于整个组织树的顶端，组织由根组织单元向下关联组织单元和账号。
* **组织单元**

  组织单元是可以理解为成员账号的容器或分组单元，通常可以映射为企业的部门、子公司或者项目组等。组织单元可以嵌套，一个组织单元只能有一个父组织单元，一个组织单元下可以关联多个子组织单元或者成员账号。
* **管理账号**

  管理账号是标准的华为云账号。企业管理员在管理账号中，使用Organizations服务[创建组织](https://support.huaweicloud.com/usermanual-organizations/org_03_0015.html)，并管理组织中其他账号。在管理账号中还可以管理整个组织的相关策略和可信服务。
* **成员账号**

  当启用Organizations服务后，通过Organizations服务邀请加入或直接创建的账号称为成员账号。成员账号可以关联在根组织单元或者任一个组织单元下。
* **邀请**

  邀请其他账号加入组织的过程。邀请只能由管理账号发出，被邀请账号只有接受邀请后，才会加入组织。通过邀请加入组织的账号，原财务关系不会调整，保留原有企业主子账号之间的财务模式。

#### 组织策略

* **服务控制策略**

  服务控制策略 (Service Control Policy，以下简称SCP) 是一种基于组织的访问控制策略。组织管理账号可以使用SCP指定组织中成员账号的权限边界，限制账号内用户的操作。服务控制策略可以关联到组织、组织单元和成员账号。当服务控制策略关联到组织或组织单元时，该组织或组织单元下所有账号受到该策略影响。详情可参考[服务控制策略介绍](https://support.huaweicloud.com/usermanual-organizations/org_03_0031.html)。
* **标签策略**

  标签策略是策略的一种类型，可帮助您在组织账号中对资源添加的标签进行标准化管理。标签策略可以关联到组织、组织单元和成员账号。标签策略对未添加标签的资源或未在标签策略中定义的标签不会生效。

#### 可信服务

* **可信服务**

  可信服务是指可与Organizations服务集成，提供组织级管理能力的华为云服务。启用华为云服务为可信服务后，可信服务会在成员账号中创建一个服务关联委托，该委托允许可信服务在成员账号中拥有执行可信服务文档中所述任务的权限，相当于云服务能力在多账号组织场景下的拓展。目前支持的可信服务请参见：[已对接组织的可信服务列表](https://support.huaweicloud.com/usermanual-organizations/org_03_0042.html)。
* **委托管理员账号**

  委托管理员账号是一个组织中有特殊权限的成员账号。管理账号可指定某个成员账号成为某个可信服务的委托管理员账号。成为委托管理员账号后，该账号下的用户可以使用对应可信服务的组织级管理能力。

#### 如何访问Organizations云服务

通过管理控制台、基于HTTPS请求的API（Application Programming Interface）两种方式访问Organizations云服务。

* 管理控制台方式

  管理控制台是网页形式的，您可以使用直观的界面进行相应的操作。登录[组织管理控制台](https://console.huaweicloud.com/organizations/?&locale=zh-cn#/home)。
* API方式

  如果用户需要将云服务平台上的组织服务集成到第三方系统，用于二次开发，请使用API方式访问Organizations云服务。具体操作请参见[Organizations云服务API参考](https://support.huaweicloud.com/api-organizations/org_04_001.html)。

####
