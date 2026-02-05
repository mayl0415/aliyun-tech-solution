---
title: "什么是云审计服务"
code: "cts"
category: "管理与监管"
source_url: "https://support.huaweicloud.com/productdesc-cts/cts_01_0001.html"
crawled_at: "2026-02-05T16:36:23.108787"
---

# 什么是云审计服务

## 产品简介

为您提供云账户下资源的操作记录

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-cts/zh-cn_image_0000002209253900.png)

## 详细说明

# 什么是云审计服务

日志审计模块是信息安全审计功能的核心必备组件，是企事业单位信息系统安全风险管控的重要组成部分。

云审计服务（Cloud Trace Service，以下简称CTS），是华为云安全解决方案中专业的日志审计服务，提供对各种云资源操作记录的收集、存储和查询功能，可用于支撑安全分析、合规审计、资源跟踪、问题回溯和问题定位等常见应用场景。

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-cts/zh-cn_image_0000002454533313.jpg)](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/support/cts-video/1756461339363365040.mp4)

#### 云审计服务功能介绍

**图1** 云审计服务介绍

![](https://support.huaweicloud.com/productdesc-cts/zh-cn_image_0000002209253900.png "点击放大")

云审计服务的功能主要包括：

* 记录审计日志：支持记录用户通过管理控制台或API接口发起的操作，以及各服务内部自触发的操作。
* 审计日志查询：支持在管理控制台对7天内操作记录按照事件类型、事件来源、资源类型、筛选类型、操作用户和事件级别等多个维度进行组合查询。
* 审计日志转储：支持将审计日志周期性的转储至对象存储服务（Object Storage Service，简称OBS）下的OBS桶，转储时会按照服务维度压缩审计日志为事件文件，还支持将审计日志转储至云日志服务（Log Tank Service，简称LTS）下的LTS日志流。
* 事件文件加密：支持在转储过程中使用密码安全中心（Data Encryption Workshop，简称DEW）中的密钥对事件文件进行加密。
* 关键操作通知：支持在发生特定操作时使用消息通知服务（Simple Message Notification，简称SMN）向用户手机、邮箱发送消息。

云审计服务记录的操作有以下三种：

* 用户登录管理控制台的操作。
* 用户通过云服务支持的API执行的操作。
* 系统内各服务内部触发的操作。

####
