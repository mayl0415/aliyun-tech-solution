---
title: "什么是配置审计"
code: "rms"
category: "管理与监管"
source_url: "https://support.huaweicloud.com/productdesc-rms/rms_01_0100.html"
crawled_at: "2026-02-05T16:54:34.931919"
---

# 什么是配置审计

## 产品简介

提供全局资源配置管理，配置检测能力

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-rms/public_sys-resources/notice_3.0-zh-cn.png)

![图片2](https://support.huaweicloud.com/productdesc-rms/zh-cn_image_0000001524289093.png)

## 详细说明

# 什么是配置审计

#### 简介

配置审计（Config）服务提供全局资源配置的检索，配置历史追溯，以及基于资源配置的持续的审计评估能力，确保云上资源配置变更符合客户预期。

![](https://support.huaweicloud.com/productdesc-rms/public_sys-resources/notice_3.0-zh-cn.png) 

Config服务的相关功能均依赖于资源记录器收集的资源数据，不开启资源记录器将会影响其他功能的正常使用，例如资源清单页面无法获取资源最新数据、合规规则无法创建、修改、启用和触发规则评估、资源聚合器无法聚合源账号的资源数据等，因此强烈建议您保持资源记录器的开启状态。如何开启并配置资源记录器请参见[配置资源记录器](https://support.huaweicloud.com/usermanual-rms/rms_04_0200.html)。

#### 产品架构

您可以使用Config查看您所拥有的资源有哪些；可以查看资源详情、资源之间的关系、资源历史；Config会在资源变更时发送消息通知给您，并定期（6小时）对您的资源变更消息进行存储；Config还会定期（24小时）对您的资源进行存储；您还可以通过配置合规规则来对您的资源进行合规性检查。

* **查看资源详情：**Config会索引您在云平台上的所有资源信息，为您提供丰富的检索功能。
* **查看资源关系：**Config会建立资源之间的关系状态，帮助您查看资源之间的关联关系。
* **查看资源历史：**您可以通过开启、配置资源记录器，来持续跟踪资源的变更历史。
* **发送消息通知：**您在开启资源记录器并成功配置消息通知（SMN）后，Config会推送资源变更的消息给您。
* **资源变更消息存储：**您在开启资源记录器并成功配置消息通知（SMN）和对象存储桶（OBS）后，Config会定期（6小时）对您的资源变更消息进行存储。
* **资源快照文件存储：**您在开启资源记录器并成功配置对象存储桶（OBS）后，Config会定期（24小时）对您的资源进行快照并对快照文件存储。
* **资源评估：**Config提供合规扫描，帮助您自动化地检查资源的合规性。
* **高级查询：**Config提供高级查询能力，通过使用ResourceQL语法来自定义查询云资源。
* **资源聚合器**：Config提供多账号资源数据聚合能力，通过使用资源聚合器聚合其他华为云账号或者组织成员账号的资源配置和合规性数据到单个账号中，方便统一查询。
* **合规规则包**：Config提供合规规则包能力，合规规则包是多个合规规则的集合，帮助您统一创建和管理合规规则，并统一查询合规性数据。

#### 访问方式

通过管理控制台、基于HTTPS请求的API（Application Programming Interface）两种方式访问配置审计服务。

* **管理控制台方式**

  管理控制台是网页形式的，您可以使用直观的界面进行相应的操作。登录[管理控制台](https://console.huaweicloud.com/?locale=zh-cn)，单击主页左上角的![](https://support.huaweicloud.com/productdesc-rms/zh-cn_image_0000001524289093.png)，选择“管理与监管 >配置审计 Config”。
* **API方式**

  如果用户需要将云平台上的配置审计服务集成到第三方系统，用于二次开发，请使用API方式访问配置审计服务，具体操作请参见[《配置审计API参考》](https://support.huaweicloud.com/api-rms/rms_01_0100.html)。

####
