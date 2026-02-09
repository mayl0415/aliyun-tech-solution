---
title: "API安全"
url: https://cloud.tencent.com/product/apism
category: "安全"
crawled_at: 2026-02-06T17:34:09.327466
---

# API安全

API安全（API Security and Management）聚焦API防御体系打造，支持资产全自动发现、敏感数据防泄露、API限流、异常事件管控闭环、实时流量分析报表等功能，联动腾讯Web应用防火墙、腾讯安全威胁情报、腾讯天御业务安全等能力，帮助企业全面识别API风险，针对性收敛API暴露面，构建全面、智能、精准的API全生命周期安全防御体系。

- [产品动态API安全2.0重磅发布，全面识别API风险](https://cloud.tencent.com/product/events/detail/3491)
- [产品动态敏感检测升级，支持内置规则及自定义规则](https://cloud.tencent.com/product/events/detail/4540)
- [产品动态事件检测升级，支持6大类API风险事件检测](https://cloud.tencent.com/product/events/detail/4992)

为什么要选择腾讯云API安全？

攻防对抗必备能力

[查看对抗案例](https://mp.weixin.qq.com/s?__biz=Mzg5OTE4NTczMQ==&mid=2247511231&idx=1&sn=ca5353b0b9c308bf18576fce1c8e874d&chksm=c055c193f72248852d9c10f12f8008ce97c2d60f0d6ac837ce8e2e1d0ca31f4809cf428c306d&mpshare=1&scene=1&srcid=0516jCYqhQXNWzRy1Yx56vXU&sharer_sharetime=1684231376090&sharer_shareid=858fde052c62a45f48134ca86bae2207&version=4.1.20.90880&platform=mac#rd)

1分钟

一键开启，无需二次接入

0改造

API资产全自动发现及分类

32种

覆盖32种API风险事件检测

19种

内置常用敏感信息检测

![](https://cloudcache.tencent-cloud.com/qcloud/ui/static/tc_portal_icon/aa141cdc-208b-4782-9b47-b6cba00075ad.png)

### 零部署，即开即用

针对已接入WAF的域名，一键即可开启API安全管控能力。针对未接入WAF的云上域名，支持自动发现，一键接入。

### 资产全自动发现

实时分析业务访问流量，自动发现API资产并动态梳理资产用途、变化。根据资产发现结果对资产功能场景、数据标签、活跃状态、鉴权情况打标分类。

### API接口限流

支持根据url、method、header参数等对不同接口、不同调用方等进行频率控制，帮助企业应对突发流量和恶意攻击，保护后端资源免受过载和滥用，提高系统的稳定性和可用性。

[技术分享](https://mp.weixin.qq.com/s/OFueM1Q3UijNvWLv9FL2CQ)

### 敏感数据防泄露

内置敏感数据识别规则，智能识别身份证、手机号等19种敏感参数信息，覆盖《个保法》提及的个人身份信息、财产信息、上网信息、位置信息等信息类型，且支持自定义敏感检测规则，防止敏感信息泄露，保障数据安全。

[技术分享](https://mp.weixin.qq.com/s/XkqN3fvjxOxfn9Rd3q9Q1Q)

### 异常事件管控闭环

持续检测API存在的各类安全风险，覆盖权限异常、账号异常、资源滥用、业务异常、涉敏异常、Web攻击等类型风险事件，帮助企业分级分类处置风险，一键添加专家建议的处置规则，助力安全事件快速闭环，降低业务安全风险。

### API流量分析

总览企业的API 资产、API 活跃程度、API 涉敏情况、API 风险事件及变化趋势，助力企业可视化管理API全生命周期防护，及时感知并处置威胁。

- API资产全生命周期管理
- API资产风险管理
- 敏感数据管控
- API限流

场景四：如何通过「API限流」防止服务“雪崩”

通过设定合理的阈值，限制每个用户或每个接口的请求频率，企业可以保护后端资源免受过载和滥用，提高系统的稳定性和可用性。

建议增加API限流策略的业务场景

- 活动保障：在大促秒杀、抢票抢券等活动场景，由于准确预估活动热度很困难，可以针对关键接口配置限速，拒绝超出访问阈值的访问或采取排队策略，避免后端崩溃。
- 关键接口防护：突发攻击往往防不胜防，一方面可以通过CC、BOT策略对抗复杂攻击，另一方面可以针对关键域名/接口可以配置兜底限速策略。
- 对不同服务对象限速：针对多个服务的客户共享后端资源的场景，多个服务对象间做好资源隔离是较好的方案，但是往往处于节约资源及成本控制的考虑较难实施，可以针对不同的调用方设置服务/接口的调用限速策略，避免雪崩影响其他用户。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/M9dyHFRXKEIZkCicSq7uH.svg)

[### 计费模式

API安全提供预付费（包年包月）购买能力，不同版本的实例开启API安全价格不同。](https://cloud.tencent.com/document/product/627/11730#c919ab48-d8a4-435d-adad-17792af7f375)

[### 操作指引

帮助您快速了解、创建并使用腾讯云API安全。](https://cloud.tencent.com/document/product/627/90623)

我们致力于为您提供个性化的售前购买咨询服务，以及全面的技术售后服务。

