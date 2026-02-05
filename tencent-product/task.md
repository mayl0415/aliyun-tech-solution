爬取腾讯云产品架构页面

页面为
https://cloud.tencent.com/product
数据来源为，产品链接以https://cloud.tencent.com/product/** 开头的页面
https://qcloudimg.tencent-cloud.cn/scripts/qccomponents/v2/full-nav-tree.json

样例
 {
                                        "id": "pPYkYxVdi",
                                        "type": "entry",
                                        "dictId": "2169",
                                        "dictType": "product",
                                        "pid": "ZRGIgAQtZ",
                                        "link": "https://cloud.tencent.com/product/iothub",
                                        "title": "物联网通信",
                                        "slug": "iothub",
                                        "desc": "帮助开发者快速搭建物联网应用平台",
                                        "description": "安全、稳定、高效的物联网通信连接平台，助力您快速实现设备-应用-云服务间数据通信",
                                        "l4ProductScope": [
                                            "topNav",
                                            "productOverview"
                                        ],
                                        "children": []
                                    },


你可以请求数据来源接口，然后根据数据来源接口中的链接，去爬取每个产品的页面，保存为md文件，保存图片链接地址

按产品分类组织文件结构
注意链接地址需要去重
最后所有md文件保存完毕后，删除所有重复的图片
