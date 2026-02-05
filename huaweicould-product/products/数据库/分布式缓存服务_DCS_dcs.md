---
title: "什么是分布式缓存服务"
code: "dcs"
category: "数据库"
source_url: "https://support.huaweicloud.com/productdesc-dcs/dcs-pd-200713001.html"
crawled_at: "2026-02-05T16:52:22.585029"
---

# 什么是分布式缓存服务

## 产品简介

兼容Redis®的高速内存数据处理引擎

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-dcs/public_sys-resources/note_3.0-zh-cn.png)

## 详细说明

# 什么是分布式缓存服务

分布式缓存服务（Distributed Cache Service，简称DCS）是华为云提供的一款兼容Redis的高速内存数据处理引擎，为您提供即开即用、安全可靠、弹性扩容、便捷管理的在线分布式缓存能力，满足用户高并发及数据快速访问的业务诉求。

* 即开即用

  DCS提供单机、主备、Proxy集群、Cluster集群、读写分离类型的缓存实例，拥有从128M到2048G的丰富内存规格。您可以通过控制台直接创建，无需单独准备服务器资源。

  Redis基础版实例采用容器化部署，秒级完成创建。
* 安全可靠

  借助华为云统一身份认证、虚拟私有云、云监控与云审计等安全管理服务，全方位保护实例数据的存储与访问。

  灵活的容灾策略，主备/集群实例从单AZ（可用区）内部署，到支持跨AZ部署。
* 弹性伸缩

  DCS提供对实例内存规格的在线扩容与缩容服务，帮助您实现基于实际业务量的成本控制，达到按需使用的目标。
* 便捷管理

  可视化Web管理界面，在线完成实例重启、参数修改、数据备份恢复等操作。DCS还提供基于RESTful的管理API，方便您进一步实现实例自动化管理。
* 在线迁移

  提供可视化Web界面迁移功能，支持备份文件导入和在线迁移两种方式，您可以通过控制台直接创建迁移任务，提高迁移效率。

#### 介绍视频

本视频介绍华为云的分布式缓存服务。

