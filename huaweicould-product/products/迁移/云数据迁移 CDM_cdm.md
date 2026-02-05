---
title: "什么是云数据迁移"
code: "cdm"
category: "迁移"
source_url: "https://support.huaweicloud.com/productdesc-cdm/cdm_01_0143.html"
crawled_at: "2026-02-05T16:37:04.884920"
---

# 什么是云数据迁移

## 产品简介

提供同/异构数据源之间批量数据迁移服务

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-cdm/public_sys-resources/note_3.0-zh-cn.png)

![图片2](https://support.huaweicloud.com/productdesc-cdm/zh-cn_image_0000001218704193.png)

## 详细说明

# 什么是云数据迁移

#### 产品定义

云数据迁移（Cloud Data Migration, 简称CDM），是一种高效、易用的数据集成服务。 CDM围绕大数据迁移上云和智能数据湖解决方案，提供了简单易用的迁移能力和多种数据源到数据湖的集成能力，降低了客户数据源迁移和集成的复杂性，有效地提高您数据迁移和集成的效率。

在数据治理中心（DataArts Studio）服务中，CDM作为其中的“数据集成”组件使用，产品能力与独立的CDM服务保持一致。因此，后文中的“云数据迁移”、“数据集成”均指CDM服务。

![](https://support.huaweicloud.com/productdesc-cdm/public_sys-resources/note_3.0-zh-cn.png) 

当前DataArts Studio已提供全新的离线集成作业能力。离线集成作业作为数据开发组件的一个作业类型，支持跨集群下发数据集成作业，实现常用的批作业迁移能力。

相比于传统的依靠CDM集群进行生命周期管理CDM迁移作业，离线集成作业依靠数据开发组件的生命周期管理，由数据开发进行集成作业的统一调度和CDM集群资源的统一支配，作业运行可靠性更高、使用体验更佳，推荐您使用离线集成作业替代传统的CDM迁移作业。关于离线集成作业的更多介绍，请您参考[离线集成作业概述](https://support.huaweicloud.com/usermanual-dataartsstudio/dataartsstudio_01_1515.html)。

CDM服务基于分布式计算框架，利用并行化处理技术，支持用户稳定高效地对海量数据进行移动，实现不停服数据迁移，快速构建所需的数据架构。

**图1** CDM定位
  
![](https://support.huaweicloud.com/productdesc-cdm/zh-cn_image_0000001218704193.png "点击放大")

#### 产品功能

* **表/文件/整库迁移**

  支持批量迁移表或者文件，还支持同构/异构数据库之间整库迁移，一个作业即可迁移几百张表。
* **增量数据迁移**

  支持文件增量迁移、关系型数据库增量迁移、HBase/CloudTable增量迁移，以及使用Where条件配合时间变量函数实现增量数据迁移。
* **事务模式迁移**

  支持当CDM作业执行失败时，将数据回滚到作业开始之前的状态，自动清理目的表中的数据。
* **字段转换**

  支持去隐私、字符串操作、日期操作等常用字段的数据转换功能。
* **文件加密**

  在迁移文件到文件系统时，CDM支持对写入云端的文件进行加密。
* **MD5校验一致性**

  支持使用MD5校验，检查端到端文件的一致性，并输出校验结果。
* **脏数据归档**

  支持将迁移过程中处理失败的、被清洗过滤掉的、不符合字段转换或者不符合清洗规则的数据单独归档到脏数据日志中，便于用户查看。并支持设置脏数据比例阈值，来决定任务是否成功。

####
