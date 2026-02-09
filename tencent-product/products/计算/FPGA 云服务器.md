---
title: "FPGA 云服务器"
url: https://cloud.tencent.com/product/fpga
category: "计算"
crawled_at: 2026-02-06T17:13:54.504131
---

# FPGA 云服务器

FPGA 云服务器提供FPGA开发和使用工具及环境，让用户轻松获取并
部署FPGA计算实例，专注于FPGA硬件加速应用开发，为您提供易用、可重构、经济、安全的FPGA云服务。

![](https://qcloudimg.tencent-cloud.cn/raw/80fc4542823b4988527d72544f07696f.png)

### 弹性计算

在腾讯云上您可以在几分钟之内快速增加或删减云服务器数量，以满足快速变化的业务需求。通过定义相关策略，您可以确保所使用的 CVM 实例数量在需求高峰期无缝扩展，保证程序的可用性；在需求平淡期自动回落，以节省成本。

![](https://qcloudimg.tencent-cloud.cn/raw/95f060d86981478ecc9e8855d59e02a7.png)

### 极致性能

FPGA 云服务器通过专用的 PCI Express (PCIe) 结构连接到您的 FPGA 实例，透传 FPGA 性能，极致发挥 FPGA 性能；与仅使用 CPU 的服务器相比，您可以使用 FPGA 硬件降低应用程序的处理延时，提高处理能力。

![](https://qcloudimg.tencent-cloud.cn/raw/c87226ce8698e17c6ea4854118f38daa.png)

### 快速部署

与云服务器 CVM、负载均衡 CLB、对象存储 COS 等多种云产品无缝接入，内网流量免费；采用与云服务器 CVM 一致的管理方式，提供 FPGA 硬件开发环境，降低学习成本，简单易用。

![](https://qcloudimg.tencent-cloud.cn/raw/0fd65818098b9b0f8c71f193fbe8fbbe.png)

### 可靠的交易平台

腾讯云提供统一的 FPGA 服务市场，知识产权开发者可以通过腾讯云服务市场为其他客户无偿或有偿地提供用于开发设计的 FPGA 应用程序；应用程序开发者可通过服务市场免费或付费地使用 FPGA 服务。

![](https://qcloudimg.tencent-cloud.cn/raw/8af2ba5f563beb778d217653cea99d96.png)

### 全面防护

不同用户、账户、实例间全面资源隔离，保证 FPGA 访问的独立与安全性，数据安全有保障；与云安全无缝对接，享有与云服务器同等的云安全基础防护和高防服务。

![](https://qcloudimg.tencent-cloud.cn/raw/ad55832a560700e4f92670dea9008cce.png)

### 节约成本

您可按需购买，无需投入大量资金购置物理服务器；将 FPGA 部署开发时间从数年或数月缩减到数天；避免本地数据中心开发 FPGA 无差别的繁重工作，助您有效降低基础设施建设人力和成本投入。

- 图像分类、检测
- 实时图像压缩

实时图像压缩

常用的图片格式有 JPEG 格式、WEBP 格式等， WEBP 图片格式比 JPEG 图片格式存储空间小 30% 。为节省
存储空间，降低传输流量，提升用户的图片下载体验，通常采用 WEBP 格式进行存储及传输分发。但 WEBP
压缩计算复杂度是 JPEG 压缩的10倍以上，采用 CPU 进行 WEBP 转码成本很高。

我们的优势

- 我们使用 FX4 FPGA 云服务器对JPEG 格式图片转成 WEBP 格式图片进行加速计算。在实际测试中，测试图片 大小为 853x640，在不影响图片图片质量的前提下，FX4 FPGA 云服务器处理延时相比 CPU 服务器降低 20 倍， FPGA 云服务器处理性能是 CPU 服务器的 6 倍。实际测试表明且不会影响视图片质量。

![](https://qcloudimg.tencent-cloud.cn/raw/f1c31cd2f751d6eebf194260ee817333.png)

- 一般常见问题
- 开发相关

### 我是 FPGA 开发人员，如何开始使用 FPGA 实例？

我们稍后将会通过提供 framework，该 framework 可以支持 C/C++、OpenCL、Verilog/VHDL 开发语言，FPGA 开发人员可以选择自己熟悉的语言方式进行 FPGA 逻辑设计。

### 我是否可以向任何云服务器 CVM 实例类型中添加 FPGA？

更多问题请查看 [常见问题](https://cloud.tencent.com/document/faq)，也可在 [问答社区](https://cloud.tencent.com/developer/ask) 中进行提问 。

按照我们的 入门指南 ，只需点几次鼠标，即可创建您的首个腾讯云 CVM 实例。

