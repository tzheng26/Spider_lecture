from bs4 import BeautifulSoup

with open("./test.html") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')

div_node = soup.find("div", id="content")
print(div_node)
print("#"*30)

links = div_node.find_all('a')
for link in links:
    print(link.name, link["href"], link.get_text())

img = div_node.find("img")
print(img["src"]) 