---
title: "MetaTown数字资产管理解决方案"
source_url: https://www.huaweicloud.com/solution/implementations/build-a-digital-assets-platform-based-on-metatown.html
collected_at: 2026-02-05
---

- [解决方案实践](https://www.huaweicloud.com/solution/implementations/index.html)
- MetaTown数字资产管理

# MetaTown数字资产管理解决方案

# MetaTown数字资产管理解决方案

[查看部署指南](https://support.huaweicloud.com/bdapbmt-ctf/bdapbmt_01.html)
[方案咨询](https://www.huaweicloud.com/consultation/?type=build-a-digital-assets-platform-based-on-metatown)

### 方案架构

该解决方案基于华为云服务构建，数字资产链 DAC提供底层区块链技术，弹性云服务器部署平台业务，云数据库提供平台数据存储能力，快速帮助用户在华为云上部署自己的数字资产管理平台。

![](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/SAC1201/MetaTown.png)

MetaTown数字资产管理解决方案

版本：1.0.0﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿

上次更新日期：2023年9月

来源：由华为云构建

部署：预计20分钟

卸载：预计10分钟

**[预估花费 ◥](https://support.huaweicloud.com/bdapbmt-ctf/bdapbmt_02.html)**

**[查看源代码 ◥](https://gitee.com/HuaweiCloudDeveloper/huaweicloud-solution-build-a-digital-assets-platform-based-on-meta-town)**

[查看部署指南](https://support.huaweicloud.com/bdapbmt-ctf/bdapbmt_01.html)

[一键部署](https://console.huaweicloud.com/rf/?region=cn-north-4#/console/stack/stackCreate?templateUrl=https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/build-a-digital-assets-platform-based-on-MetaTown/build-a-digital-assets-platform-based-on-MetaTown.tf.json&stackName=build-a-digital-assets-platform-based-on-MetaTown&stackDescription=基于MetaTown构建数字资产平台)

**架构描述**

该方案会部署如下资源：

1. 创建两台弹性云服务器 ECS，用于部署MetaTown平台的前端和后端服务。

2. 创建弹性公网IP EIP，并绑定到前端节点，提供MetaTown平台被公网访问能力。

3. 创建[分布式缓存服务 Redis](https://www.huaweicloud.com/product/dcs.html)，提供缓存能力，加速用户端访问速度，提升用户体验。

4. 创建[云数据库 RDS](https://www.huaweicloud.com/product/mysql.html)，用于存储MetaTown平台的业务数据。

5. 数字资产链 DAC，提供数字资产的铸造、发行、流转、确权等全生命周期管理。

6. 通过[对象存储服务 OBS](https://www.huaweicloud.com/product/obs.html)，存储数字内容（图片）原文件，用于铸造数字资产。

**架构描述**

该方案会部署如下资源：

1. 创建两台弹性云服务器 ECS，用于部署MetaTown平台的前端和后端服务。

2. 创建弹性公网IP EIP，并绑定到前端节点，提供MetaTown平台被公网访问能力。

3. 创建[分布式缓存服务 Redis](https://www.huaweicloud.com/product/dcs.html)，提供缓存能力，加速用户端访问速度，提升用户体验。

4. 创建[云数据库 RDS](https://www.huaweicloud.com/product/mysql.html)，用于存储MetaTown平台的业务数据。

5. [数字资产链 DAC](https://www.huaweicloud.com/product/bcs/dac.html)，提供数字资产的铸造、发行、流转、确权等全生命周期管理。

6. 通过[对象存储服务 OBS](https://www.huaweicloud.com/product/obs.html)，存储数字内容（图片）原文件，用于铸造数字资产。

展开内容

收起内容

### 方案优势

### 高性能

华为云数字资产链 DAC支持五万次/秒并发链上数字资产创建，支持百亿级数字资产发行流转。
### 一键部署

该解决方案支持一键部署，用户可以基于官方示例模板，快速构建MetaTown数字资产平台。
### 开源和定制化

该解决方案是开源的，用户可以免费用于商业用途，并且还可以在源码基础上进行定制化开发。
