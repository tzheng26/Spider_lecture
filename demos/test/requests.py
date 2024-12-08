# 内容下载
import requests

url="http://www.crazyant.net"

r = requests.get(url)

# 输出状态码,200表示请求成功
# 400：Bad Request，表示请求无法被服务器理解或无法完成请求。
# 401：Unauthorized，表示请求需要用户验证。
# 403：Forbidden，表示服务器理解请求，但是拒绝执行它。
# 404：Not Found，表示请求的资源无法在服务器上找到。
# 500：Internal Server Error，表示服务器遇到了一个未知的错误。
print(r.status_code)

# 输出编码格式, 从headers中识别，识别不出默认为ISO-8859-1，可以通过r.encoding手动设置，根据r.text的内容 head中的meta信息设置。
r.encoding

# 输出页面内容
print(r.text)



