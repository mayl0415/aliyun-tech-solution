---
title: "客户运营能力API简介"
code: "oce"
category: "用户服务"
source_url: "https://support.huaweicloud.com/api-oce/zh-cn_topic_0075195195.html"
crawled_at: "2026-02-05T16:56:11.164919"
---

# 客户运营能力API简介

## 产品简介

面向客户开放，支持多种交易运营能力

## 详细说明

# 客户运营能力API简介

华为云面向客户开放运营能力，用于支撑客户平台管理产品、管理账户、管理交易、管理账单、管理企业、管理配置信息、管理工单等场景。

**表1** API列表和描述

| **场景** | **子场景** | **API名称** | **API说明** |
| --- | --- | --- | --- |
| 管理产品 | 查询产品信息 | [查询云服务类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256679455.html) | 客户在自建平台查询云服务类型的列表。 |
| [查询资源类型列表](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001256519451.html) | 客户在自建平台查询资源类型的列表。 |
| [根据云服务类型查询资源列表](https://support.huaweicloud.com/api-oce/qct_00003.html) | 客户在自建平台根据云服务类型查询关联的资源类型编码和名称，用于查询按需产品的价格或包年/包月产品的价格。 |
| [查询使用量类型列表](https://support.huaweicloud.com/api-oce/qct_00004.html) | 客户在自建平台查询资源的使用量类型列表。 |
| [查询度量单位列表](https://support.huaweicloud.com/api-oce/qct_00006.html) | 客户在自建平台上查询资源使用量，包年包月资源的时长及金额的度量单位及名称，度量单位类型等。 |
| [查询度量单位进制](https://support.huaweicloud.com/api-oce/qct_00007.html) | 客户在自建平台上查询度量单位的进制转换信息，用于不同度量单位之间的转换。 |
| 查询商品价格 | [查询按需产品价格](https://support.huaweicloud.com/api-oce/bcloud_01001.html) | 客户在自建平台按照条件查询按需产品的价格。 |
| [查询包年/包月产品价格](https://support.huaweicloud.com/api-oce/bcloud_01002.html) | 客户在自建平台按照条件查询包年/包月产品开通时候的价格。 |
| [查询包年/包月资源的续订金额](https://support.huaweicloud.com/api-oce/bcloud_01007.html) | 客户在自建平台按照条件查询包年/包月资源续订时候的续订金额。 |
| 管理账户 | 管理账户 | [查询账户余额](https://support.huaweicloud.com/api-oce/mac_00001.html) | 客户可以查询自身的账户余额。 |
| [查询储值卡列表](https://support.huaweicloud.com/api-oce/mac_00002.html) | 客户可以查询已购买的储值卡列表。 |
| [查询收支明细](https://support.huaweicloud.com/api-oce/mac_00003.html) | 客户可以查询自身的收支明细情况。 |
| 管理交易 | 管理优惠券 | [查询优惠券列表](https://support.huaweicloud.com/api-oce/mp_02001.html) | 客户可以查询自身的优惠券信息。 |
| [查询优惠券收支明细](https://support.huaweicloud.com/api-oce/mp_02007.html) | 客户可以查询自身优惠券的收支明细情况。 |
| 管理包年/包月订单 | [查询订单列表](https://support.huaweicloud.com/api-oce/api_order_00013.html) | 客户购买包年/包月资源后，可以查看待审核、处理中、已取消、已完成和待支付等状态的订单。 |
| [查询订单详情](https://support.huaweicloud.com/api-oce/api_order_00014.html) | 客户可以在客户自建平台查看订单详情。 |
| [查询订单可用优惠券](https://support.huaweicloud.com/api-oce/api_order_00015.html) | 客户在自建平台查看订单可用的优惠券列表。 |
| [查询订单可用折扣](https://support.huaweicloud.com/api-oce/api_order_00025.html) | 客户在自建平台支付待支付订单时，查询可使用的折扣信息。 |
| [支付包年/包月产品订单](https://support.huaweicloud.com/api-oce/api_order_00030.html) | 客户可以对待支付状态的包年/包月产品订单进行支付。 |
| [取消待支付订单](https://support.huaweicloud.com/api-oce/api_order_00017.html) | 客户可以对待支付的订单进行取消操作。 |
| [查询退款订单的金额详情](https://support.huaweicloud.com/api-oce/api_order_00020.html) | 客户在客户销售平台查询某次退订订单或者降配订单的退款金额所属资源类型和对应订单。 |
| 管理包年/包月资源 | [查询客户包年/包月资源列表](https://support.huaweicloud.com/api-oce/api_order_00021.html) | 客户在自建平台查询某个或所有的包年/包月资源。 |
| [续订包年/包月资源](https://support.huaweicloud.com/api-oce/api_order_00018.html) | 客户在自建平台完成包年/包月资源的续订。 |
| [退订包年/包月资源](https://support.huaweicloud.com/api-oce/api_order_00019.html) | 客户购买包年/包月资源后，支持客户退订包年/包月实例。退订资源实例包括资源续费部分和当前正在使用的部分，退订后资源将无法使用。 |
| [设置包年/包月资源自动续费](https://support.huaweicloud.com/api-oce/api_order_00022.html) | 为防止资源到期被删除，客户可为长期使用的包年/包月资源开通自动续费。 |
| [取消包年/包月资源自动续费](https://support.huaweicloud.com/api-oce/api_order_00023.html) | 客户设置自动续费后，还可以执行取消自动续费的操作。关闭自动续费后，资源到期将不会被自动续费。 |
| [设置或取消包年/包月资源到期转按需](https://support.huaweicloud.com/api-oce/api_order_00024.html) | 客户可以设置包年/包月资源到期后转为按需资源计费。包年/包月计费模式到期后，按需的计费模式即生效。 |
| [设置包年/包月资源自动续费扣款日和续费后资源统一到期日](https://support.huaweicloud.com/api-oce/api_order_00031.html) | 客户的包年/包月资源可进行设置自动续费扣款日和续费后统一到期日。 |
| 管理资源包 | [查询资源包列表](https://support.huaweicloud.com/api-oce/api_order_00027.html) | 客户在自建平台查询资源包列表。 |
| [查询资源包使用量](https://support.huaweicloud.com/api-oce/api_order_00028.html) | 客户在自建平台根据资源项维度查询资源包使用量。 |
| [查询资源包使用明细](https://support.huaweicloud.com/api-oce/api_order_00029.html) | 客户在自建平台查询资源包使用明细。 |
| 管理账单 | 管理账单 | [查询汇总账单](https://support.huaweicloud.com/api-oce/mbc_00008.html) | 客户在自建平台查询自身的消费汇总账单，此账单按月汇总消费数据。 |
| [查询资源详单](https://support.huaweicloud.com/api-oce/mbc_00003.html) | 客户在自建平台查询自己的资源详单，用于反映各类资源的消耗情况。 |
| [查询资源消费记录](https://support.huaweicloud.com/api-oce/mbc_00004.html) | 客户在自建平台查询每个资源的消费明细数据。 |
| [查询流水账单](https://support.huaweicloud.com/api-oce/mbc_00007.html) | 客户在自建平台查询自己的消费流水账单。 |
| 查询95计费资源用量 | [查询95计费资源用量汇总](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001144806706.html) | 客户在自建平台查询自己的资源使用量汇总。 |
| [查询95计费资源用量明细](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001190606757.html) | 客户在自建平台查询自己的资源使用量明细。 |
| 管理成本 | 管理成本 | [查询月度成本](https://support.huaweicloud.com/api-oce/mbc_00010.html) | 客户在自建平台查询指定月份的月度摊销成本。 |
| [查询成本数据](https://support.huaweicloud.com/api-oce/costm_00014.html) | 客户在自建平台查询成本分析数据。 |
| 管理企业 | 管理企业项目 | [开通客户企业项目权限](https://support.huaweicloud.com/api-oce/ep_00022.html) | 客户在自建平台开通客户企业项目权限。 |
| 管理企业多账号 | [查询企业组织结构](https://support.huaweicloud.com/api-oce/ep_00020.html) | 企业主账号在自建平台查询企业组织结构。 |
| [查询企业子账号列表](https://support.huaweicloud.com/api-oce/ep_00021.html) | 企业主账号在自建平台查询企业子账号信息列表。 |
| [查询企业主账号可拨款余额](https://support.huaweicloud.com/api-oce/ep_00018.html) | 企业主账号在自建平台查询自己的可拨款余额。 |
| [查询企业子账号可回收余额](https://support.huaweicloud.com/api-oce/ep_00019.html) | 企业主账号在自建平台查询企业子账号的可回收余额。 |
| [创建企业子账号](https://support.huaweicloud.com/api-oce/ep_00023.html) | 企业主账号在自建平台创建企业子账号。 |
| [发送短信验证码](https://support.huaweicloud.com/api-oce/ep_00014.html) | 企业主账号在自建平台发送短信验证码。 |
| [企业主账号向企业子账号拨款](https://support.huaweicloud.com/api-oce/ep_00016.html) | 企业主账号在自建平台向企业子账号拨款。 |
| [企业主账号从企业子账号回收拨款](https://support.huaweicloud.com/api-oce/ep_00017.html) | 企业主账号在自建平台回收给企业子账号的拨款。 |
| [查询企业主账号可拨款优惠券列表](https://support.huaweicloud.com/api-oce/ep_00024.html) | 企业主账号在自建平台查询自己的可拨款优惠券列表。 |
| [查询企业子账号可回收优惠券列表](https://support.huaweicloud.com/api-oce/ep_00025.html) | 企业主账号在自建平台查询企业子账号的可回收优惠券。 |
| [企业主账号向企业子账号拨款优惠券](https://support.huaweicloud.com/api-oce/ep_00026.html) | 企业主账号在自建平台向企业子账号拨款优惠券。 |
| [企业主账号从企业子账号回收优惠券](https://support.huaweicloud.com/api-oce/ep_00027.html) | 企业主账号在自建平台回收给企业子账号的拨款优惠券。 |
| 管理配置信息 | 查询国家省市信息 | [查询省份信息](https://support.huaweicloud.com/api-oce/mpf_02001.html) | 客户在自建平台上查询省份信息。 |
| [查询城市信息](https://support.huaweicloud.com/api-oce/mpf_02002.html) | 客户在自建平台上查询城市信息。 |
| [查询区县信息](https://support.huaweicloud.com/api-oce/mpf_02003.html) | 客户在自建平台上查询区县信息。 |
| 管理工单 | [管理工单](https://support.huaweicloud.com/api-oce/mw_00000.html) | [工单管理API参考](https://support.huaweicloud.com/api-ticket/ticket_api_00006.html) | 客户可以在客户自建平台上提交华为云工单，华为云售后服务团队收到工单后会协助客户处理使用华为云过程中遇到的问题。 |

####
