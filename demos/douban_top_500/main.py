import requests
from bs4 import BeautifulSoup
import pprint
import json
import pandas as pd

page_indexs = range(0, 250, 25)
# list(page_indexs)

def download_all_htmls():
    """
    下载所有列表页面的HTML，用于后续的分析
    """
    htmls = []
    for idx in page_indexs:
        url = f"https://movie.douban.com/top250?start={idx}&filter="
        print("craw html:", url)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            raise Exception(f"error: {r.status_code}")
        htmls.append(r.text)
    return htmls
    
htmls = download_all_htmls()
# print(htmls[0])

def parse_single_html(html):
    """
    解析单个HTML，得到数据
    @return list({"link","title",[label]})
    """
    soup = BeautifulSoup(html, "html.parser")
    article_items = (soup.find("div", class_="article")
                     .find("ol", class_="grid_view")
                     .find_all("div", class_="item"))
    datas = []
    for article_item in article_items:
        rank = article_item.find("div", class_="pic").find("em").get_text()
        info = article_item.find("div", class_="info")
        title = info.find("div", class_='hd').find("span", class_="title").get_text()
        stars = info.find("div", class_="bd").find("div", class_="star").find_all("span")
        rating_star = stars[0]["class"][0]
        rating_num = stars[1].get_text()
        comments = stars[3].get_text()

        datas.append({
            "rank": rank,
            "title": title,
            "rating_star": rating_star.replace("rating", "").replace("-t",""),
            "rating_num": rating_num,
            "comments": comments.replace("人评价", "")
        })
    return datas

pprint.pprint(parse_single_html(htmls[0]))

# 执行所有的HTML页面的解析
all_datas = []
for html in htmls:
    all_datas.extend(parse_single_html(html))

# 将结果存入excel
df = pd.DataFrame(all_datas)
print(df)
df.to_excel("豆瓣电影Top250.xlsx")