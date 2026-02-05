---
title: "什么是FunctionGraph"
code: "functiongraph"
category: "计算"
source_url: "https://support.huaweicloud.com/productdesc-functiongraph/functiongraph_01_0100.html"
crawled_at: "2026-02-05T16:27:16.960816"
---

# 什么是FunctionGraph

## 产品简介

自动运行代码，无需配置或管理服务器

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-functiongraph/zh-cn_image_0000001212740388.png)

## 详细说明

# 什么是FunctionGraph

FunctionGraph是一项基于事件驱动的函数托管计算服务。使用FunctionGraph函数，只需编写业务函数代码并设置运行的条件，无需配置和管理服务器等基础设施，函数以弹性、免运维、高可靠的方式运行。此外，按函数实际执行资源计费，不执行不产生费用。

函数使用流程如[图1](#functiongraph_01_0100__fig4953173820317)所示。

**图1** 函数使用流程
  
![](https://support.huaweicloud.com/productdesc-functiongraph/zh-cn_image_0000001212740388.png "点击放大")

#### 功能简介

**①编写代码**

用户编写业务代码，目前支持Node.js、Python、Java、Go、C#、PHP和定制运行时语言，详情请参考[开发指南](https://support.huaweicloud.com/devg-functiongraph/functiongraph_02_0101.html)。

**②上传代码**

目前支持在线编辑、上传ZIP或JAR包，从OBS引用ZIP包等，详情请参考[代码上传方式说明](https://support.huaweicloud.com/productdesc-functiongraph/functiongraph_01_0200.html#functiongraph_01_0200__table35034283164337)。

**③API和云产品事件源触发函数执行**

通过RESTful API或者云产品事件源触发函数执行，生成函数实例，实现业务功能，详情请参考[函数触发器](https://support.huaweicloud.com/productdesc-functiongraph/functiongraph_01_0200.html#functiongraph_01_0200__section327204091911)。

**④弹性执行**

函数在执行过程中，会根据请求量弹性扩容，支持请求峰值的执行，此过程用户无需配置，由FunctionGraph完成，并发数限制请参考[约束与限制](https://support.huaweicloud.com/productdesc-functiongraph/functiongraph_01_0150.html)。

**⑤查看日志**

FunctionGraph函数实现了与云日志服务LTS的对接，可查看函数运行日志信息，详情请参考[日志和监控](https://support.huaweicloud.com/productdesc-functiongraph/functiongraph_01_0200.html#functiongraph_01_0200__section382816599214)。

**⑥查看监控**

FunctionGraph函数实现了与应用运维管理服务AOM的对接，可查看图形化的函数监控信息，详情请参考[日志和监控](https://support.huaweicloud.com/productdesc-functiongraph/functiongraph_01_0200.html#functiongraph_01_0200__section382816599214)。

**⑦计费方式**

函数执行结束后，根据函数请求执行次数和执行时间计费，详情请参考[函数工作流计费概述](https://support.huaweicloud.com/price-functiongraph/functiongraph_00_0001.html)。

####