[![](https://support.huaweicloud.com/productdesc-dcs/zh-cn_image_0000002342403888.jpg)](https://res-video.hc-cdn.com/cloudbu-site/china/zh-cn/support/dcs-video/1717061799029480915.mp4)

#### DCS Redis

DCS Redis当前支持的Redis版本为Redis 4.0、Redis 5.0、Redis 6.0、Redis 7.0。

![](https://support.huaweicloud.com/productdesc-dcs/public_sys-resources/note_3.0-zh-cn.png) 

DCS Redis 3.0已暂停售卖，建议使用Redis 5.0及以上版本。

Redis是一种支持Key-Value等多种数据结构的存储系统。可用于缓存、事件发布或订阅、高速队列等[典型应用场景](https://support.huaweicloud.com/productdesc-dcs/dcs-pd-200713002.html)。Redis使用ANSI C语言编写，提供字符串（[String](https://redis.io/topics/data-types-intro#redis-strings)）、哈希（[Hash](https://redis.io/topics/data-types-intro#redis-hashes)）、列表（[List](https://redis.io/topics/data-types-intro#redis-lists)）、集合结构（[Set](https://redis.io/topics/data-types-intro#redis-sets)、 [Sorted\_Set](https://redis.io/topics/data-types-intro#redis-sorted-sets) ）、流（[Stream](https://redis.io/topics/streams-intro)）等数据类型的直接存取。数据读写基于内存，同时可持久化到磁盘。

DCS Redis拥有灵活的实例配置供您选择：

* 华为云DCS Redis 4.0/5.0/6.0/7.0基础版。

  **表1** DCS Redis 4.0/5.0/6.0/7.0基础版

  |  |  |
  | --- | --- |
  | 实例类型 | 提供单机、主备、Proxy集群、Cluster集群、读写分离类型，分别适配不同的业务场景。  + 单机：适用于应用对可靠性要求不高、仅需要缓存临时数据的业务场景。单机实例支持读写高并发，但不做持久化，实例重启或关闭后原有缓存数据不会加载。 + 主备：包含一个主节点，一个或多个备节点，主备节点的数据通过实时复制保持一致，当主节点故障后，备节点自动升级为主节点。同时用户可通过读写分离技术，在主节点上写，从备节点读，从而提升缓存的整体读写性能。 + Proxy集群：在Cluster集群的基础上，增加挂载Proxy节点和ELB节点，通过ELB节点实现负载均衡，将不同请求分发到Proxy节点，实现客户端高并发请求。每个Cluster集群分片默认是一个双副本的主备实例，当主节点故障后，同一分片中的备节点会升级为主节点来继续提供服务。 + Cluster集群：通过[分片](https://support.huaweicloud.com/productdesc-dcs/dcs-pd-200312004.html#dcs-pd-200312004__section20999323134412)化分区来增加缓存的容量和并发连接数，每个分片包含一个主节点和0到多个备节点，分片本身对外不可见。分片中主节点故障后，同一分片中备节点会升级为主节点来继续提供服务。用户可通过读写分离技术，在主节点上写，从备节点读，从而提升缓存的整体读写能力。 + 读写分离：在主备实例的基础上，增加挂载Proxy节点和ELB节点，通过ELB节点实现负载均衡，将不同请求分发到Proxy节点，Proxy节点识别用户读写请求，将请求发送到主节点或备节点，从而实现读写分离。 |
  | 规格 | Redis提供128MB~1024GB等多种规格。 |
  | 兼容开源Redis版本 | DCS提供不同的实例版本，分别兼容开源Redis的4.0、5.0、6.0、7.0。 |
  | 实例性能 | CPU架构为x86系列的Redis实例，单分片QPS约10万/秒，CPU架构为Arm系列的Redis实例，单分片QPS约8万/秒。 |
  | 高可用与容灾 | 除单机实例外，其他类型的实例都提供Region内的跨可用区部署，实现实例内部节点间的电力、网络层面物理隔离。 |

  有关开源Redis技术细节，您可以访问Redis官方网站<https://redis.io/>了解。
* 华为云DCS Redis 6.0企业版。

  华为云DCS 企业版，为华为云全自研的版本，由传统的master-worker线程模型升级为master-N\*worker多线程模型，对比传统缓存软件模型，整体性能N倍提升。DCS 企业版100%兼容Redis协议、模块和脚本，如脚本和事务的原子性等，在相同的硬件上，企业版的QPS约是Redis的两倍，且延迟可降低约60%。

  多线程高性能版，适用于对单节点性能有超高要求的用户，比如互联网热点事件、大咖直播等高并发访问场景。Redis 6.0之前版本，通常受到慢请求单线程处理的制约，任何一个慢请求的出现都会带来其它用户请求的延时。Redis多线程高性能版对从IO到后端事件处理的全流程，进行了多线程并行优化；通过公平自旋锁实现多线程高效访问缓存数据；通过优化Key逐出算法，提升逐出效率1倍以上；通过支持SubKey过期提高了大Key读写性能。

  **表2** DCS Redis 6.0企业版

  |  |  |
  | --- | --- |
  | 实例类型 | Redis 6.0企业版分为高性能型和企业版存储型，目前只支持主备实例类型。（企业版存储型由内存+SSD磁盘组成。）  主备实例包含一个主节点，一个备节点，主备节点的数据通过实时复制保持一致，当主节点故障后，备节点自动升级为主节点。同时用户可通过读写分离技术，在主节点上写，从备节点读，从而提升缓存的整体读写性能。 |
  | 规格 | Redis提供8GB、16GB、32GB、64GB多种规格。 |
  | 兼容开源版本 | DCS企业版完全兼容开源Redis 6。 |
  | 实例性能 | 高性能型单节点QPS约40万/秒，存储型单节点QPS约7万/秒。 |
  | 高可用与容灾 | 除单机实例外，其他类型的实例都提供Region内的跨可用区部署，实现实例内部节点间的电力、网络层面物理隔离。 |

#### DCS Memcached（已停售）

![](https://support.huaweicloud.com/productdesc-dcs/public_sys-resources/note_3.0-zh-cn.png) 

DCS Memcached已停售，建议使用Redis实例。

Memcached是一种内存Key-Value缓存系统，它支持简单字符串数据的存取，通常作为后端数据库内容缓存，以提升web的应用性能，降低对后端数据库的性能依赖，具体了解请参考[Memcached（已停售）典型应用场景](https://support.huaweicloud.com/productdesc-dcs/dcs-pd-200713002.html#dcs-pd-200713002__section351625761211)。

DCS全面兼容Memcached协议并增强实现了双机热备和数据持久化。

**表3** DCS Memcached灵活的实例配置

|  |  |
| --- | --- |
| 实例类型 | 提供单机、主备两种类型，分别适配不同的业务场景。  单机：适用于应用对可靠性要求不高、仅需要缓存临时数据的业务场景。单机实例支持读写高并发，但不做持久化，实例重启后原有缓存数据不会加载。  主备：包含一个主节点和一个备节点，主备节点的数据通过实时复制保持一致，备节点对用户不可见且不能直接读写数据，当主节点故障后，备节点自动升级为主节点。 |
| 内存规格 | 单机和主备实例均提供2G、4G、8G、16G、32G、64G共6种内存规格。 |
| 高可用与容灾 | 主备实例提供Region内的跨可用区部署，实现实例内部节点间的电力、网络层面物理隔离。 |

有关开源Memcached技术细节，您可以访问Memcached官方网站<https://memcached.org/>。

####
