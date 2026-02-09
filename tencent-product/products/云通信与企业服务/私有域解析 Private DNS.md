---
title: "私有域解析 Private DNS"
url: https://cloud.tencent.com/product/privatedns
category: "云通信与企业服务"
crawled_at: 2026-02-09T11:12:26.249562
---

# 私有域解析 Private DNS

私有域解析 Private DNS 是基于腾讯云私有网络 VPC （Virtual Private Cloud）环境的私有域名解析管理服务。通过它，您可以在自定义的一个或多个私有网络中快速构建DNS系统，并能够方便地使用私有域名记录来管理 VPC 关联的 CVM、CLB、CDN、COS 等腾讯云自有资源，而这些私有域名在 VPC 之外将无法访问。

- [优惠活动私有域解析全民限时免费额度包上线](https://cloud.tencent.com/document/product/1338/55665)
- [产品公告私有域解析全新地域上线](https://cloud.tencent.com/document/product/1338/50529)
- [产品公告私有域解析 API 3.0 正式开放](https://cloud.tencent.com/document/product/1338/55955)

### 灵活配置

通过私有域解析 Private DNS ，您可以根据需要自定义创建私有域。域名无需公网注册，支持一键备注，标签管理，灵活配置更便捷。

### 反向解析

通过创建指定后缀私有域并设置 PTR 记录，将 IP 映射至域名实现反向解析，通过反向解析可以降低垃圾邮件数量，IP 用途一目了然。

### 负载均衡

支持 CNAME、A、AAAA、TXT 多记录类型负载均衡，支持“随机应答”、“权重轮询”模式，通过设置记录值和权重，将客户端的请求分配到各个服务端。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/-X2yGAEyUryLQnaldZkqN.png)

### 请求量统计

支持按照地域、VPC、域名维度筛选查看请求量统计，实例消耗一手掌握。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/y3QBnAYgwQiKAeqay2sMO.png)

### 子域名递归解析

通过开启「子域名递归查询」，实现当私有网络环境下域名查询未匹配时，转向公网递归查询。

### 安全稳定

基于 DNSPod 十余年行业领先的 DNS 基础架构，并依托腾讯云私有网络 VPC ，提供安全、稳定、高可用的私有域名解析能力。

### 产品使用原理

用户于私有网络环境下创建私有域 example.com ，并添加「 www 主机记录 - CNAME 记录 - domain.com 记录值」解析记录，此时客户端发起查询 CNAME 记录，由于已配置记录，此时返回结果为 domain.com；查询「test.domain.com」A 记录，由于未配置因而返回 SOA。

用户于私有网环境下创建私有域 example.com，开启子域名递归解析，添加「www 主机记录- A 记录 - 8.8.8.8 记录值」解析记录，该域名于公网权威 DNS 配置记录值为 119.29.29.29 ；此时客户端发起请求查询 A 记录，此时返回结果为「8.8.8.8」；如删除私有域该条记录，则返回「119.29.29.29」。

![](https://qcloudimg.tencent-cloud.cn/raw/e64bbb31a6b69e1dd379ddf2e522a67e.svg)

2020

- 09月

  09-20

  09-20

  已发布

  新品上线

2021

- 03月

  03-31

  03-31

  已发布

- 03月

  03-31

  03-31

  已发布

- 05月

  05-11

  05-11

  已发布

  全民限时免费额度包上线

  私有域解析 Private DNS 上线免费额度，私有域解析 Private DNS 将按腾讯云实名认证类型、私有域数量和解析请求额度为您提供对应的免费资源。有效期为 2021年05月11日 至 2022年05月11日。

- 05月

  05-20

  05-20

  已发布

  API 正式开放

  私有域解析 Private DNS API3.0 正式开放，支持使用腾讯云 API3.0 规范调用私有域解析 Private DNS 产品服务。

- 05月

  05-20

  05-20

  已发布

  新增地域支持

  私有域解析 Private DNS 全新地域上线，新增南京、香港、新加坡、法兰克福、雅加达地域支持。

- 07月

  07-09

  07-09

  已发布

  新增地域支持

  私有域解析 Private DNS 全新地域上线，新增3大金融区（北京金融区、上海金融区、深圳金融区）。

2023

- 02月

  02-02

  2023-02-02

  已发布

  支持自定义非标TLD

  支持添加非标 TLD 作为 Zone，实现云上自定义 Hostname

- 02月

  02-02

  2023-02-02

  已发布

  新增CNAME加速特性

  新增CNAME混合加速功能，解决内网域名多映射关系的层级查询

- 02月

  02-02

  2023-02-02

  已发布

  新增上海自动驾驶专区

  新增上海自动驾驶专区，完成中国站全地域覆盖

2024

- 12月

  12-02

  2024-12-02

  内测中

  Private DNS 云上转发至云下已开启公测

  功能介绍：支持将云上的解析请求转发至云下，用户可在云上访问到云下idc机器。

2025

- 01月

  01-09

  2025-01-09

  已发布

  私有域解析单个私有域负载均衡配额从20提升至60个

  私有域负载均衡解析记录的数量限制已从原先的20个提升至60个，用户可以创建更多的解析记录来增强负载均衡能力。

2026

- 02月09日

  02-09

[### 文档总览

提供 Private DNS 产品从了解到进阶实践的全程指导，助您更便捷地使用私有域名解析管理服务。](https://cloud.tencent.com/document/product/1338)

[### 产品简介

提供 Private DNS 产品概述、产品优势、应用场景及使用限制说明。](https://cloud.tencent.com/document/product/1338/50527)

[### 快速入门

提供 Private DNS 开通服务与功能使用等简要说明。](https://cloud.tencent.com/document/product/1338/50533)

[### 购买指南

提供 Private DNS 产品计费方式、计费规则及欠费处理等说明。](https://cloud.tencent.com/document/product/1338/50523)

[### 操作指南

提供 Private DNS 相关功能操作说明。](https://cloud.tencent.com/document/product/1338/50538)

### 自定义的私有域是否需要注册？

通过私有域解析 Private DNS 创建的私有域是仅在关联 VPC 内生效的虚拟域名，不需要在域名服务商处注册，支持自定义创建符合标准的规范域名。

### 私有域解析 Private DNS 与 DNS 解析 DNSPod 的主要区别是什么？

### 如何设置私有域反向解析？

### 如何设置私有域既支持内网解析，也支持公网解析？

### 私有域解析 Private DNS 是同区域还是跨区域？

更多问题请查看 [常见问题](https://cloud.tencent.com/document/product/1338/50526)，也可在 [问答社区](https://cloud.tencent.com/developer/ask) 中进行提问 。

按照我们的入门指南 ，快速部署您的私有域解析 Private DNS 服务。

