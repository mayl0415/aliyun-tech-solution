---
title: "什么是对象存储服务"
code: "obs"
category: "存储"
source_url: "https://support.huaweicloud.com/productdesc-obs/zh-cn_topic_0045829060.html?utm_source=obs_Growth_map&utm_medium=display&utm_campaign=help_center&utm_content=Growth_map"
crawled_at: "2026-02-05T16:27:29.685510"
---

# 什么是对象存储服务

## 产品简介

稳定、安全、高效、易用的云存储服务

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-obs/figure/zh-cn_image_0000001886542248.png)

![图片2](https://support.huaweicloud.com/productdesc-obs/public_sys-resources/note_3.0-zh-cn.png)

## 详细说明

# 什么是对象存储服务

#### 对象存储服务简介

[对象存储服务](https://www.huaweicloud.com/product/obs.html)（Object Storage Service，OBS）是一个基于对象的海量存储服务，为客户提供海量、安全、高可靠、低成本的数据存储能力。

OBS系统和单个桶都没有总数据容量和对象/文件数量的限制，为用户提供了超大存储容量的能力，适合存放任意类型的文件，适合普通用户、网站、企业和开发者使用。OBS是一项面向Internet访问的服务，提供了基于HTTP/HTTPS协议的Web服务接口，用户可以随时随地连接到Internet，通过OBS[管理控制台](https://console.huaweicloud.com/console/?locale=zh-cn#/obs/manager/buckets)或各种OBS工具访问和管理存储在OBS中的数据。此外，OBS支持SDK和OBS API接口，可使用户方便管理自己存储在OBS上的数据，以及开发多种类型的上层业务应用。

在全球多区域部署了OBS基础设施，具备高度的可扩展性和可靠性，用户可根据自身需要指定区域使用OBS，由此获得更快的访问速度和实惠的服务价格。

#### 介绍视频

[![](https://support.huaweicloud.com/productdesc-obs/figure/zh-cn_image_0000002375067138.jpg)](https://bbs-video.huaweicloud.com/video/media/20200428/20200428174250_80882/OBS%E5%AF%B9%E8%B1%A1%E5%AD%98%E5%82%A8%E6%9C%8D%E5%8A%A1%E4%BB%8B%E7%BB%8D.mp4)

#### 产品架构

OBS的基本组成是[桶](https://support.huaweicloud.com/productdesc-obs/obs_03_0207.html)和[对象](https://support.huaweicloud.com/productdesc-obs/obs_03_0206.html)。

桶是OBS中存储对象的容器，每个桶都有自己的存储类别、访问权限、所属区域等属性，用户在互联网上通过桶的[访问域名](https://support.huaweicloud.com/productdesc-obs/obs_03_0152.html)来定位桶。

对象是OBS中数据存储的基本单位，一个对象实际是一个文件的数据与其相关属性信息的集合体，包括Key、Metadata、Data三部分：

* Key：键值，即对象的名称，为经过UTF-8编码的长度大于0且不超过1024的字符序列。一个桶里的每个对象必须拥有唯一的对象键值。
* Metadata：元数据，即对象的描述信息，包括系统元数据和用户元数据，这些元数据以键值对（Key-Value）的形式被上传到OBS中。
  + 系统元数据由OBS自动产生，在处理对象数据时使用，包括Date，Content-length，Last-modify，ETag等。
  + 用户元数据由用户在上传对象时指定，是用户自定义的对象描述信息。
* Data：数据，即文件的数据内容。

针对OBS提供的REST API进行了二次开发，为您提供了[管理控制台](https://console.huaweicloud.com/console/?locale=zh-cn#/obs/manager/buckets)、SDK和各类工具，方便您在不同的场景下轻松访问OBS桶以及桶中的对象。您也可以利用OBS提供的SDK和API，根据您业务的实际情况自行开发，以满足不同场景的海量数据存储诉求。

**图1** 产品架构
  
![](https://support.huaweicloud.com/productdesc-obs/figure/zh-cn_image_0000001886542248.png "点击放大")

#### 存储类别

OBS提供了四种存储类别：标准存储、低频访问存储、归档存储、深度归档存储（受限公测中），从而满足客户业务对存储性能、成本的不同诉求。不同规格的存储类别转换请参见[OBS存储类别转换](https://support.huaweicloud.com/usermanual-obs/obs_41_0082.html)，不同规格的存储类别计费参见[存储费用](https://support.huaweicloud.com/price-obs/obs_42_0003.html)。

* 标准存储访问时延低和吞吐量高，因而适用于有大量热点文件（平均一个月多次）或小文件（小于1MB），且需要频繁访问数据的业务场景，例如：大数据、移动应用、热点视频、社交图片等场景。
* 低频访问存储适用于不频繁访问（平均一年少于12次）但在需要时也要求快速访问数据的业务场景，例如：文件同步/共享、企业备份等场景。与标准存储相比，低频访问存储有相同的数据持久性、吞吐量以及访问时延，且成本较低，但是可用性略低于标准存储。
* 归档存储适用于很少访问（平均一年访问一次）数据的业务场景，例如：数据归档、长期备份等场景。归档存储安全、持久且成本极低，可以用来替代磁带库。为了保持成本低廉，数据恢复时间可能长达数分钟到数小时不等。
* 深度归档存储（受限公测）适用于长期不访问（平均几年访问一次）数据的业务场景，其成本相比归档存储更低，但相应的数据恢复时间将更长，一般为数小时。

上传对象时，对象的存储类别默认继承桶的存储类别，您也可以重新指定对象的存储类别。

修改桶的存储类别，桶内已有对象的存储类别不会修改，新上传对象时的默认对象存储类别随之修改。

**表1** 存储类别对比

| 对比项目 | 标准存储 | 低频访问存储 | 归档存储 | 深度归档存储（受限公测） |
| --- | --- | --- | --- | --- |
| 特点 | 高性能、高可靠、高可用的对象存储服务 | 高可靠、较低成本的实时访问存储服务 | 归档数据的长期存储，存储单价更优惠 | 深度归档数据的长期存储，存储单价相比归档存储更优惠 |
| 应用场景 | 云应用、数据分享、内容分享、热点对象 | 网盘应用、企业备份、活跃归档、监控数据 | 档案数据、医疗影像、视频素材、带库替代 | 长期不访问的数据存档场景 |
| [设计持久性](https://support.huaweicloud.com/obs_faq/obs_faq_0058.html) | 99.999999999% | 99.999999999% | 99.999999999% | 99.999999999% |
| [设计持久性（多AZ）](https://support.huaweicloud.com/obs_faq/obs_faq_0058.html) | 99.9999999999% | 99.9999999999% | 不支持多AZ | 不支持多AZ |
| [设计可用性](https://support.huaweicloud.com/obs_faq/obs_faq_0058.html) | 99.99% | 99% | 99% | 99% |
| [设计可用性（多AZ）](https://support.huaweicloud.com/obs_faq/obs_faq_0058.html) | 99.995% | 99.5% | 不支持多AZ | 不支持多AZ |
| 最低存储时间a | 无 | 30天 | 90天 | 180天 |
| 最小计量单位b | 64KB | 64KB | 64KB | 64KB |
| [数据恢复](https://support.huaweicloud.com/usermanual-obs/obs_03_0320.html) | 不涉及 | 按实际恢复数据量收费，单位GB | 分加急、标准恢复方式  按实际恢复数据量收费，单位GB | 分加急和标准两种恢复方式  按实际恢复数据量收费，单位GB |
| 图片处理 | 支持 | 支持 | 不支持 | 不支持 |

![](https://support.huaweicloud.com/productdesc-obs/public_sys-resources/note_3.0-zh-cn.png) 

a：最低存储时间是指对象的计费时间下限。对象存储时间小于最低存储时间时，将按照最低存储时间计费。例如，一个低频访问存储对象在OBS中存储了20天后删除，会按照30天计费。

b：最小计量单位是指对象的存储容量计费下限。存储单个对象小于64KB按64KB计费，大于64KB按实际大小计费。

#### 如何访问对象存储服务

对象存储服务提供了多种资源管理工具，您可以选择[表2](#ZH-CN_TOPIC_0000001874791709__zh-cn_topic_0129289501_table163451344069)中的任意一种方式访问并管理对象存储服务上的资源。

**表2** OBS资源管理工具

| 工具 | 描述 | 使用方法 |
| --- | --- | --- |
| 管理控制台 | [管理控制台](https://console.huaweicloud.com/console/?locale=zh-cn#/obs/manager/buckets)是网页形式的。通过[管理控制台](https://console.huaweicloud.com/console/?locale=zh-cn#/obs/manager/buckets)，您可以使用直观的界面进行相应的操作。 | [用户指南](https://support.huaweicloud.com/usermanual-obs/obs_41_0003.html)中的“使用OBS控制台”操作步骤。 |
| OBS Browser（已下线） | OBS Browser已于2020年4月15日下线，相关功能已集成到新版客户端工具OBS Browser+中，请获取最新的[OBS Browser+工具](https://support.huaweicloud.com/browsertg-obs/obs_03_1003.html)。给您带来不便敬请谅解。 | - |
| OBS Browser+ | OBS Browser+是一款运行在Windows系统上的对象存储服务管理工具，OBS Browser+的图形化界面可以非常方便地让用户在本地对OBS进行管理。 | [OBS Browser+工具指南](https://support.huaweicloud.com/browsertg-obs/obs_03_1000.html) |
| obsutil | obsutil是一款用于访问管理OBS的命令行工具，您可以使用该工具对OBS进行常用的配置管理操作。对于熟悉命令行程序的用户，obsutil是执行批量处理、自动化任务的不错选择。 | [obsutil工具指南](https://support.huaweicloud.com/utiltg-obs/obs_11_0001.html) |
| obsfs | obsfs是OBS提供的一款基于FUSE的文件系统工具，主要用于将并行文件系统挂载至Linux系统，让用户能够在本地像操作文件系统一样直接使用OBS海量的存储空间。 | [obsfs工具指南](https://support.huaweicloud.com/fstg-obs/obs_12_0001.html) |
| SDK | SDK是对OBS服务提供的REST API进行的封装，以简化用户的开发工作。用户直接调用SDK提供的接口函数即可实现使用OBS业务能力的目的。 | [SDK参考](https://support.huaweicloud.com/sdkreference-obs/obs_02_0001.html) |
| API | OBS提供REST形式的访问接口，使用户能够非常容易地从Web应用中访问OBS。用户可以通过本文档提供的简单的REST接口，在任何时间、任何地点、任何互联网设备上进行上传和下载数据。 | [API参考](https://support.huaweicloud.com/api-obs/zh-cn_topic_0031051947.html) |

####
