"""
爬取图片并下载
url: https://pic.netbian.com/4kmeinv/
爬取网页 requests
解析网页 BeautifulSoup
"""
import requests
from bs4 import BeautifulSoup
import os


# 获取网页源代码
# url = "https://pic.netbian.com/4kmeinv/"

def craw_html(url):
    r = requests.get(url)
    r.encoding = "gbk"   
    print(r.status_code) # 200说明没有反爬机制

    html = r.text
    # print(html) 
    return html  

def parse_and_download(html): 
    # 解析图片地址
    soup = BeautifulSoup(html, "html.parser")
    imgs = soup.find_all("img")
    for img in imgs:
        src = img["src"]
        if "/uploads/" not in src:
            continue
        src = f"https://pic.netbian.com{src}"
        print(src )

        # 获取图片本地文件地址
        filename = os.path.basename(src)
        with open(f"美女图片/{filename}", "wb") as f:
            r_img = requests.get(src)
            f.write(r_img.content)  # r.content是二进制数据

# 0-10页
urls = ["https://pic.netbian.com/4kmeinv/"] + [f"https://pic.netbian.com/4kmeinv/index_{i}.html" for i in range(2,11)]

for url in urls:
    print("#### 正在爬取：", url )
    html = craw_html(url)
    parse_and_download(html)  # 下载图片
 