---
title: "什么是对象存储迁移服务"
code: "oms"
category: "迁移"
source_url: "https://support.huaweicloud.com/productdesc-oms/zh-cn_topic_0045916963.html"
crawled_at: "2026-02-05T16:37:01.755028"
---

# 什么是对象存储迁移服务

## 产品简介

公有云对象存储数据迁移服务

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-oms/public_sys-resources/note_3.0-zh-cn.png)

## 详细说明

# 什么是对象存储迁移服务

对象存储迁移服务（Object Storage Migration Service，OMS）是一种线上数据迁移服务，帮助您将其他云服务商对象存储服务中的数据在线迁移至华为云的对象存储服务（Object Storage Service，OBS）中。

![](https://support.huaweicloud.com/productdesc-oms/public_sys-resources/note_3.0-zh-cn.png) 

目前支持亚马逊云（中国）、阿里云、微软云、百度云、华为云、金山云、优刻得、青云、七牛云、腾讯云、HTTP/HTTPS数据源、谷歌云平台的对象存储数据迁移。

对象存储迁移服务的典型应用场景有：

* 对象数据搬迁：将典型Web应用搬迁到华为云上时，把用户的对象存储数据搬迁到华为云中。
* 云上容灾：出于灾备，把用户对象存储数据复制到华为云中。
* 对象数据恢复：利用其他云服务提供商备份的数据，恢复用户在华为云丢失的对象存储数据。

#### 主要功能

对象存储迁移服务主要具有以下功能：

**迁移任务**：适用于单个桶数据量不超过3 TB或对象个数不超过500万的对象存储迁移场景，通过创建对象存储迁移任务，可将对象数据进行快速迁移。更多相关功能请参阅[表1](#zh-cn_topic_0045916963__table12746038163919)。

**表1** 迁移任务支持功能

| 功能 | 说明 |
| --- | --- |
| [创建迁移任务](https://support.huaweicloud.com/usermanual-oms/topic_0000001089828284.html) | 创建对象存储任务，对您的对象数据实施迁移。 |
| [查看迁移任务](https://support.huaweicloud.com/usermanual-oms/zh-cn_topic_0045916969.html) | 创建迁移任务后，您可以随时查看迁移的进度以及详情，以确定任务的执行状态是否正常。 |
| [管理迁移任务](https://support.huaweicloud.com/usermanual-oms/zh-cn_topic_0045916984.html) | 创建迁移任务后，您可以对迁移任务执行暂停/恢复、重启、删除等操作。 |

**迁移任务组**：适用于单个桶数据量大于3 TB或对象个数大于500万的对象迁移场景，迁移任务组将源端待迁移对象智能分解到多个迁移任务中并行迁移，最大化利用服务的并发性能。更多相关功能请参阅[表2](#zh-cn_topic_0045916963__table16789165434016)。

**表2** 迁移任务组支持功能

| 功能 | 说明 |
| --- | --- |
| [创建迁移任务组](https://support.huaweicloud.com/usermanual-oms/oms_01_0017.html) | 将一个迁移任务智能拆分为多个迁移任务，并以组的方式进行管理。 |
| [查看迁移任务组](https://support.huaweicloud.com/usermanual-oms/oms_01_0018.html) | 创建迁移任务组后，您可以随时查看迁移的进度以及详情，以确定任务组的执行状态是否正常。 |
| [管理迁移任务组](https://support.huaweicloud.com/usermanual-oms/oms_01_0019.html) | 创建迁移任务组后，您可以对迁移任务执行暂停/恢复、重启等操作。 |

**同步任务**：用于源端变更对象主动同步的场景，通过在源端对象存储服务配置事件触发器，当出现对象新增或修改时，通过函数工作流服务，主动调用OMS服务的数据同步接口，及时将数据同步到华为云OBS侧。更多相关功能请参阅[表3](#zh-cn_topic_0045916963__table15196154084110)。

![](https://support.huaweicloud.com/productdesc-oms/public_sys-resources/note_3.0-zh-cn.png) 

目前只支持华北-北京四、华东-上海一地区。

**表3** 同步任务支持功能

| 功能 | 说明 |
| --- | --- |
| [创建同步任务](https://support.huaweicloud.com/usermanual-oms/oms_01_0042.html) | 填写源端和目的端AK/SK并配置同步任务参数。 |
| [源端配置同步请求](https://support.huaweicloud.com/usermanual-oms/oms_01_0043.html) | 源端配置同步请求，以确保源端云服务提供商的对象存储服务可以针对源端新增、修改对象实时调用OMS同步接口(例如通过消息通知或函数计算服务方式)，以完成对源端新增、修改对象数据的同步迁移。 |
| [监控同步任务状态](https://support.huaweicloud.com/usermanual-oms/oms_01_0044.html) | 同步任务开始后，您可以随时查看同步的进度以及详情，以确定同步迁移的执行状态是否正常。 |

####
