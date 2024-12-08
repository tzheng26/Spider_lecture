# 爬取https://tianqi.2345.com/wea_history/54511.htm网站北京十年历史天气数据
# url不变，从后台抓取数据。通过“检查”-Network抓包
import requests
import pandas as pd

url = "https://tianqi.2345.com/Pc/GetHistory" # ？后面的参数在payload中

headers = {
    "User-Agent": """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"""
}

def craw_table(year, month):
    """提供年月，返回该月的天气数据表格"""
    payload = {
        "areaInfo[areaId]": 54511,
        "areaInfo[areaType]": 2,
        "date[year]": year,
        "date[month]": month
    }
    response = requests.get(url, headers=headers, params=payload)
    # print(response.status_code)
    # print(response.text) # 返回的是json数据
    data = response.json()["data"]
    # print(data)

    # dataframe
    df = pd.read_html(data)[0] # 读取html <table>表格
    # print(df.head()) # 阅读前5行
    return df

df_list = []
for year in range(2011,2024):
    for month in range(1,13):
        print("爬取：", year, month)
        df = craw_table(year, month)
        df_list.append(df)

df = pd.concat(df_list).to_excel("北京天气历史数据.xlsx", index=False)  
