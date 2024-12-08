import requests
from bs4 import BeautifulSoup

def get_novel_chapters():
    root_url = "http://www.89wxw.cn/0_9/"
    r = requests.get(root_url)
    r.encoding = "gbk" 
    soup = BeautifulSoup(r.text, "html.parser")

    data = []
    for dd in soup.find_all("dd"):
        link = dd.find("a")
        if not link:
            continue
        data.append(("http://www.89wxw.cn%s"%link["href"], link.get_text()))
    return data 
 
def get_chapter_content(url):
    r = requests.get(url)
    r.encoding = "gbk" 
    soup = BeautifulSoup(r.text, "html.parser")
    content = soup.find("div", id="content").get_text()
    return content 

novel_chapters = get_novel_chapters()
total_cnt = len(novel_chapters)
idx = 0
for chapter in novel_chapters ():
    url, title = chapter 
    idx += 1
    print(idx, "/", total_cnt, chapter[1]) 
    with open("%s.txt"%title, "w") as f:
        f.write(get_chapter_content(url)) 