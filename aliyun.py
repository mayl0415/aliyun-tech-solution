import os
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526 import DescribeInstanceTypesRequest

# 从环境变量获取凭据
access_key_id = os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_ID")
access_key_secret = os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_SECRET")

if not access_key_id or not access_key_secret:
    print("错误: 请先设置环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET")
    exit(1)

# 初始化 Client
client = AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')

request = DescribeInstanceTypesRequest.DescribeInstanceTypesRequest()
# DescribeInstanceTypesRequest 在 V1.0 SDK 中可能不支持 set_PageSize，直接查询即可

try:
    response = client.do_action_with_exception(request)
    # response 是 bytes 类型，需要转为字符串
    print(str(response, encoding='utf-8'))
except Exception as e:
    print(f"调用失败: {e}")