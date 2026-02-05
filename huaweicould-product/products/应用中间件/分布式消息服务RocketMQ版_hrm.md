---
title: "什么是分布式消息服务RocketMQ版"
code: "hrm"
category: "应用中间件"
source_url: "https://support.huaweicloud.com/productdesc-hrm/hrm-pd-001.html"
crawled_at: "2026-02-05T16:53:10.705412"
---

# 什么是分布式消息服务RocketMQ版

## 产品简介

低延迟、高可靠，兼容开源RocketMQ

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-hrm/zh-cn_image_0000001462827681.png)

![图片2](https://support.huaweicloud.com/productdesc-hrm/public_sys-resources/note_3.0-zh-cn.png)

## 详细说明

# 什么是分布式消息服务RocketMQ版

分布式消息服务RocketMQ版是一个低延迟、弹性高可靠、高吞吐、动态扩展、便捷多样的消息中间件服务。

分布式消息服务RocketMQ版具有如下特点：

* 兼容开源RocketMQ客户端。
* 提供顺序、延迟、定时、重投、死信、事务消息等功能，更好地适配电商、金融等多样的业务场景。
* 提供消息追踪、消息溯源、链路诊断、死信导出、监控告警等能力，帮助您全方面地了解服务状况，保证业务正常运行。

#### 产品架构

**图1** 产品架构示意图（以4.8.0版本为例）
  
![](https://support.huaweicloud.com/productdesc-hrm/zh-cn_image_0000001462827681.png "点击放大")

示意图说明：

* Broker：负责接收和存储Producer发送的消息，或者转发消息到Consumer。一个Broker由一个主节点和两个备节点组成。
* NameServer：负责接收和存储Broker中的元数据。
* Producer：从NameServer获取元数据，然后将消息发送到Broker。
* Consumer：从NameServer获取元数据，然后从Broker拉取消息。

#### 支持的消息类型

分布式消息服务RocketMQ版支持4种消息类型。

* 普通消息：没有特殊功能的消息，区别于延迟消息、顺序消息和事务消息。
* 延迟消息/定时消息：生产者生产消息到分布式消息服务RocketMQ版后，消息不会立即被消费，而是延迟到特定时间后才会发送给消费者进行消费。
* 顺序消息：消费者按照消息发送的顺序来消费消息。
* 事务消息：提供类似X/Open XA的分布事务功能，通过事务消息能达到分布式事务的最终一致。

#### 支持的高级特性

分布式消息服务RocketMQ版支持4种高级特性。

* 消息过滤：消费者根据分布式消息服务RocketMQ版设置的标签对已订阅Topic中的消息进行过滤，达到只消费需要的消息的目的。
* 消息重试：消费者消费某条消息失败后，分布式消息服务RocketMQ版根据重试机制将消息重新发送给消费者进行消费。如果重试次数到达设定的最大值时，消息尚未被成功消费，此消息将被发送到死信队列。

  分布式消息服务RocketMQ版的重试机制如[表1](#hrm-pd-001__table16984253511)所示。

  **表1** 消息重试机制

  | 消费类型 | 重试时间间隔 | 最大重试次数 |
  | --- | --- | --- |
  | 顺序消费 | 通过**suspendTimeMillis**设置重试时间间隔。  默认值为1000ms，即1s。 | 通过消费者的**setMaxReconsumeTimes**函数配置最大重试次数。若未设置参数值，默认为无限重试。 |
  | 普通消费 | 重试时间间隔根据重试次数阶梯变化，如[表2](#hrm-pd-001__table3229119104411)所示。 | 创建消费组时设置。  取值范围：1-16。 |

  **表2** 普通消费重试时间间隔

  | 重试次数 | 与上次的间隔时间 | 重试次数 | 与上次的间隔时间 |
  | --- | --- | --- | --- |
  | 1 | 10s | 9 | 7min |
  | 2 | 30s | 10 | 8min |
  | 3 | 1min | 11 | 9min |
  | 4 | 2min | 12 | 10min |
  | 5 | 3min | 13 | 20min |
  | 6 | 4min | 14 | 30min |
  | 7 | 5min | 15 | 1h |
  | 8 | 6min | 16 | 2h |
* 延时消息：生产者生产消息到分布式消息服务RocketMQ版后，消息不会立即被消费，而是延迟**固定时间**后才会发送给消费者进行消费。生产者可以指定18个延时等级，每个延时等级对应的时间如[表3](#hrm-pd-001__table6746133810237)所示。

  **表3** 延时等级

  | 延时等级 | 延时时间 | 延时等级 | 延时时间 |
  | --- | --- | --- | --- |
  | 1 | 1s | 10 | 6min |
  | 2 | 5s | 11 | 7min |
  | 3 | 10s | 12 | 8min |
  | 4 | 30s | 13 | 9min |
  | 5 | 1min | 14 | 10min |
  | 6 | 2min | 15 | 20min |
  | 7 | 3min | 16 | 30min |
  | 8 | 4min | 17 | 1h |
  | 9 | 5min | 18 | 2h |
* 定时消息：生产者生产消息到分布式消息服务RocketMQ版后，消息不会立即被消费，而是延迟到设定的时间点后才会发送给消费者进行消费。分布式消息服务RocketMQ版支持**任意时间**的定时消息，4.8.0版本的最大推迟时间为1年，5.x版本的最大推迟时间为7天。同时也支持定时消息的取消。

  ![](https://support.huaweicloud.com/productdesc-hrm/public_sys-resources/note_3.0-zh-cn.png) 

  2022年3月30日及以后购买的实例支持定时消息功能，在此之前购买的实例不支持此功能。

#### 介绍视频

本视频介绍什么是分布式消息服务。

[![](https://support.huaweicloud.com/productdesc-hrm/zh-cn_image_0000002356561541.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/support/kafka-video/DMSIntroduction.mp4)

####
