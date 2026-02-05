---
title: "什么是弹性公网IP"
code: "eip"
category: "网络"
source_url: "https://support.huaweicloud.com/productdesc-eip/overview_0001.html"
crawled_at: "2026-02-05T16:28:45.758562"
---

# 什么是弹性公网IP

## 产品简介

提供独立的公网IP资源服务

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-eip/zh-cn_image_0000002182297312.png)

![图片2](https://support.huaweicloud.com/productdesc-eip/zh-cn_image_0000002182457028.png)

![图片3](https://support.huaweicloud.com/productdesc-eip/public_sys-resources/note_3.0-zh-cn.png)

![图片4](https://support.huaweicloud.com/productdesc-eip/zh-cn_image_0000002201759752.png)

## 详细说明

# 什么是弹性公网IP

#### 产品简介

弹性公网IP（Elastic IP，简称EIP）提供独立的公网IP资源，包括公网IP地址与公网出口带宽服务。为资源配置弹性公网IP后，可以直接访问公网，如果资源只配置了私网IP，就无法直接访问公网。

弹性公网IP和与它要绑定的云资源必须在同一个区域，不支持跨区域使用弹性公网IP。

全域弹性公网IP（Global Elastic IP, 简称G-EIP）提供全球公网接入能力，支持用户指定全局区域及地址池创建公网IP地址，可跨区域绑定云上任意区域的实例（如ECS、ELB等），实现云上资源和公网通信。

如[表1](#overview_0001__zh-cn_topic_0000002072814242_table1517313813614)所示，您可以根据实际业务需求选择适合的功能。

**表1** EIP和G-EIP功能说明

| 对比维度 | 使用场景 | 功能说明 | 功能特点 | 使用方式 |
| --- | --- | --- | --- | --- |
| 弹性公网IP | EIP和云资源必须在同一个区域，不支持跨区域使用EIP。 | EIP提供独立的公网IP资源，包括公网IP地址与公网出口带宽服务。可以与ECS、BMS、虚拟IP、ELB、NAT网关等资源灵活地绑定及解绑。 | * 支持与同区域云资源灵活的绑定与解绑 * 成本低 * 组网简单 | * [申请EIP](https://support.huaweicloud.com/usermanual-eip/eip_0008.html) * [绑定/解绑EIP](https://support.huaweicloud.com/usermanual-eip/eip_0009.html) |
| 全域弹性公网IP | 全域弹性公网IP通过绑定**全域互联带宽**和**全域公网带宽**实现跨区域绑定云上任意区域的实例。 | G-EIP提供全球公网接入能力，支持用户指定全局区域及地址池创建公网IP地址，可跨区域绑定云上任意区域的实例（如ECS、ELB等），实现云上资源和公网通信。 | * 支持与跨区域云资源绑定 * 网络通信依赖绑定全域互联带宽和全域公网带宽 | * [创建G-EIP](https://support.huaweicloud.com/usermanual-eip/eip_geip_0003.html) * [将G-EIP绑定至实例](https://support.huaweicloud.com/usermanual-eip/eip_geip_0004.html) |

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-eip/zh-cn_image_0000002332722512.png)](https://bbs-video.huaweicloud.com/video/media/20190626/20190626160610_93995/%E8%99%9A%E6%8B%9F%E7%A7%81%E6%9C%89%E4%BA%91%EF%BC%88VPC%EF%BC%89%E6%9C%8D%E5%8A%A1%E4%BB%8B%E7%BB%8D.mp4)

#### 弹性公网IP

弹性公网IP可以与弹性云服务器、裸金属服务器、虚拟IP、弹性负载均衡、NAT网关等资源灵活地绑定及解绑。

一个弹性公网IP只能绑定一个云资源使用，弹性公网IP和与它要绑定的云资源必须在同一个区域，不支持跨区域使用弹性公网IP。

以绑定ECS实例为例：

* 一个弹性公网IP只能绑定一个ECS实例，如果这个弹性公网IP已绑定了ECS实例，不支持再直接绑定其他云资源。您可以先解绑弹性公网IP，使弹性公网IP处于“未绑定实例”状态，再绑定同区域的其他云资源。
* 弹性公网IP的区域必须和要绑定的ECS实例的区域相同。比如华北-北京四的弹性公网IP，只能绑定华北-北京四的ECS。

**图1** 通过EIP访问公网
  
![](https://support.huaweicloud.com/productdesc-eip/zh-cn_image_0000002182297312.png "点击放大")

#### 弹性公网IP带宽

带宽是指在单位时间（一般指的是1秒钟）内能传输的数据量，带宽数值越大表示传输能力越强，即在单位时间内传输的数据量越多。带宽分为公网带宽和内网带宽。

公网带宽是指华为云到公网之间的网络带宽流量。公网带宽分为出云带宽和入云带宽。本文主要介绍出云带宽和入云带宽，具体内容参见[图2](#overview_0001__zh-cn_topic_0000002072814242_zh-cn_topic_0171168670_fig147774992112)。

* **出云带宽**在云监控指标中对应的是**出网带宽**/**出网流量**指标。
* **入云带宽**在云监控指标中对应的是**入网带宽**/**入网流量**指标。

**图2** 入云带宽和出云带宽
  
![](https://support.huaweicloud.com/productdesc-eip/zh-cn_image_0000002182457028.png "点击放大")

**表2** 出云带宽和入云带宽

| 带宽类别 | **描述** |
| --- | --- |
| 出云带宽 | 从华为云流出到公网方向的带宽。例如，云服务器对外提供访问，或者在外网的FTP客户端下载云服务器内部的资源等方式都是使用出云带宽。在云监控指标中对应的是出网带宽/出网流量指标。  **目前，华为云仅对出云带宽（即**出网**带宽/**出网**流量）收取费用。**  说明：  * 如果您需要**查看带宽使用情况**，请参见[查看监控指标](https://support.huaweicloud.com/usermanual-eip/monitor_0003.html)。 * 如果您需要**查看带宽的计费详情**，请参见[费用账单](https://support.huaweicloud.com/price-eip/eip_billing_0022.html)。 |
| 入云带宽 | 从公网流入华为云方向的带宽。例如，在云服务器内部下载外部网络资源，或者在外网的FTP客户端上传云服务器内部的资源等方式都是使用入云带宽。在云监控指标中对应的是入网带宽/入网流量指标。  入云带宽的最大值受用户购买的出云带宽值影响，带宽限速规则如下：  * 若您的带宽大小小于或等于10Mbit/s，则入云方向带宽为10Mbit/s，出云方向带宽大小为您的实际带宽大小。 * 若您的带宽大小大于10Mbit/s，则出云方向和入云方向带宽相同，都等于您的实际带宽大小。  上述带宽限速规则不适用华北-北京一、华东-上海二区域。 |

#### 弹性公网IP线路类型

弹性公网IP带宽的线路类型有：全动态BGP线路、精品动态BGP线路、静态BGP线路，对比如下所示。

![](https://support.huaweicloud.com/productdesc-eip/public_sys-resources/note_3.0-zh-cn.png) 

因产品升级，优选BGP线路已于2025年12月1日 0点售罄下线，您在此时间之前创建的优选BGP类型资源（含弹性公网IP、共享带宽实例）可继续正常使用，不受下线影响，直至您主动释放或退订云服务实例。

**表3** 静态BGP、全动态BGP、精品动态BGP的区别

| 对比维度 | 精品动态BGP | 静态BGP | 全动态BGP |
| --- | --- | --- | --- |
| 定义 | 精品动态BGP线路类型是特定方向的优质互联网线路。通过与多家主流运营商线路互联对接，建立由中国-香港直连中国内地的公网互联路径，提供两区域间低时延、高质量的互联网通信。相较于原“优选BGP”类型线路，精品动态BGP重点优化中国内地省级路由，进一步提升网络访问体验。 | 由网络运营商手动配置的路由信息。当网络的拓扑结构或链路的状态发生变化时，运营商需要手动去修改路由表中相关的静态路由信息。 | 使用BGP协议同时接入多个运营商，可以根据设定的寻路协议实时自动优化网络结构，保持客户使用的网络持续稳定，高效。 |
| 保障性 | 线路保障能力与全动态BGP一致，多线接入的BGP，在遇到运营商内部故障时，能够快速切换到其他运营商接入链路，保证用户能够正常访问。除此之外，质量更高，时延更低。目前支持中国-香港当地主流运营商线路。 | 当静态BGP中网络结构发生变化，运营商是无法在第一时间自动调整网络设置，而是通过其他技术进行切换，所以静态BGP时延一般略大。  如用户选择静态BGP，需要自身应用系统具备容灾功能。 | 多线接入的BGP，能够感知接入线路及运营商内部网络状况，运营商内部故障时，能够快速切换到其他运营商接入链路，保证用户能够正常访问，而不是访问中断。  目前支持的运营商线路包括：电信、移动、联通、教育网、广电、鹏博士等 。 |
| 优势 | * 避免绕行国际运营商出口网络。 * 延时更低，可有效提升境外业务对中国大陆用户覆盖质量。 | 通过单个网络运营商访问公网，成本低且便于自主调度。 | BGP公网出口支持秒级跨域切换，保证您的用户无论使用哪种网络，均能享受高速、安全的网络质量。 |
| 服务可用性 | 99.95% | 99% | 99.95% |
| 计费 | 精品动态BGP > 全动态BGP > 静态BGP。更多计费详情请参见[产品价格详情](https://www.huaweicloud.com/pricing.html?tab=detail#/eip)中“弹性公网IP”的内容。 | | |

![](https://support.huaweicloud.com/productdesc-eip/public_sys-resources/note_3.0-zh-cn.png) 

* 关于服务可用性的更多信息请参见[SLA服务等级协议](https://www.huaweicloud.com/declaration/sla.html)。
* 亚太及中国-香港地域的EIP（除优选BGP线路外），在为中国内地客户端提供服务或访问中国内地公网资源时，会有较高访问延迟，极限情况下可能会产生丢包。建议您采用同Region部署业务或云连接（Cloud Connect）进行跨域互联。

  注：亚太地域包括亚太-新加坡、亚太-曼谷、亚太-雅加达、亚太-马尼拉。

#### 如何访问弹性公网IP

通过管理控制台、基于HTTPS请求的API（Application Programming Interface）两种方式访问弹性公网IP。

* 管理控制台方式

  管理控制台是网页形式的，您可以使用直观的界面进行相应的操作。登录[管理控制台](https://console.huaweicloud.com/?locale=zh-cn)，从主页选择“弹性公网IP”。
* API方式

  如果用户需要将云平台上的弹性公网IP集成到第三方系统，用于二次开发，请使用API方式访问弹性公网IP，具体操作请参见[《弹性公网IP API参考》](https://support.huaweicloud.com/api-eip/eip_api01_0001.html)。

#### 全域弹性公网IP

全域弹性公网IP（Global Elastic IP，G-EIP）提供全球公网接入能力，支持用户指定全局区域及地址池创建公网IP地址，可跨区域绑定云上任意区域的实例，实现云上资源和公网通信。全域公网带宽架构如[图3](#overview_0001__zh-cn_topic_0000002072814242_fig5535123113916)所示。

**图3** 全域弹性公网IP架构
  
![](https://support.huaweicloud.com/productdesc-eip/zh-cn_image_0000002201759752.png "点击放大")

#### 全域弹性公网IP的网络说明

全域弹性公网IP需要绑定**全域互联带宽**和**全域公网带宽**实现云内骨干网络通信和公网通信。如果实例为ECS时，还需要将全域互联网网关绑定至全域弹性公网IP。

**表4** 全域弹性公网IP网络说明

| 通信场景 | 所需资源 | 场景说明 | 举例说明 | 操作指导 |
| --- | --- | --- | --- | --- |
| 云内通信 | * 全域弹性公网IP * 全域互联带宽 * 和全域弹性公网IP绑定的实例，比如ECS、ELB | 连通G-EIP和实例之间的云内网络，必须为G-EIP绑定全域互联带宽，根据G-EIP接入点和实例所在区域，选择不同类型的全域互联带宽。  关于全域互联带宽的详细信息，请参见[全域互联带宽概述管理](https://support.huaweicloud.com/usermanual-cc/cc_03_1101.html)。 | * G-EIP A的接入点为华东-杭州，G-EIP A绑定的ELB-A所在区域为华东-上海一，华东-杭州和华东-上海一均属于华东城域，因此全域互联带宽-A选择城域带宽。 * G-EIP B的接入点为华东-杭州，G-EIP B绑定的ECS-B所在区域为华南-广州，华东-杭州和华南-广州属于不同城域，但是属于同一个大区，因此全域互联带宽-B选择大区带宽。 * G-EIP C的接入点为华东-杭州，G-EIP C绑定的ECS-C所在区域为中国-香港，华东-杭州和中国-香港属于不同的大区，因此全域互联带宽-C选择跨区带宽。 | 1. [创建全域弹性公网IP](https://support.huaweicloud.com/usermanual-eip/eip_geip_0003.html)：创建一个或者多个G-EIP。 2. [将全域弹性公网IP绑定至实例](https://support.huaweicloud.com/usermanual-eip/eip_geip_0004.html)：将G-EIP绑定至ECS或者ELB实例，一个G-EIP同时只能绑定一个任意区域的实例。 3. [将实例添加至全域互联带宽](https://support.huaweicloud.com/usermanual-cc/cc_03_1103.html)： 为G-EIP绑定全域互联带宽。  一个全域互联带宽仅能关联一种实例类型，首次添加了实例类型后仅可绑定该类型下的子实例，如需添加其他实例类型，请进行移出后重新添加。 |
| 公网通信 | * 全域弹性公网IP * 全域公网带宽 * 和全域弹性公网IP绑定的实例，比如ECS、ELB | 连通G-EIP和公网之间的网络，必须将G-EIP加入全域公网带宽中，G-EIP接入点和全域公网带宽保持一致，一个全域公网带宽中可同时加入多个G-EIP。  关于全域公网带宽的详细信息，请参见[全域公网带宽概述](https://support.huaweicloud.com/usermanual-eip/eip_ibw_0002.html)。 | 将G-EIP A、G-EIP B、G-EIP C添加到全域公网带宽-A中，G-EIP和全域公网带宽的接入点必须保持一致，此处均为华东-杭州，带宽的复用为您节约网络成本。 | 1. [购买全域公网带宽](https://support.huaweicloud.com/usermanual-eip/eip_ibw_0003.html)：购买全域公网带宽，全域公网带宽中的接入点必须和G-EIP的接入点保持一致。 2. [迁入全域弹性公网IP](https://support.huaweicloud.com/usermanual-eip/eip_ibw_0004.html)：将G-EIP添加到全域公网带宽中，一个全域公网带宽中可同时加入多个G-EIP。 |

#### 如何访问全域弹性公网IP

通过管理控制台、基于HTTPS请求的API（Application Programming Interface）两种方式访问全域弹性公网IP。

* 管理控制台方式

  管理控制台是网页形式的，您可以使用直观的界面进行相应的操作。登录[管理控制台](https://console.huaweicloud.com/?locale=zh-cn)，从主页选择“全域弹性公网IP”。
* API方式

  如果用户需要将云平台上的全域弹性公网IP集成到第三方系统，用于二次开发，请使用API方式访问全域弹性公网IP，具体操作请参见[《弹性公网IP API参考》](https://support.huaweicloud.com/api-eip/globalEips.html)。

####
