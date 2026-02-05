---
title: "什么是微服务引擎"
code: "cse"
category: "应用中间件"
source_url: "https://support.huaweicloud.com/productdesc-cse/cse_productdesc_0001.html"
crawled_at: "2026-02-05T16:32:11.954489"
---

# 什么是微服务引擎

## 产品简介

微服务应用快速注册发现、配置管理及治理

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-cse/zh-cn_image_0000002218174110.png)

## 详细说明

# 什么是微服务引擎

微服务引擎（Cloud Service Engine，简称CSE）是微服务应用的云中间件，为用户提供应用网关、注册发现、配置管理、服务治理等高性能和高韧性的企业级云服务；无缝兼容SpringCloud、ServiceComb、Dubbo等开源生态；用户可结合其他云服务，快速构建云原生微服务体系，实现微服务应用的快速开发与高可用运维。

产品全景图如下所示：

![](https://support.huaweicloud.com/productdesc-cse/zh-cn_image_0000002218174110.png)

其中特性优势：

1. 开源社区主流技术全兼容。
   * 支持SpringCloud、Dubbo等开源框架 。
   * 零代码修改即可接入CSE。
   * 支持开源主流注册配置中心。
2. 云原生的融合应用网关。
   * 提供基于Envoy的高性能应用网关，替换Spring Cloud Gateway、Zuul。
   * 支持热加载变更配置不中断业务请求。
   * 实现Ingress、微服务网关、安全网关合一。
3. 统一服务治理平台。
   * 支持多框架、多技术栈、多语言应用。
   * 互通互访、统一治理、平滑演进。

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-cse/zh-cn_image_0000002296344070.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/support/cse-video/1748396842198234875.mp4)

#### 应用网关

CSE应用网关基于开源社区版Envoy，提供Ingress网关和微服务网关二合一的云原生网关服务。使用华为云CSE应用网关可以获得微服务架构或容器化应用的极简网关体验，快速对接服务发现、实现服务路由、安全控制、流量治理等功能，让用户专注于业务应用的开发与维护。CSE应用网关的可观测能力，与华为云AOM、APM、LTS等服务预集成，提供监控告警、调用链路分析、访问日志查询等功能。

#### 注册配置中心Nacos引擎

CSE注册配置中心Nacos兼容开源Nacos、Eureka客户端，具备注册发现、动态配置管理、访问权限控制、可观测等能力。可打造高可用、易管理的微服务中间件。

#### ServiceComb引擎

CSE ServiceComb引擎基于Apache ServiceComb开源生态，提供一站式的微服务平台。支持使用Java-Chassis SDK、SpringCloudHuawei SDK或无侵入的Sermant Java Agent（支持标准SpringCloud和Dubbo框架）接入。接入后，用户可以轻松使用服务契约、服务治理、灰度发布、业务场景治理、服务监控、配置管理、访问控制等众多功能，实践api first开发，构建高安全、高性能、高稳定的微服务应用。关于Apache ServiceComb Service Center的详细内容请参考：

* <https://github.com/apache/servicecomb-service-center/>
* <https://service-center.readthedocs.io/en/latest/user-guides.html>

ServiceComb引擎分为1.x、2.x版本。

ServiceComb引擎2.x版本是可支持大规模微服务应用管理的商用引擎。您可根据业务需要选择不同规格；引擎资源独享，性能不受其他租户影响。

相较于ServiceComb引擎1.x版本，ServiceComb引擎2.x版本底层架构、功能、安全及性能全面升级，提供了独立的服务注册发现中心和配置中心，支持基于用户业务场景的定义和治理。两个版本的特性比对请参见[表1](#cse_productdesc_0001__table18740654153218)。

**表1** ServiceComb引擎2.x和ServiceComb引擎1.x特性比对

| 功能 | 特性 | | 2.x | 1.x | 备注 |
| --- | --- | --- | --- | --- | --- |
| 引擎管理 | 安全性 | 支持安全认证 | √ | √ | - |
| 可靠性 | 3AZ高可靠 | √ | √ | - |
| 微服务管理 | 基础能力 | 注册发现 | √ | √ | - |
| 多框架接入 | √ | √ | 支持Spring Cloud、ServiceComb Java Chassis。 |
| 无实例版本自动清理 | √ | x | 2.3.7及以后版本，支持保留最近3个微服务版本，并自动清理无实例版本。 |
| 性能 | 实例变化毫秒级推送 | √ | √ | - |
| 配置管理 | 基础能力 | 管理配置 | √ | √ | - |
| 配置格式多样化 | √ | 仅支持文本 | 2.x新增支持配置格式有：YAML、JSON、TEXT、Properties、INI、XML。 |
| 导入导出 | √ | √ | 2.x新增支持设置导入相同配置策略。 |
| 高级特性 | 历史版本 | √ | x | - |
| 版本对比 | √ | x | - |
| 一键回滚 | √ | x | - |
| 配置标签 | √ | x | - |
| 性能 | 秒级下发 | √ | x | - |
| 微服务治理 | 业务场景化治理 | 业务场景定义 | √ | x | - |
| 基于请求Method的匹配规则 | √ | x | - |
| 基于请求Path的匹配规则 | √ | x | - |
| 基于请求Headers的匹配规则 | √ | x | - |
| 治理策略-流量控制 | 服务端的令牌桶限流 | √ | √ | - |
| 治理策略-重试 | 客户端通过重试来保证用户业务的可用性、容错性、一致性 | √ | √ | - |
| 治理策略-熔断 | 服务端通过熔断故障业务，防止故障蔓延到整个服务，发生大规模故障 | √ | √ | - |
| 治理策略-隔离仓 | 服务端基于信号量控制请求并发能力 | √ | x | - |
| 开发工具 | 本地轻量化引擎 | 本地一键启动，方便开发者离线开发微服务 | √ | √ | - |

####
