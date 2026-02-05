---
title: "什么是OrgID"
code: "orgid"
category: "开天aPaaS"
source_url: "https://support.huaweicloud.com/productdesc-orgid/orgid_01_0001.html"
crawled_at: "2026-02-05T16:35:03.238076"
---

# 什么是OrgID

## 产品简介

为企业提供统一账号、应用授权管理

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-orgid/zh-cn_image_0000002031104833.png)

## 详细说明

# 什么是OrgID

组织成员账号OrgID是面向企业提供组织管理、企业成员账号管理以及SaaS应用授权管理能力的云服务。OrgID将Huawei ID账号体系延伸到企业用户，统一华为云面向生态SaaS服务的组织、账号，面向生态伙伴推出SaaS服务账号集成规范。

#### 为什么选择OrgID

OrgID通过将Huawei ID扩展到企业组织内部应用领域，解决：

* 企业应用账号统一：企业可以选择使用Huawei ID作为企业SaaS服务的账号，并与企业内部账号关联。
* 账号绑定统一：与企业使用的IDaaS集成，企业用户可以选择使用Huawei ID或企业内部账号登录。
* 单点登录：企业用户一次登录实现轻应用间或SaaS服务间统一登录。
* 企业的统一管理：支持企业管理员对企业的部门、部门用户、账号、应用、应用认证源进行统一管理。
* 企业用户登录成功后，可以免登录打开任意企业内的应用，包括移动端，PC端。
* 通过统一账号来实现企业多维度运营分析：包括租户维度、用户维度、应用维度。

#### 产品功能

* 账号登录：提供组织成员（个人华为账号、管理式华为账号、第三方认证源账号）统一登录界面，实现企业内账号在华为云、业务应用的统一。
* 组织管理：通过个人华为账号或者管理式华为账号管理组织，包括组织部门管理、组织成员管理、组织信息管理，为企业内应用提供组织、部门、成员的统一管理。
* 应用注册：提供多种协议的应用注册管理，包括CAS、OAuth、OIDC、SAML。
* 用户关联中心：Huawei ID和第三方认证源的账号会关联生成用户标识，统一管理在OrgID的用户中心，通过用户中心控制组织下应用的访问。
* 应用授权管理：管理员授权用户可以访问的应用，包括自有应用和云商店联运KIT的SaaS应用。
* 业务访问控制：管理应用的访问策略，包括用户、设备、区域和认证源等。
* 应用单点登录：提供基于OrgID登录后应用间的免登录能力，提供基于App内部应用的免登录能力，提供其他应用的免登录能力。
* 用户运营分析：提供成员行业分析，应用使用分析。
* 三方账号绑定：支持钉钉、企业微信、WeLink等外部认证源的账号登录。

#### 产品架构

OrgID产品架构请参考[图1](#orgid_01_0001__fig888412255415)。

**图1** OrgID产品架构
  
![](https://support.huaweicloud.com/productdesc-orgid/zh-cn_image_0000002031104833.png)

#### 访问方式

* 应用注册协议

  SaaS应用接入OrgID云服务，需要遵从联运KIT规范接入改造，主要是对接统一账号，详细请见[联营SaaS技术对接说明](https://support.huaweicloud.com/usermanual-marketplace/zh-cn_topic_0070649105.html)。
* 地址访问

  组织成员通过[OrgID](https://orgid.macroverse.huaweicloud.com/orgid/console-web/index.html#/login)访问。

####
