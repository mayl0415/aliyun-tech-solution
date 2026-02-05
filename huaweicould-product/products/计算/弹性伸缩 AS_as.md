---
title: "什么是弹性伸缩？"
code: "as"
category: "计算"
source_url: "https://support.huaweicloud.com/productdesc-as/zh-cn_topic_0042018383.html"
crawled_at: "2026-02-05T16:27:11.113235"
---

# 什么是弹性伸缩？

## 产品简介

根据预设策略自动调整计算资源的服务

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-as/zh-cn_image_0000002304558548.png)

![图片2](https://support.huaweicloud.com/productdesc-as/zh-cn_image_0284722761.png)

## 详细说明

# 什么是弹性伸缩？

#### 弹性伸缩简介

弹性伸缩（Auto Scaling，以下简称AS）是根据用户的业务需求，通过设置伸缩规则来自动增加/缩减业务资源。当业务需求增长时，AS自动为您增加弹性云服务器（ECS）实例或带宽资源，以保证业务能力；当业务需求下降时，AS自动为您缩减弹性云服务器（ECS）实例或带宽资源，以节约成本。AS支持自动调整弹性云服务器和带宽资源。

**图1** 弹性伸缩图例
  
![](https://support.huaweicloud.com/productdesc-as/zh-cn_image_0000002304558548.png "点击放大")

#### 产品架构

通过伸缩控制可以实现弹性云服务器（ECS）实例伸缩和带宽伸缩：

* 伸缩控制：配置策略设置指标阈值/伸缩活动执行的时间，通过云监控监控指标是否达到阈值，通过定时调度，实现伸缩控制。
* 配置策略：可以根据业务需求，配置告警策略/定时策略/周期策略。
* 配置告警策略：可配置CPU、内存、磁盘、入网流量等监控指标。
* 配置定时策略：通过配置触发时间可以配置定时策略。
* 配置周期策略：通过配置重复周期、触发时间、生效时间可以配置周期策略。
* 云监控监控到所配置的告警策略中的某些指标达到告警阈值，从而触发伸缩活动，实现ECS实例的增加/减少或带宽的增大/减小。
* 到达所配置的触发时间时，触发伸缩活动，实现ECS实例的增加/减少或带宽的增大/减小。

**图2** 弹性伸缩产品架构图
  
![](https://support.huaweicloud.com/productdesc-as/zh-cn_image_0284722761.png "点击放大")

#### 访问方式

公有云提供了Web化的服务管理平台，即管理控制台和基于HTTPS请求的API（Application programming interface）管理方式。

* API方式

  如果用户需要将公有云平台上的弹性伸缩服务集成到第三方系统，用于二次开发，请使用API方式访问弹性伸缩服务，具体操作请参见[《弹性伸缩API参考》](https://support.huaweicloud.com/api-as/as_02_0100.html)。
* 控制台方式

  其他相关操作，请使用管理控制台方式访问弹性伸缩服务。

  如果用户已注册公有云，可直接登录[AS控制台](https://console.huaweicloud.com/ecm/?#/as/manager/groupConfigInfo/groupList)”。

####
