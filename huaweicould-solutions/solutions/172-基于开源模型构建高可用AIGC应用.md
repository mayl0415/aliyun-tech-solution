---
title: "基于开源模型构建高可用AIGC应用"
source_url: https://www.huaweicloud.com/solution/implementations/building-high-availability-aigc-applications-with-stable-diffusion.html
collected_at: 2026-02-05
---

- [解决方案实践](https://www.huaweicloud.com/solution/implementations/index.html)
- 基于开源模型构建高可用AIGC应用

# 基于开源模型构建高可用AIGC应用

# 基于开源模型构建高可用AIGC应用

[查看部署指南](https://support.huaweicloud.com/bhaaigcasd-aislt/bhaaigcasd_01.html)
[方案咨询](https://www.huaweicloud.com/consultation/?type=building-high-availability-aigc-applications-with-stable-diffusion)

### 方案架构

该解决方案在华为云弹性云服务器 ECS上基于开源Stable Diffusion一键部署构建AIGC应用。

![](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/SAC/2022/building-high-availability-aigc-applications-with-stable-diffusion.png)

**基于开源模型构建高可用AIGC应用**

版本：1.2.0﻿

上次更新日期：2023年11月

来源：由华为云构建

部署：预计30分钟

卸载：预计10分钟

**[预估成本 ◥](https://support.huaweicloud.com/bhaaigcasd-aislt/bhaaigcasd_02.html)**

**[查看源代码 ◥](https://gitee.com/HuaweiCloudDeveloper/huaweicloud-solution-building-high-availability-aigc-applications-with-stable-diffusion)**

数据中心：

亚太-新加坡
华北-北京四
华东-上海一

[查看部署指南](https://support.huaweicloud.com/bhaaigcasd-aislt/bhaaigcasd_01.html)
[一键部署](https://console.huaweicloud.com/rf/?locale=zh-cn&region=ap-southeast-3#/console/stack/stackCreate?templateUrl=https://documentation-samples-4.obs.ap-southeast-3.myhuaweicloud.com/solution-as-code-moudle/building-high-availability-aigc-applications-with-stable-diffusion/building-high-availability-aigc-applications-with-stable-diffusion.tf.json&stackName=building-high-availability-aigc-applications-with-stable-diffusion&stackDescription=基于开源模型构建高可用AIGC应用)

[查看部署指南](https://support.huaweicloud.com/bhaaigcasd-aislt/bhaaigcasd_01.html)
[一键部署](https://console.huaweicloud.com/rf/?region=cn-north-4#/console/stack/stackCreate?templateUrl=https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/building-high-availability-aigc-applications-with-stable-diffusion/building-high-availability-aigc-applications-with-stable-diffusion.tf.json&stackName=building-high-availability-aigc-applications-with-stable-diffusion&stackDescription=基于开源模型构建高可用AIGC应用)

[查看部署指南](https://support.huaweicloud.com/bhaaigcasd-aislt/bhaaigcasd_01.html)
[一键部署](https://console.huaweicloud.com/rf/?region=cn-east-3#/console/stack/stackCreate?templateUrl=https://documentation-samples-3.obs.cn-east-3.myhuaweicloud.com/solution-as-code-moudle/building-high-availability-aigc-applications-with-stable-diffusion/building-high-availability-aigc-applications-with-stable-diffusion.tf.json&stackName=building-high-availability-aigc-applications-with-stable-diffusion&stackDescription=基于开源模型构建高可用AIGC应用)

**架构描述**

该解决方案会部署如下资源：

1. 创建两台Linux GPU加速型[弹性云服务器 ECS](https://www.huaweicloud.com/product/ecs.html)，用于搭建AIGC应用系统。

2. 创建三个[弹性公网IP EIP](https://www.huaweicloud.com/product/eip.html)，分别绑定到两个到服务器及弹性负载均衡 ELB，用于提供访问公网和被公网访问能力。

3. 部署一个[弹性负载均衡 ELB](https://www.huaweicloud.com/product/elb.html)，用于业务流量跨可用区进行分发。

4. 创建安全组，通过配置安全组规则，为弹性云服务器 ECS提供安全防护。

5. 创建一个[对象存储服务 OBS](https://www.huaweicloud.com/product/obs.html)桶，用于保存生成的图片文件。

6. 在两台Linux弹性云服务器 ECS上分别完成Stable Diffusion WebUI应用、inotify-tools工具安装，以及对象存储服务 OBS obsutil工具安装，用于自动上传备份在页面上保存的图片。

**架构描述**

该解决方案会部署如下资源：

1. 创建两台Linux GPU加速型[弹性云服务器 ECS](https://www.huaweicloud.com/product/ecs.html)，用于搭建AIGC应用系统。

2. 创建三个[弹性公网IP EIP](https://www.huaweicloud.com/product/eip.html)，分别绑定到两个到服务器及弹性负载均衡 ELB，用于提供访问公网和被公网访问能力。

3. 部署一个[弹性负载均衡 ELB](https://www.huaweicloud.com/product/elb.html)，用于业务流量跨可用区进行分发。

4. 创建安全组，通过配置安全组规则，为弹性云服务器 ECS提供安全防护。

5. 创建一个[对象存储服务 OBS桶](https://www.huaweicloud.com/product/obs.html)，用于保存生成的图片文件。

6. 在两台Linux弹性云服务器 ECS上分别完成Stable Diffusion WebUI应用、inotify-tools工具安装，以及对象存储服务 OBS obsutil工具安装，用于自动上传备份在页面上保存的图片。

展开内容

收起内容

### 方案优势

### 高可用

弹性云服务器 ECS跨可用区部署，提供多可用区容灾能力，够快速自动完成故障切换。
### 开源和定制化

该解决方案是开源的，用户可以免费用于商业用途，并且还可以在源码基础上进行定制化开发。
### 一键部署

一键轻松部署，即可实现基于Stable Diffusion的AIGC应用系统搭建。
