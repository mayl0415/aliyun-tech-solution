---
title: "基于开源Odoo快速部署ERP系统"
source_url: https://www.huaweicloud.com/solution/implementations/build-an-erp-based-on-odoo.html
collected_at: 2026-02-05
---

- [解决方案实践](https://www.huaweicloud.com/solution/implementations/index.html)
- 基于开源Odoo快速部署ERP系统

# 基于开源Odoo快速部署ERP系统

# 基于开源Odoo快速部署ERP系统

[查看部署指南](https://support.huaweicloud.com/berpbo-ctf/berpbo_01.html)
[方案咨询](https://www.huaweicloud.com/consultation/?type=build-an-ERP-based-on-odoo)

### 方案架构

该方案可以帮助您快速在华为云弹性云服务器 ECS上基于开源Odoo构建ERP系统。

![](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/SAC/2023/1230/build-an-erp-based-on-odoo_1.png)

**基于开源Odoo快速部署ERP系统**

版本：2.0.0﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿

上次更新日期：2024年1月

来源：由华为云构建

部署：预计20分钟

卸载：预计5分钟

**[预估成本 ◥](https://support.huaweicloud.com/berpbo-ctf/berpbo_02.html)**

**[查看源代码 ◥](https://gitee.com/HuaweiCloudDeveloper/huaweicloud-solution-build-an-erp-based-on-odoo)**

数据中心：

华北-北京四
华南-广州
华东-上海一

[查看部署指南](https://support.huaweicloud.com/berpbo-ctf/berpbo_01.html)
[一键部署（单机版）](https://console.huaweicloud.com/rf/?region=cn-north-4&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/build-an-ERP-based-on-odoo/build-an-ERP-based-on-odoo.tf.json&stackName=build-an-ERP-based-on-odoo&stackDescription=基于开源Odoo快速部署ERP系统)
[一键部署（高可用版）](https://console.huaweicloud.com/rf/?region=cn-north-4&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/build-an-ERP-based-on-odoo/build-a-ha-ERP-based-on-odoo.tf.json&stackName=build-a-ha-ERP-based-on-odoo&stackDescription=基于开源Odoo快速部署高可用ERP系统)

[查看部署指南](https://support.huaweicloud.com/berpbo-ctf/berpbo_01.html)
[一键部署（单机版）](https://console.huaweicloud.com/rf/?region=cn-south-1&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-2.obs.cn-south-1.myhuaweicloud.com/solution-as-code-moudle/build-an-ERP-based-on-odoo/build-an-ERP-based-on-odoo.tf.json&stackName=build-an-ERP-based-on-odoo&stackDescription=基于开源Odoo快速部署ERP系统)

[查看部署指南](https://support.huaweicloud.com/berpbo-ctf/berpbo_01.html)
[一键部署（单机版）](https://console.huaweicloud.com/rf/?region=cn-east-3&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-3.obs.cn-east-3.myhuaweicloud.com/solution-as-code-moudle/build-an-erp-based-on-odoo/build-an-ERP-based-on-odoo.tf.json&stackName=build-an-ERP-based-on-odoo&stackDescription=基于开源Odoo快速部署ERP系统)

**架构描述**

该解决方案将会部署如下资源：

1. 创建三个[弹性公网IP EIP](https://www.huaweicloud.com/product/eip.html)，用于提供访问公网和被公网访问的能力；

2. 创建两台[弹性云服务器 ECS](https://www.huaweicloud.com/product/ecs.html)，分别绑定弹性公网IP，跨可用区部署，用于部署开源Odoo软件；

3. 部署一个[弹性负载均衡 ELB](https://www.huaweicloud.com/product/elb.html)，绑定弹性公网IP，用于业务流量跨可用区进行分发；

4. 创建一个[云数据库 RDS for PostgreSQL](https://www.huaweicloud.com/product/pg.html)实例(主备)，提供业务数据读写的故障容灾能力；

5. 创建[分布式缓存服务Redis版](https://www.huaweicloud.com/product/dcs.html)（主备），为用户提供高性能、低成本数据库，同时数据流转过程中数据的一致性；

6. 创建一个[弹性文件服务 SFS](https://www.huaweicloud.com/product/sfs.html) Turbo，为Odoo高可用环境提供共享文件存储服务。

**架构描述**

该解决方案将会部署如下资源：

1. 创建三个[弹性公网IP EIP](https://www.huaweicloud.com/product/eip.html)，用于提供访问公网和被公网访问的能力；

2. 创建两台[弹性云服务器 ECS](https://www.huaweicloud.com/product/ecs.html)，分别绑定弹性公网IP，跨可用区部署，用于部署开源Odoo软件；

3. 部署一个[弹性负载均衡 ELB](https://www.huaweicloud.com/product/elb.html)，绑定弹性公网IP，用于业务流量跨可用区进行分发；

4. 创建一个[云数据库 RDS for PostgreSQL](https://www.huaweicloud.com/product/pg.html)实例(主备)，提供业务数据读写的故障容灾能力；

5. 创建[分布式缓存服务Redis版](https://www.huaweicloud.com/product/dcs.html)（主备），为用户提供高性能、低成本数据库，同时数据流转过程中数据的一致性；

6. 创建一个[弹性文件服务 SFS](https://www.huaweicloud.com/product/sfs.html) Turbo，为Odoo高可用环境提供共享文件存储服务。

展开内容

收起内容

### 方案优势

### 负载均衡

弹性负载均衡 ELB支持将业务流量跨可用区进行分发，保障业务实时在线，使流量分发更均衡。
### 高可用

弹性云服务器 ECS跨可用区部署，部署云数据库RDS服务实例（主备），具备故障容灾的能力。
### 一键部署

一键轻松部署，即可完成云资源的创建，和构建基于Odoo的ERP系统。
