import requests

# 测试拼多多可用链接
# 0-13

key = '耳机'
url = 'http://apiv3.yangkeduo.com/api/alexa/v1/goods?&page=13&size=20&list_id=DE8ysp8KuO'
# url = 'http://apiv3.yangkeduo.com/api/alexa/v1/goods?&page=26'

r = requests.get(url)

print(r.text)
