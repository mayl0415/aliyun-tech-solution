---
title: "什么是智能边缘云"
code: "iec"
category: "CDN与智能边缘"
source_url: "https://support.huaweicloud.com/productdesc-iec/iec_01_0100.html"
crawled_at: "2026-02-05T16:29:44.033272"
---

# 什么是智能边缘云

## 产品简介

部署距用户更近的位置，提供低时延体验

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-iec/zh-cn_image_0225215964.png)

![图片2](https://support.huaweicloud.com/productdesc-iec/zh-cn_image_0225250300.png)

![图片3](https://support.huaweicloud.com/productdesc-iec/zh-cn_image_0244413346.png)

![图片4](https://support.huaweicloud.com/productdesc-iec/zh-cn_image_0225299740.png)

![图片5](https://support.huaweicloud.com/productdesc-iec/zh-cn_image_0225332230.png)

## 详细说明

# 什么是智能边缘云

#### 边缘计算

迈入5G和AI时代，新型业务如增强现实AR、虚拟现实VR、互动直播、自动驾驶、智能制造等应运而生。以上这些业务场景对时延和网络带宽有着强烈诉求，而在传统的集中式云计算场景中，所有数据都集中存储在大型数据中心。由于地理位置和网络传输的限制，无法满足新型业务的低时延、高带宽等要求。

* 网络高时延：传统云计算无法即时处理和分析新型业务产生的数据，导致应用终端获得的响应慢，体验差。
* 带宽高成本：新型业务的应用终端产生的数据传回云端将消耗更高的网络带宽，导致服务厂商需要支付高昂的网络成本。
* 数据合规性：新型业务数据存储在云端，无法满足企业对敏感数据本地化存储的要求，直接影响企业数据上云的策略。

面对传统集中式云计算的固有局限性，边缘计算成为应对新型业务和数据合规业务的较好选择。边缘计算通过在靠近终端应用的位置建立站点，最大限度的将集中式云计算的能力延伸到边缘侧，有效解决以上的时延和带宽问题。

您可以参考[图1](#iec_01_0100__fig15619657111913)了解更多关于云计算和边缘计算的区别。

**图1** 云计算和边缘计算
  
![](https://support.huaweicloud.com/productdesc-iec/zh-cn_image_0225215964.png "点击放大")

从广义上讲，云计算包括边缘计算，边缘计算是云计算的扩展，二者为互补而非替代关系。只有云计算与边缘计算相互协同（简称边云协同），才能更好的满足各种应用场景下的不同需求。

通过[图2](#iec_01_0100__fig14441324155218)进一步了解边缘计算的范畴。

**图2** 边缘计算的范畴
  
![](https://support.huaweicloud.com/productdesc-iec/zh-cn_image_0225250300.png "点击放大")

按照从用户/终端到中心云（父区域）的距离，可以划分3个“圈”:

* 第一个“圈”是现场边缘，覆盖1~5ms时延范围，算力以AI推理为主，主要面向自动驾驶，工业互联网等实时性业务。
* 第二个“圈”是近场边缘，覆盖5~20ms时延范围，算力以渲染为主，同时还有一部分推理，主要面向视频场景。
* 第三个“圈”是传统的公有云（也称为中心云），覆盖20~100ms时延范围，用于承载未下沉到边缘的业务，例如海量的数据存储，挖掘，训练等。

面向近场边缘和现场边缘场景，华为云分别推出了[智能边缘云](https://www.huaweicloud.com/zh-cn/product/iec.html)（Intelligent EdgeCloud，IEC）和[智能边缘小站](https://www.huaweicloud.com/zh-cn/product/ies.html)（CloudPond）两款产品。

* [智能边缘云](https://www.huaweicloud.com/zh-cn/product/iec.html)IEC：提供广域覆盖的分布式边缘云，用于客户就近灵活部署业务。
* [智能边缘小站](https://www.huaweicloud.com/zh-cn/product/ies.html)CloudPond：提供部署在用户数据中心的软硬件一体的边缘解决方案。

除了上述两款产品，华为云还推出了面向客户业务现场场景的[智能边缘平台](https://www.huaweicloud.com/zh-cn/product/ief.html)（Intelligent EdgeFabric，IEF）产品。作为基于云原生技术构建的边云协同操作系统，IEF可运行在多种边缘设备上，将丰富的AI、IoT（Internet of Things）及数据分析等智能应用以轻量化的方式从云端部署到边缘，满足用户对智能应用边云协同的业务诉求。

#### 什么是智能边缘云

智能边缘云（IEC）部署在距离企业和热点用户区域更近的位置，具有与中心云一致的体验，为时延敏感型业务如互动娱乐、在线教育、媒体创作等提供低于10ms的时延体验，支持全局智能管理及调度。

您可以通过[IEC和华为云的关系是什么？](https://support.huaweicloud.com/zh-cn/iec_faq/iec_04_0102.html)了解更多详情。

IEC产品架构如[图3](#iec_01_0100__fig3978134523815)所示。

**图3** IEC产品架构
  
![](https://support.huaweicloud.com/productdesc-iec/zh-cn_image_0244413346.png "点击放大")

* IEC控制台和API部署在华为云中，提供边缘业务管理，支持跨边缘站点的统一算力、网络、存储、镜像配置及管理。
* IEC使用华为云统一身份认证（Identity and Access Management，IAM）服务提供账号鉴权功能，使用华为云镜像服务（Image Management Service，IMS）提供创建实例需要的私有镜像。

  需要注意的是除了IAM和IMS之外，其余架构图中提到的虚拟私有云（Virtual Private Cloud，VPC），弹性公网IP（Elastic IP，EIP），实例、子网、磁盘、安全组、网络ACL（Access Control Lists，访问控制列表）等组件均属于IEC范畴，与华为云上的云服务，包括弹性云服务器（Elastic Cloud Server，ECS），云硬盘（Elastic Volume Service，EVS）服务，虚拟私有云VPC虽然功能类似，但没有关联关系，各自承载不同的业务。举例说明，通过IEC控制台或者API创建的实例仅归属于华为云服务IEC业务范畴，与通过华为云服务ECS创建的实例没有关联关系。IEC上创建的实例不能通过ECS管理，ECS上创建的实例也不能通过IEC管理。
* IEC在中国大陆建立了多个边缘站点，提供物理隔离的资源池，提供多元算力、存储和网络的能力。
* 边缘站点之间物理隔离，所以归属于不同边缘站点的子网之间不连通；VPC之间逻辑隔离，所以归属于不同VPC的子网之间不连通。如[图3](#iec_01_0100__fig3978134523815)，四个子网彼此互不连通。
* 用户在IEC控制台或者通过API[创建边缘业务](https://support.huaweicloud.com/zh-cn/qs-iec/iec_03_0300.html)后，系统自动将用户业务就近接入边缘站点。通过动态调度，实现降低网络时延等优势。

详细的各组件介绍内容和配置操作请参见《[智能边缘云用户指南](https://support.huaweicloud.com/zh-cn/usermanual-iec/iec_02_0100.html)》。

#### 为什么选择智能边缘云

自建服务存在的成本高，安全风险大等诸多劣势已无法满足新型业务的高要求。[图4](#iec_01_0100__fig1863519367470)向您详细展示了IEC与自建服务的优劣势对比。

**图4** IEC与自建服务对比
  
![](https://support.huaweicloud.com/productdesc-iec/zh-cn_image_0225299740.png "点击放大")

上一部分[边缘计算](#iec_01_0100__section19200132384420)中我们提到华为云边缘计算的范畴，您可以通过[图5](#iec_01_0100__fig141031246184613)进一步了解IEC在面对边缘侧业务下相比传统集中式公有云在降低网络时延方面的优势。

**图5** IEC与传统公有云对比
  
![](https://support.huaweicloud.com/productdesc-iec/zh-cn_image_0225332230.png "点击放大")

了解更多选择IEC的优势，请参见[产品优势](https://support.huaweicloud.com/productdesc-iec/iec_01_0200.html)。

#### IEC与相关产品区别

华为提供多种云化产品，您可以通过[表1](#iec_01_0100__table719329134316)了解智能边缘云（IEC）和智能边缘小站（CloudPond）、智能边缘平台（Intelligent EdgeFabric，IEF）、IoT边缘（IoT Edge）、内容分发网络（Content Delivery Network，CDN）的区别，以便根据使用场景综合选择。

**表1** IEC与相关产品区别

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 产品名称 | [IEC](https://www.huaweicloud.com/zh-cn/product/iec.html) | [CloudPond](https://www.huaweicloud.com/zh-cn/product/ies.html) | [IEF](https://www.huaweicloud.com/zh-cn/product/ief.html) | [IoT Edge](https://www.huaweicloud.com/zh-cn/product/iotedge.html) | [CDN](https://www.huaweicloud.com/zh-cn/product/cdn.html) |
| 定位 | 构建广域覆盖的分布式边缘云 | 构建部署在用户数据中心的边缘小站 | 基于云原生技术构建的边云协同操作系统 | 物联网边缘“小脑” | 构建在现有互联网基础之上的一层智能虚拟网络 |
| 能力 | 提供多元算力，满足多种业务需求，用户通过就近部署业务，有效降低网络时延 | 将华为云可用区拉远，在用户数据中心提供公有云服务，满足数据本地化需求，降低业务延迟 | 从云端下发应用到边缘，帮助用户在云端对边缘应用进行管理，解决应用“推送/简化部署”到边缘的问题 | 聚焦边缘设备管理，就近提供计算和智能服务，满足行业在实时业务、应用智能等方面的需求 | 提高用户访问网站的响应速度与网站的可用性，解决网络带宽小、用户访问量大、网点分布不均等问题 |
| 适用场景 | 直播、边缘渲染加速、云游戏等 | 创新业务部署、传统业务上云、数据本地留存 | 园区视频分析、工业视觉、工业预测性维护等 | 智慧园区、智慧交通、智能制造等 | 网站加速、文件下载加速等内容加速 |
| 部署位置 | 运营商机房 | 用户数据中心 | 任意位置 | 任意位置 | 运营商机房 |

IEC使用过程和其他一些云服务有依赖或协作关系，详情请参见[与其他云服务的关系](https://support.huaweicloud.com/productdesc-iec/iec_01_0900.html)。

#### 访问方式

您可以通过控制台和API两种方式访问IEC。

**表2** 访问方式

| **方式** | **说明** | 入口/指导 |
| --- | --- | --- |
| 控制台 | 提供直观的Web化管理界面，简化您的操作。 | 请参见《[智能边缘云快速入门](https://support.huaweicloud.com/zh-cn/qs-iec/iec_03_0100.html)》 |
| API | 提供基于HTTPS请求的API，方便您将IEC集成到第三方系统，用于二次开发。 | 请参见《[智能边缘云API参考](https://support.huaweicloud.com/zh-cn/api-iec/iec_05_0100.html)》。 |

####
