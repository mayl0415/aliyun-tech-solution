---
title: "什么是DDoS攻击"
code: "aad"
category: "安全与合规"
source_url: "https://support.huaweicloud.com/productdesc-aad/aad_01_0006.html"
crawled_at: "2026-02-05T16:35:46.025940"
---

# 什么是DDoS攻击

## 产品简介

配置高防IP，将攻击流量引流到高防IP

## 详细说明

# 什么是DDoS攻击

拒绝服务（Denial of Service，简称DoS）攻击也称洪水攻击，是一种网络攻击手法，其目的在于使目标电脑的网络或系统资源耗尽，服务暂时中断或停止，导致合法用户不能够访问正常网络服务的行为。当攻击者使用网络上多个被攻陷的电脑作为攻击机器向特定的目标发动DoS攻击时，称为分布式拒绝服务攻击（Distributed Denial of Service Attack，简称DDoS）。常见DDoS攻击类型如[表1](#aad_01_0006__table54061242121716)所示。

**表1** 常见DDoS攻击类型

| 攻击类型 | 说明 | 举例 |
| --- | --- | --- |
| 网络层攻击 | 通过大流量拥塞被攻击者的网络带宽，导致被攻击者的业务无法正常响应客户访问。 | NTP Flood攻击。 |
| 传输层攻击 | 通过占用服务器的连接池资源，达到拒绝服务的目的。 | SYN Flood攻击、ACK Flood攻击、ICMP Flood攻击。 |
| 会话层攻击 | 通过占用服务器的SSL会话资源，达到拒绝服务的目的。 | SSL连接攻击。 |
| 应用层攻击 | 通过占用服务器的应用处理资源，极大消耗服务器处理性能，达到拒绝服务的目的。 | HTTP Get Flood攻击、HTTP Post Flood攻击。 |

**
