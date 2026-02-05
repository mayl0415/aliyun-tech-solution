---
title: "什么是键值存储服务"
code: "kvs"
category: "存储"
source_url: "https://support.huaweicloud.com/productdesc-kvs/kvs_01_0003.html"
crawled_at: "2026-02-05T16:51:54.296729"
---

# 什么是键值存储服务

## 产品简介

Serverless KV存储服务

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-kvs/public_sys-resources/notice_3.0-zh-cn.png)

![图片2](https://support.huaweicloud.com/productdesc-kvs/zh-cn_image_0000001782013529.png)

## 详细说明

# 什么是键值存储服务

#### KVS简介

键值存储服务（Key-Value Storage Service，KVS）主要面向游戏、大数据、互联网等业务场景提供完全托管的键值存储及索引服务，主要用于应用的键值类数据（如：元数据、描述数据、管理参数、状态数据）的存储，提供可预测的性能和无缝扩展，无需进行分区管理、硬件预置、集群扩展等操作。

使用KVS创建一个存储仓，在存储仓中创建一个或多个表，来存储和检索任意规模的数据。

![](https://support.huaweicloud.com/productdesc-kvs/public_sys-resources/notice_3.0-zh-cn.png) 

虽然KVS服务支持您将数据同步到华为云键值存储指定Region的存储仓里，但是华为云并不感知您对象的具体内容。如果您的行为涉及跨境传输，请您确保使用本服务符合所适用的法律法规要求。

#### 产品架构

KVS产品结构请参考[图1](#kvs_01_0003__zh-cn_topic_0000001704123106__fig1799610924515)。通过和其他产品、服务组合，KVS可以实现如下功能：

* CES实时采样KVS监控指标，提供及时有效的资源信息监控告警，支持配置监控告警，告警通知随时触发随时响应。
* 使用KVS在某个区域可以创建多个仓，在仓中可以创建多个表，在表中可以存储键值（Key-Value，简称KV）数据。
* KVS提供本地二级索引、全局二级索引，帮助您快速检索表中的键值数据，实现快速且准确访问。

**图1** KVS产品架构
  
![](https://support.huaweicloud.com/productdesc-kvs/zh-cn_image_0000001782013529.png "点击放大")

#### 访问方式

云服务平台提供的Web化的服务管理平台，即管理控制台、基于HTTPS请求的API（Application programming interface）管理方式以及SDK方式均可访问键值存储服务。

* API方式

  如果用户需要将云服务平台上的键值存储服务集成到第三方系统，用于二次开发，请使用API方式访问键值存储服务，具体操作请参见[《键值存储服务API参考》](https://support.huaweicloud.com/api-kvs/kvs_02_0007.html)。
* 管理控制台方式

  其他相关操作，请使用管理控制台方式访问键值存储服务。

  如果用户已注册，可直接登录管理控制台，从主页选择“键值存储服务 KVS”。如果未注册，请参见[注册华为账号并开通华为云](https://support.huaweicloud.com/usermanual-account/account_id_001.html)并完成[实名认证](https://support.huaweicloud.com/usermanual-account/account_auth_00001.html)。
* SDK方式

  KVS提供Java、C++等主流语言，帮助用户使用SDK完成二次开发，使用SDK方式访问键值存储服务，具体操作请参见[《键值存储服务SDK参考》](https://support.huaweicloud.com/sdkreference-kvs/kvs_03_0001.html)。

####
