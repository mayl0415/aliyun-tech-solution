---
title: "什么是设备接入IoTDA"
code: "iothub"
category: "IoT物联网"
source_url: "https://support.huaweicloud.com/productdesc-iothub/iot_04_0002.html"
crawled_at: "2026-02-05T16:52:57.749930"
---

# 什么是设备接入IoTDA

## 产品简介

安全可靠接入海量设备

## 产品图片

![图片1](https://support.huaweicloud.com/productdesc-iothub/figure/zh-cn_image_0000001130147031.png)

## 详细说明

# 什么是设备接入IoTDA

华为云物联网平台设备接入云服务（IoTDA）提供海量设备的接入和管理能力，将物理设备连接到云，支撑设备数据采集上云和云端下发命令给设备进行远程控制，配合华为云其他产品，帮助您快速构筑物联网解决方案。

使用物联网平台构建一个完整的物联网解决方案主要包括3部分：物联网平台、业务应用和设备。

* 物联网平台作为连接业务应用和设备的中间层，屏蔽了各种复杂的设备接口，实现设备的快速接入；同时提供强大的开放能力，支撑行业用户构建各种物联网解决方案。
* 设备可以通过固网、2G/3G/4G/5G、NB-IoT、Wifi等多种网络接入物联网平台，并使用LWM2M/CoAP、MQTT、HTTPS等主流协议或行业协议将业务数据上报到平台，平台也可以将控制命令下发给设备。
* 业务应用通过调用物联网平台提供的API，实现设备数据采集、命令下发、设备管理等业务场景。

**图1** 物联网解决方案
  
![](https://support.huaweicloud.com/productdesc-iothub/figure/zh-cn_image_0000001130147031.png "点击放大")

#### 视频介绍

[![](https://support.huaweicloud.com/productdesc-iothub/figure/zh-cn_image_0000002378549601.jpg)](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/support/iothub-video/1726195831641236580.mp4)

#### 设备接入IoTDA特性

物联网平台支持终端设备直接接入，也可以通过工业网关或者家庭网关接入。物联网平台支持多网络接入、多协议接入、系列化Agent接入，解决设备接入复杂多样化和碎片化难题，也提供了丰富完备的设备管理能力，简化海量设备管理复杂性，提升管理效率。IoT设备接入云服务支持的特性详见下表。

**表1** IoT设备接入云服务支持特性

| 特性分类 | 功能特性 | 功能说明 |
| --- | --- | --- |
| 设备接入 | 原生协议接入 | 支持MQTT/CoAP/LwM2M/HTTPS协议接入。 |
| 系列化Device SDK | 支持IoT Device SDK和IoT Device SDK Tiny，覆盖的语言包括C、Java等。详情请参考[IoT Device SDK介绍](https://support.huaweicloud.com/sdkreference-iothub/iot_02_0178.html)。 |
| 行业协议接入 | 支持通过边缘网关接入Modbus、OPCUA，可通过行业协议插件方式支持行业协议接入。 |
| 设备接入鉴权 | 支持一机一密，X.509证书等鉴权方式。 |
| [泛协议接入](https://support.huaweicloud.com/usermanual-iothub/iot_01_0125.html) | 提供开源SDK和技术框架，需用户自行部署云网关完成TCP协议转换，或部署协议驱动到边缘网关。 |
| 设备管理 | 设备全生命周期管理 | 设备增删改查、设备状态管理、设备冻结/解冻、子设备管理等。 |
| 设备群组与标签 | 支持对设备进行分组或打标签，详细请参见[群组与标签](https://support.huaweicloud.com/usermanual-iothub/iot_01_0020.html)。 |
| 设备物模型定义 | 对设备进行物模型定义（Product Model），详细请参见[产品模型](https://support.huaweicloud.com/devg-iothub/iot_01_0017.html)。 |
| 设备影子 | 支持影子数据查询和影子设置，详细请参见[设备影子](https://support.huaweicloud.com/usermanual-iothub/iot_01_0049.html)。 |
| OTA升级 | 支持对设备软固件进行升级，详细请参考[OTA升级](https://support.huaweicloud.com/usermanual-iothub/iot_01_0155.html)。 |
| 设备文件上传 | 支持设备上传文件到OBS，设备可向云端请求文件，详细请参见[文件上传](https://support.huaweicloud.com/usermanual-iothub/iot_01_0033.html)。 |
| 设备批量操作 | 支持对设备的批量操作，包括[批量创建设备](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)、[批量软固件升级](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)和[批量命令下发](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)。 |
| 消息通信 | 双向消息透传 | 支持设备消息HTTP/AMQP推送到应用服务器，支持应用侧向设备以异步方式下发消息。 |
| 物模型Topic通信 | 应用侧和设备侧基于物模型定义的属性、命令和事件进行解耦通信。 |
| 自定义Topic通信 | 支持用户自定义Topic进行双向消息通信。 |
| 数据解析转换 | 在线开发编解码插件，对设备数据进行数据解析和格式转换。 |
| 命令下发 | 支持以同步方式向在线设备下发命令，NB场景支持异步方式下发命令，详细请参见[命令下发](https://support.huaweicloud.com/usermanual-iothub/iot_01_0051.html)。 |
| 规则引擎 | 数据流转 | 支持数据流转到华为云Kafka/OBS/GaussDB/DIS/DMS/ROMA等服务，详细请参见[规则引擎](https://support.huaweicloud.com/usermanual-iothub/iot_01_0022.html)。 |
| 规则联动 | 支持建立设备联动规则，实现联动控制，详细请参见[规则引擎](https://support.huaweicloud.com/usermanual-iothub/iot_01_0022.html)。 |
| 数据转发 | 支持平台将设备上报数据通过HTTP或AMQP转发至应用服务器。 |
| 监控运维 | 日志能力 | 控制台提供消息跟踪功能，对接LTS提供日志分析能力，对接CTS提供审计日志功能，详细请参见[监控运维](https://support.huaweicloud.com/usermanual-iothub/iot_01_0030.html)。 |
| 告警能力 | 系统类告警（如阈值类告警）和设备规则触发告警对接AOM提供告警通知管理能力，详细请参见[告警管理](https://support.huaweicloud.com/usermanual-iothub/iot_01_0030_3.html)。 |
| 指标监控 | 租户级业务指标（如设备状态、命令、订阅推送、消息流转等）对接AOM提供监控报表能力，详细请参见[查看报表](https://support.huaweicloud.com/usermanual-iothub/iot_01_0030_1.html)。 |
| 设备发放 | 设备启动引导 | 通过Bootstrap流程，引导物联网设备在初次上电时获得正确的目标物联网平台地址，继而完成设备与平台的建链过程。 |
| 多种发放策略 | 支持多种智能发放策略，比如关键字模糊匹配，使用证书进行发放，自定义发放策略等。 |
| 设备迁移能力 | 设备迁移能力，根据业务迁移需要，帮助企业重置设备发放信息，实现更改对端物联网平台的目的。 |

#### 安全&数据保护

已获国家安全等保2.0四级认证，通过ISO27001/ISO27017/ ISO27018/CSA STAR国际安全认证，数据隐私保护遵从中国《个人信息保护法》、欧盟GDPR数据隐私保护要求，建立端到端可信的安全体系。

* 设备安全：提供一机一密的设备安全认证机制，防止设备非法接入，支持设备的安全检测。
* 信息传输安全：基于TLS、DTLS、DTLS+加密协议，提供安全的传输通道。
* 平台安全：基于华为云整体进行威胁防御，充分利用华为云安全服务/组件和华为的安全研究部门，建立安全分析、设计、编码、测试、安全攻防等一整套安全防御体系。
* 数据保护：满足中国《个人信息保护法》、欧盟GDPR数据隐私保护要求。

#### IoT边缘

[IoT边缘](https://support.huaweicloud.com/iotedge/index.html)作为物联网边缘“小脑”，在靠近物或数据源头的边缘侧，融合网络、计算、存储、应用核心能力的开放平台，就近提供计算和智能服务，满足行业在实时业务、应用智能、安全与隐私保护等方面的基本需求。

#### 全球SIM联接

可实现设备在全球范围，通过定量流量、空中写卡和远程设备发放技术，实现就近华为公有云站点可靠接入，并享受当地资费套餐，详情请参考[全球SIM联接](https://support.huaweicloud.com/qs-ocgsl/oceanlink_03_0001.html)。

####
