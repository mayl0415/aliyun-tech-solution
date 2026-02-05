---
title: "什么是应用管理与运维平台"
code: "servicestage"
category: "开发与运维"
source_url: "https://support.huaweicloud.com/productdesc-servicestage/servicestage_01_0007.html"
crawled_at: "2026-02-05T16:33:12.851581"
---

# 什么是应用管理与运维平台

## 产品简介

面向企业的一站式PaaS平台服务

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-servicestage/zh-cn_image_0000002232389429.png)

## 详细说明

# 什么是应用管理与运维平台

应用管理与运维平台（ServiceStage）是面向企业的应用管理与运维平台，提供应用发布、部署、监控与运维等一站式解决方案。支持Java、PHP、Python、Node.js、Docker、Tomcat技术栈。支持Apache ServiceComb Java Chassis（Java Chassis）、Spring Cloud等微服务应用，让企业应用上云更简单。

ServiceStage主要包含如下能力：

1. 应用管理：支持应用生命周期管理、环境管理。
2. 微服务应用接入：支持Java Chassis、Spring Cloud微服务框架。配合微服务引擎可实现服务注册发现、配置管理和服务治理，请参考[微服务开发指南](https://support.huaweicloud.com/devg-servicestage/cse_04_0001.html)。
3. 应用运维：通过日志、监控、告警支持应用运维管理。

**图1** ServiceStage产品功能
  
![](https://support.huaweicloud.com/productdesc-servicestage/zh-cn_image_0000002232389429.png "点击放大")

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-servicestage/zh-cn_image_0000002321491914.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/support/servicestage-video/productdesc-servicestage-hws.mp4)

#### 应用管理

* 应用生命周期管理

  应用完成开发后，可以托管在ServiceStage上，为您提供完整的应用生命周期管理：

  + 使用源码、软件包（Jar/War/Zip）和容器镜像进行应用组件创建，实现应用部署。
  + 应用从创建到下线的全流程管理，包括创建、部署、启动、升级、回滚、伸缩、停止和删除应用等功能。
* 环境管理

  环境是用于应用组件部署和运行的计算、网络、中间件等基础资源的集合。ServiceStage把计算资源（如云容器引擎CCE、弹性云服务器ECS等）、网络资源（如弹性负载均衡ELB、弹性公网IP等）和中间件（如分布式缓存DCS、RDS、微服务引擎CSE等）组合为一个环境，如：开发环境，测试环境，预生产环境，生产环境。

  环境内网络互通，可以按环境维度来管理资源、部署服务，减少具体基础资源运维管理的复杂性。

#### 微服务应用接入

ServiceStage微服务引擎支持主流微服务框架接入和治理，您可以灵活选择最适合的微服务技术，快速开发云应用，适应复杂多变的业务需求。

* 支持原生ServiceComb微服务框架

  使用ServiceComb框架开发的微服务，可以无缝接入微服务引擎。

  微服务引擎采用的Apache ServiceComb Service Center，是一个RESTful风格的、高可用无状态的服务注册发现中心，提供微服务发现和微服务管理功能。服务提供者可以将自身的实例信息注册到服务注册发现中心，以供服务消费者发现并使用。关于Apache ServiceComb Service Center的详细内容请参考：

  + <https://github.com/apache/servicecomb-service-center/>
  + <https://service-center.readthedocs.io/en/latest/user-guides.html>

* 兼容主流微服务开源框架

  为Spring Cloud开发的微服务提供了非常简单的接入方式，开发者只需要修改依赖关系和少量的配置，就可以接入微服务引擎，使用统一的治理能力。
* 提供微服务治理能力

  使用微服务框架开发的应用托管在ServiceStage后，启动应用实例会将微服务注册到服务注册发现中心。您可以参考[微服务治理](https://support.huaweicloud.com/usermanual-servicestage/servicestage_03_0102.html)，针对微服务进行相关的治理。

#### 应用运维

* 提供应用组件多维度的指标监控，帮助您把握应用上线后的运行状况。
* 提供界面化的日志查看、搜索能力，帮助您快速定位问题。

####
