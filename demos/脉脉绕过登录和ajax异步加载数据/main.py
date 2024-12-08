"""
爬取脉脉网站的职言数据 

爬取技术：
1. 需要登录才能访问
    使用人工登录+获取cookie的方式绕过登录
2. 需要Ajax异步加载数据
    通过network抓包得到结果

maimai.cn 扫码人工登录
职言中，下拉加载更多数据，但url不变，通过network抓包得到结果
（fetch/xhr是异步请求的意思）
"""

import requests
from bs4 import BeautifulSoup

url = "https://maimai.cn/sdk/web/content/get_list"

payloads = {
    "api": "gossip/v3/square",
    "u": "1515483",
    "page": 7,
    "before_id": 0
} 

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
    "cookie": "mmsid=2021050516340000a
}

# cookies 表示登录用户的身份

resp = requests.get(url, params=payloads) 