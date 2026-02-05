---
title: "什么是云存储网关"
code: "csg"
category: "存储"
source_url: "https://support.huaweicloud.com/productdesc-csg/csg_01_0002.html"
crawled_at: "2026-02-05T16:27:59.688314"
---

# 什么是云存储网关

## 产品简介

为企业应用提供标准的文件存储访问入口

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-csg/zh-cn_image_0166619804.png)

## 详细说明

# 什么是云存储网关

云存储网关（Cloud Storage Gateway，CSG）是一种混合云存储服务。用户本地数据中心的应用程序通过标准存储协议（NFS协议）访问网关，连接到华为云，实现用户本地和华为云存储数据的同步管理。

用户只需在本地部署网关，通过NFS协议将数据缓存到本地，再定期同步到华为云OBS存储。数据上云后，可通过OBS生命周期管理，将数据存储在低频访问存储或归档存储桶中，降低存储成本，在使用数据时再从低频访问存储或归档存储桶中读取；同时通过协议接口，NFS客户端可反向同步OBS中的已有对象到本地。通过CSG可实现数据无缝上下云，简化用户本地存储，解决本地数据冗余的问题。

**图1** CSG架构示意图
  
![](https://support.huaweicloud.com/productdesc-csg/zh-cn_image_0166619804.png "点击放大")

####
