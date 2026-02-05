---
title: "什么是CloudPond"
code: "cloudpond"
category: "CDN与智能边缘"
source_url: "https://support.huaweicloud.com/productdesc-cloudpond/ies_01_0100.html"
crawled_at: "2026-02-05T16:29:51.070211"
---

# 什么是CloudPond

## 产品简介

将云基础设施部署到机房用于边缘计算

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-cloudpond/zh-cn_image_0272668769.png)

![图片2](https://support.huaweicloud.com/productdesc-cloudpond/zh-cn_image_0272668770.png)

![图片3](https://support.huaweicloud.com/productdesc-cloudpond/zh-cn_image_0000001658166036.png)

## 详细说明

# 什么是CloudPond

#### 边缘计算

迈入5G和AI时代，新型业务如增强现实AR、虚拟现实VR、互动直播、自动驾驶、智能制造等应运而生。以上这些业务场景对时延和网络带宽有着强烈诉求，而在传统的集中式云计算场景中，所有数据都集中存储在大型数据中心。由于地理位置和网络传输的限制，无法满足新型业务的低时延、高带宽等要求。

* 网络高时延：传统云计算无法即时处理和分析新型业务产生的数据，导致应用终端获得的响应慢，体验差。
* 带宽高成本：新型业务的应用终端产生的数据传回云端将消耗更高的网络带宽，导致服务厂商需要支付高昂的网络成本。
* 数据合规性：新型业务数据存储在云端，无法满足企业对敏感数据本地化存储的要求，直接影响企业数据上云的策略。

面对传统集中式云计算的固有局限性，边缘计算成为应对新型业务和数据合规业务的较好选择。边缘计算通过在靠近终端应用的位置建立站点，最大限度的将集中式云计算的能力延伸到边缘侧，有效解决以上的时延和带宽问题。

您可以参考[图1](#ies_01_0100__fig15619657111913)了解更多关于云计算和边缘计算的区别。

**图1** 云计算和边缘计算
  
![](https://support.huaweicloud.com/productdesc-cloudpond/zh-cn_image_0272668769.png "点击放大")

从广义上讲，云计算包括边缘计算，边缘计算是云计算的扩展，二者为互补而非替代关系。只有云计算与边缘计算相互协同（简称边云协同），才能更好的满足各种应用场景下的不同需求。

通过[图2](#ies_01_0100__fig14441324155218)进一步了解边缘计算的范畴。

**图2** 边缘计算的范畴
  
![](https://support.huaweicloud.com/productdesc-cloudpond/zh-cn_image_0272668770.png "点击放大")

按照从用户/终端到中心云的距离，可以划分3个“圈”:

* 第一个“圈”是现场边缘，覆盖1~5ms时延范围，算力以AI推理为主，主要面向自动驾驶，工业互联网等实时性业务。
* 第二个“圈”是近场边缘，覆盖5~20ms时延范围，算力以渲染为主，同时还有一部分推理，主要面向视频场景。
* 第三个“圈”是传统的公有云（也称为中心云），覆盖20~100ms时延范围，用于承载未下沉到边缘的业务，例如海量的数据存储，挖掘，训练等。

面向近场边缘和现场边缘场景，华为云分别推出了[智能边缘云](https://www.huaweicloud.com/zh-cn/product/iec.html)（IEC）和[CloudPond云服务](https://www.huaweicloud.com/zh-cn/product/ies.html)两款产品。

* 智能边缘云IEC：提供广域覆盖的分布式边缘云，用于客户就近灵活部署业务。
* CloudPond：提供部署在用户数据中心的软硬件一体的边缘解决方案。

除了上述两款产品，华为云还推出了面向客户业务现场场景的[智能边缘平台](https://www.huaweicloud.com/zh-cn/product/ief.html)（Intelligent EdgeFabric，IEF）产品。作为基于云原生技术构建的边云协同操作系统，IEF可运行在多种边缘设备上，将丰富的AI、IoT（Internet of Things）及数据分析等智能应用以轻量化的方式从云端部署到边缘，满足用户对智能应用边云协同的业务诉求。

关于CloudPond云服务、智能边缘云和智能边缘平台的详细对比，请参见[CloudPond、IEC、IEF有什么区别和关联？](https://support.huaweicloud.com/zh-cn/cloudpond_faq/ies_04_0102.html)。

面向现场边缘场景，现推出CloudPond云服务（CloudPond）产品，提供部署在用户本地的软硬件一体的边缘解决方案。

#### 什么是CloudPond云服务

CloudPond云服务将云基础设施和云服务部署到企业现场，适合对应用访问时延、数据本地化留存及本地系统交互等有高要求的场景，可便捷地将云端丰富应用部署到本地。

您可以通过[CloudPond和华为云的关系是什么？](https://support.huaweicloud.com/zh-cn/cloudpond_faq/ies_04_0104.html)了解更多详情。

CloudPond产品架构如[图3](#ies_01_0100__fig3807124716119)所示。提前熟悉CloudPond的一些[常用概念](https://support.huaweicloud.com/productdesc-cloudpond/ies_01_1000.html)将帮助您更轻松的了解CloudPond产品架构。

**图3** CloudPond产品架构
  
![](https://support.huaweicloud.com/productdesc-cloudpond/zh-cn_image_0000001658166036.png "点击放大")

* CloudPond将华为云一体化整机柜设备部署到用户本地，为您提供在本地使用华为云服务的机会。
* [边缘小站](https://support.huaweicloud.com/productdesc-cloudpond/ies_01_1000.html#ies_01_1000__section20361111755519)隶属于华为云区域的边缘可用区，该可用区基础设施由华为云完全托管、维护和支持，使用体验与通用可用区一致。边缘小站和其所属的边缘可用区，以及小站中运行的云资源为CloudPond用户专属，与其他公有云用户不共享，您可以通过[边缘小站与区域和可用区是什么关系？](https://support.huaweicloud.com/cloudpond_faq/ies_04_0401.html)了解更多详情。

  根据实际业务类型的多样化，同一个数据中心的不同场地可以分别部署多个不同的边缘小站。您也可以在多个地理位置不同的数据中心创建多个不同的边缘小站。
* CloudPond控制台部署在中心云上。通过CloudPond控制台，您可以方便的查看边缘小站信息和云服务资源的使用情况。
* 用户通过云服务控制台进行业务资源的开通和管理。CloudPond运行必选的云服务包括[弹性云服务器](https://www.huaweicloud.com/product/ecs.html)（Elastic Cloud Server，ECS）、[云硬盘](https://www.huaweicloud.com/product/evs.html)（Elastic Volume Service，EVS）、[虚拟私有云](https://www.huaweicloud.com/product/vpc.html)（Virtual Private Cloud，VPC）、[弹性公网IP](https://www.huaweicloud.com/product/eip.html)（Elastic IP，EIP），同时您可以根据需求将一些可选的云服务和应用部署在CloudPond上。更多云服务支持情况请参见[与CloudPond有业务交互的云服务](https://support.huaweicloud.com/productdesc-cloudpond/ies_01_1100.html#ies_01_1100__section86011712459)。您还可以使用统一身份认证服务IAM和云监控服务CES分别对部署在CloudPond上的云服务资源进行账号鉴权和监控。
* 网络连接方面：
  + CloudPond和用户本地系统之间：根据实际业务需要，用户可以打通边缘小站和用户本地系统的网络通信，使得用户能够更便捷的将CloudPond整体纳入企业内网架构中。
  + CloudPond和中心云之间：CloudPond所在的边缘可用区和中心云的通用可用区共享同一虚拟私有云VPC，用户在CloudPond上可通过VPC内网访问中心云的其他云服务。

  更多详细介绍请参见[网络连接](https://support.huaweicloud.com/zh-cn/usermanual-cloudpond/ies_02_0500.html)[组网方案和要求](https://support.huaweicloud.com/productdesc-cloudpond/ies_01_0600.html)。

#### 为什么选择CloudPond

考虑到自建IT系统的各种困难（如部署周期长，运维难度高，运营成本高等），很多企业用户选择了业务上云，而上什么云取决于企业的自身条件和需求。目前，业界主流的云形态有私有云、公有云、混合云等。

CloudPond呈现了一种全新的产品形态，吸取了已有的几类云形态的优势，提供低时延、低成本、数据本地化等服务能力，有效解决了用户在一些场景下单独使用一类云形态时遇到的痛点问题。

CloudPond和私有云、公有云、混合云的对比请参见[表1 CloudPond和私有云、公有云、混合云的对比](#ies_01_0100__table131791828192013)。

**表1** CloudPond和私有云、公有云、混合云的对比

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 产品形态 | CloudPond | 私有云 | 公有云（中心云） | 混合云 |
| 定位 | 归属于华为云的一款针对边缘计算场景的云服务，部署于用户数据中心的华为云边缘小站。 | 部署于用户本地或者指定的物理位置，专供一个用户使用，该用户拥有对基础设施和云资源的完全控制权。所有操作始终在私有网络上进行。 | 云资源由公有云厂商拥有和运营，通过Internet提供给用户按需/包周期使用，基础设施部署于云厂商的数据中心。 | 结合私有云和公有云的一种模式，用户可将敏感数据存储在私有云，同时利用托管公有云的计算资源。 |
| 安装和运维 | 用户直接租赁华为云提供的一体化机柜，基础设施由华为云负责安装和运维，用户仅需保证本地机房环境的可用性和稳定性即可。 | * 用户自建：用户自行采购基础设施，并负责安装和运维。 * 托管建设：用户租赁或者买断第三方云厂商提供的基础设施，联合云厂商共同负责基础设施的安装和运维。 | 用户直接使用第三方云厂商提供的云服务，基础设施由云厂商负责安装和运维。 | 用户租赁或者买断第三方云厂商提供的私有云和公有云的混合基础设施，联合云厂商共同负责基础设施的安装和运维。 |
| 云资源占用 | 用户专属 | 用户专属 | 与其他用户共享 | 用户专属和与其他用户共享混合 |
| 数据本地化 | 所有数据存储在本地边缘小站内，满足数据合规要求。 | 数据存储在自建或者托管的数据中心。 | 数据存储在云厂商数据中心。 | 部分数据存储在本地，部分数据存储在云厂商数据中心，视用户需求而定。 |
| 访问时延 | 边缘小站部署在用户本地，应用终端访问时延较低。 | 业务部署在用户本地或托管中心，应用终端访问时延较低。 | 业务部署在云端，应用终端访问时延相对较高。 | 视业务部署位置情况而定。 |
| 综合成本 | 成本较低，主要由用户机房、能源、云服务使用、服务支持、人员开销（业务运维）等构成。 | 成本较高，主要由用户机房、能源、相关设备、私有云软件、服务支持、人员开销（业务运维和平台运维）等构成。 | 成本较低，主要由云服务使用、网络、服务支持、人员开销（业务运维）等构成。 | 成本中等，由私有云和公有云成本共同组成，不同用户的私有云和公有云占比不同。 |

更多更详细的选择理由请参见[产品优势](https://support.huaweicloud.com/productdesc-cloudpond/ies_01_0200.html)。

#### 访问方式

您可以通过控制台和API两种方式访问CloudPond。

控制台的操作请参见《[CloudPond云服务快速入门](https://support.huaweicloud.com/zh-cn/qs-cloudpond/ies_03_0100.html)》。

**表2** 访问方式

| **方式** | **说明** | 入口/指导 |
| --- | --- | --- |
| 控制台 | 提供直观的Web化管理界面，简化您的操作。 | 请参见《[CloudPond云服务快速入门](https://support.huaweicloud.com/zh-cn/qs-cloudpond/ies_03_0100.html)》 |
| API | 提供基于HTTPS请求的API，方便您将CloudPond集成到第三方系统，用于二次开发。 | 请参见[《CloudPond云服务API参考》](https://support.huaweicloud.com/api-cloudpond/ies_05_0100.html)。 |

####
