---
title: "基于Slurm构建泛HPC场景云上云下资源协同解决方案"
source_url: https://www.huaweicloud.com/solution/implementations/deploy-a-scalable-hpc-cluster-with-slurm.html
collected_at: 2026-02-05
---

- [解决方案实践](https://www.huaweicloud.com/solution/implementations/index.html)
- 基于Slurm构建泛HPC场景云上云下资源协同

# 基于Slurm构建泛HPC场景云上云下资源协同解决方案

# 基于Slurm构建泛HPC场景云上云下资源协同解决方案

[查看部署指南](https://support.huaweicloud.com/dshpccs-high-tech/dshpccs_01.html)
[方案咨询](https://www.huaweicloud.com/consultation/?type=slurm)

### 方案架构

该解决方案可以帮助用户在华为云上轻松搭建可弹性扩展的Slurm集群。

![](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/SAC/2023/1130/deploy-a-scalable-hpc-cluster-with-slurm_1.jpg)

**基于Slurm构建泛HPC场景云上云下资源协同解决方案**

版本：2.0.0﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿

上次更新日期：2023年12月

来源：由华为云构建

部署：预计30分钟

卸载：预计10分钟

**[预估成本 ◥](https://support.huaweicloud.com/dshpccs-high-tech/dshpccs_02.html)**

**[查看源代码 ◥](https://gitee.com/HuaweiCloudDeveloper/huaweicloud-solution-deploy-a-scalable-hpc-cluster-with-slurm/tree/master-dev/)**

数据中心：

华东-上海一
华北-北京四

[查看部署指南](https://support.huaweicloud.com/dshpccs-high-tech/dshpccs_01.html)
[一键部署](https://console.huaweicloud.com/rf/?region=cn-east-3&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples-3.obs.cn-east-3.myhuaweicloud.com/solution-as-code-moudle/deploy-a-scalable-hpc-cluster-with-slurm/deploy-a-scalable-hpc-cluster-with-slurm.tf.json&stackName=deploy-a-scalable-hpc-cluster-with-slurm&stackDescription=基于Slurm构建泛HPC场景云上云下资源协同解决方案)

[查看部署指南](https://support.huaweicloud.com/bpwbw-ctf/bpwbw_01.html)
[一键部署](https://console.huaweicloud.com/rf/?region=cn-north-4&locale=zh-cn#/console/stack/stackCreate?templateUrl=https://documentation-samples.obs.cn-north-4.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-moudle/deploy-a-scalable-hpc-cluster-with-slurm/deploy-a-scalable-hpc-cluster-with-slurm.tf.json&stackName=deploy-a-scalable-hpc-cluster-with-slurm&stackDescription=基于Slurm构建泛HPC场景云上云下资源协同解决方案)

**架构描述**

该解决方案会部署如下资源：

1. 创建两台Linux[弹性云服务器 ECS](https://www.huaweicloud.com/product/ecs.html)，安装软件Slurm，在调度节点安装Gearbox程序、配置Java环境。

2. 创建一条[弹性公网IP EIP](https://www.huaweicloud.com/product/eip.html)，用于提供访问公网和被公网访问能力。

3. 创建安全组，可以保护弹性云服务器 ECS的网络安全，通过配置安全组规则，限定云服务器的访问端口。

4. 使用[镜像服务 IMS](https://www.huaweicloud.com/product/ims.html)，创建计算节点服务器镜像，用于弹性扩容时使用该镜像配置计算节点服务器初始化环境。

5. 使用[弹性伸缩 AS](https://www.huaweicloud.com/product/as.html)，创建一个伸缩组实例 ，通过设置弹性伸缩配置及伸缩策略来进行集群实例资源的弹性扩缩容。

6. 使用[云监控服务 CES](https://www.huaweicloud.com/product/ces.html)，Gearbox程序监测集群作业状态，计算自定义指标Workload值，上报指标到云监控服务。

7. 创建[弹性文件服务 SFS](https://www.huaweicloud.com/product/sfs.html)，挂载到所有弹性云服务器 ECS上，为集群环境提供共享文件存储服务。

**架构描述**

该解决方案会部署如下资源：

1. 创建两台Linux[弹性云服务器 ECS](https://www.huaweicloud.com/product/ecs.html)，安装软件Slurm，在调度节点安装Gearbox程序、配置Java环境。

2. 创建一条[弹性公网IP EIP](https://www.huaweicloud.com/product/eip.html)，用于提供访问公网和被公网访问能力。

3. 创建安全组，可以保护弹性云服务器 ECS的网络安全，通过配置安全组规则，限定云服务器的访问端口。

4. 使用[镜像服务 IMS](https://www.huaweicloud.com/product/ims.html)，创建计算节点服务器镜像，用于弹性扩容时使用该镜像配置计算节点服务器初始化环境。

5. 使用[弹性伸缩 AS](https://www.huaweicloud.com/product/as.html)，创建一个伸缩组实例 ，通过设置弹性伸缩配置及伸缩策略来进行集群实例资源的弹性扩缩容。

6. 使用[云监控服务 CES](https://www.huaweicloud.com/product/ces.html)，Gearbox程序监测集群作业状态，计算自定义指标Workload值，上报指标到云监控服务。

7. 创建[弹性文件服务 SFS](https://www.huaweicloud.com/product/sfs.html)，挂载到所有弹性云服务器 ECS上，为集群环境提供共享文件存储服务。

展开内容

收起内容

### 方案优势

### 动态扩缩容

该解决方案配置弹性伸缩组，服务器内置Gearbox程序，该程序可周期性监测集群指标上报云监控服务CES，由CES告警规则触发AS自动扩缩容。
### 个性定制化

该解决方案及内置Gearbox程序均为开源，用户可以免费用于商业用途，并可以在源码基础上进行定制化开发。
### 一键部署

一键轻松部署，即可完成弹性扩缩容的HPC集群环境部署。
