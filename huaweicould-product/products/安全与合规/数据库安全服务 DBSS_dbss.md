---
title: "什么是数据库安全服务？"
code: "dbss"
category: "安全与合规"
source_url: "https://support.huaweicloud.com/productdesc-dbss/dbss_01_0001.html"
crawled_at: "2026-02-05T16:35:51.649408"
---

# 什么是数据库安全服务？

## 产品简介

数据库审计，SQL注入攻击检测

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-dbss/zh-cn_image_0000002300114850.png)

![图片2](https://support.huaweicloud.com/productdesc-dbss/zh-cn_image_0000002333954313.png)

![图片3](https://support.huaweicloud.com/productdesc-dbss/zh-cn_image_0000002333794537.png)

![图片4](https://support.huaweicloud.com/productdesc-dbss/zh-cn_image_0000002299955210.png)

![图片5](https://support.huaweicloud.com/productdesc-dbss/zh-cn_image_0000002300114866.png)

## 详细说明

# 什么是数据库安全服务？

数据库安全服务（Database Security Service，DBSS）提供数据库安全审计、数据库加密与访问控制、数据库运维服务功能，数据库审计通过实时记录用户访问数据库行为，形成细粒度的审计报告，对风险行为和攻击行为进行实时告警。数据库加密与访问控制将系统作为代理加密网关，部署在数据库和客户端应用程序之间，任何访问都需要经过该网关，从而实现数据加密和访问控制功能。数据库运维安全管理通过统一登录、权限管控、多因素认证、操作审批等技术，可实现对于运维人员的最小化权限控制、危险操作阻断以及行为审计。

#### 数据库安全审计

数据库安全审计采用数据库旁路部署方式，支持对华为云上的RDS、ECS/BMS自建的数据库进行审计。

**图1** 数据库安全审计部署架构
  
![](https://support.huaweicloud.com/productdesc-dbss/zh-cn_image_0000002300114850.png "点击放大")

**图2** 组网方式
  
![](https://support.huaweicloud.com/productdesc-dbss/zh-cn_image_0000002333954313.png "点击放大")

**图3** 实现流程
  
![](https://support.huaweicloud.com/productdesc-dbss/zh-cn_image_0000002333794537.png "点击放大")

数据库安全审计的Agent部署说明如下：

* ECS/BMS自建数据库：在数据库端部署Agent
* RDS关系型数据库：在应用端或代理端部署Agent

#### 数据库安全加密

数据库加密与访问控制是一款基于网关代理加密技术，实现敏感数据加密存储的数据库安全防护产品。

系统作为代理加密网关，部署在数据库和客户端应用程序之间，任何访问都需要经过该网关，从而实现数据加密和访问控制功能。

**图4** 组网方式
  
![](https://support.huaweicloud.com/productdesc-dbss/zh-cn_image_0000002299955210.png "点击放大")

#### 数据库安全运维

数据库运维安全管理是一款针对数据库运维人员操作行为安全管控的数据安全产品。

数据库运维安全管理通过统一登录、权限管控、多因素认证、操作审批等技术，可实现对于运维人员的最小化权限控制、危险操作阻断以及行为审计。

**图5** 实现流程
  
![](https://support.huaweicloud.com/productdesc-dbss/zh-cn_image_0000002300114866.png "点击放大")

#### 服务特点

* 助力企业满足等保合规要求
  + 满足等保测评数据库审计需求
  + 满足国内外安全法案合规需求，提供满足数据安全标准（例如Sarbanes-Oxley）的合规报告
* 支持备份和恢复数据库审计日志，满足审计数据保存期限要求
* 支持风险分布、会话统计、会话分布、SQL分布的实时监控能力
* 提供风险行为和攻击行为实时告警能力，及时响应数据库攻击
* 帮助您对内部违规和不正当操作进行定位追责，保障数据资产安全

数据库安全审计采用数据库旁路部署方式，在不影响用户业务的前提下，可以对数据库进行灵活的审计。

* 基于数据库风险操作，监视数据库登录、操作类型（数据定义、数据操作和数据控制）和操作对象，有效对数据库进行审计。
* 从风险、会话、SQL注入等多个维度进行分析，帮助您及时了解数据库状况。
* 提供审计报表模板库，可以生成日报、周报或月报审计报表（可设置报表生成频率）。同时，支持发送报表生成的实时告警通知，帮助您及时获取审计报表。

####
