---
title: "智算存储 NitroFS"
url: https://cloud.tencent.com/product/nitrofs
category: "存储"
crawled_at: 2026-02-06T17:23:25.980134
---

# 智算存储 NitroFS

智算存储 NitroFS 是腾讯云为大模型训练、推理等场景提供的高性能存储服务。提供 POSIX、KV 等多种访问接口，并通过端到端 RDMA 、富客户端等技术，提供TB级吞吐和亚毫秒级延迟。满足大模型 checkpoint 读写、KVCache 存储等场景的关键存储需求。

[立即申请](https://cloud.tencent.com/online-service?source=PRESALE&from=sales_console_bar_overview)

99.95%

SLA 服务可用性不低于99.95%

1000万

可支持1000万的IOPS性能

TB/s

可提供TB级吞吐

200PiB

单实例最大支持200PiB的超大空间

### 富客户端

通过本地数据路由缓存感知，数据读写时从客户端一跳直达存储节点。

### 多种接口支持

支持类 POSIX 文件语义、KV等多种接口，为AI业务提供高性能的存储服务。

### 全链路零拷贝

提供端到端的 RDMA 能力，且无网关转发。
数据可直通底层存储服务器，提供亚毫秒级的延迟和TB级的吞吐能力。

### 分块 KV 存储引擎

存储内置 KV 引擎，数据分块读写场景时，仅跟元数据服务交互1次。

### 数据流动能力

支持与对象存储对接，透明接管对象存储。
并支持自动化的淘汰和预热策略。

### 高级功能丰富

支持快照、权限管理、配额等文件系统常用高级功能。

### 卓越性能

基于 RDMA 、富客户端等技术，可支持TB级的吞吐和亚毫秒级时延。

### 多协议支持

支持类 POSIX 文件语义、KV 等多种接口。为 AI 业务场景提供一站式的存储服务。

### 稳定可靠

由腾讯内 KVCache 存储和大模型存储孵化而来，具备成熟的产品方案和实践经验。

通过高速的 RDMA 网络连接客户端和服务端。

无接入节点层，客户端一跳直达存储后端。

采用非对称架构，提供单独的数据节点和元数据节点。

支持与对象存储进行数据流动，形成整体解决方案。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/5tz8eaUG7kjR5DrUUBrB3.png)

### 相关云产品

[![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/ZYhyQZtq-sFh-rjCbdCoU.png)

GPU 云服务器](https://cloud.tencent.com/product/gpu)

[![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/tkCYkHfhWNkHZ9XkA5eog.png)

VPC 网络](https://cloud.tencent.com/product/vpc)

[![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/xzXur_MOYKvRv0wns6JeE.png)

对象存储](https://cloud.tencent.com/product/cos)

- 大模型训练
- 大模型推理 KVCache
- 自动驾驶

自动驾驶

自动驾驶涉及海量小样本的读取，需要存储有足够低的延迟和极强的元数据性能，并且会需要和对象存储的生态进行打通，满足不同流程的训练需求。智算存储 NitroFS 可作为自动驾驶存储，加速训练场景下，海量小文件的样本读取。

我们的能力

- 支持端到端 RDMA 能力，且数据读写时从客户端一跳直达存储节点，大幅降低访问时延，并提升访问效率。
- 支持与对象存储对接，透明接管对象存储。 并支持自动化的淘汰和预热策略。

![](https://qcloudimg.tencent-cloud.cn/trisys/assets/product/images/Uthb17222CDMLvM5vRWVF.png)

1. 此页提到的智算存储 NitroFS 的产品数据，均来源于腾讯内部实验室，统计时间为2025年5月。
2. 此产品正在邀测中，敬请期待。

[联系我们](https://cloud.tencent.com/online-service?source=PRESALE&from=sales_console_bar_overview)
