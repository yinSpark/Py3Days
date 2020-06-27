import requests
from http import cookiejar
# from pyquery import PyQuery as pq

session = requests.Session()
session.cookies = cookiejar.LWPCookieJar(filename='./cookies.txt')
url = 'https://www.zhihu.com/explore'
headers = {
'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'
}
session.cookies.load(ignore_discard=True)
r = session.get(url, allow_redirects=False, headers=headers)
# print(r.status_code)
# print(r.text)
# doc = pq(r.text)
# items = doc('.explore-tab .feed-item').items()
# for item in items:
#     question = item.find('h2').text()
#     author = item.find('.author-link-line').text()
#     answer = pq(item.find('.content').html()).text()
# with open('explore.txt', 'w', encoding='utf-8') as file:
#     file.write('\n'.join([question, author, answer]))
#     file.write('\n' + '=' * 50 + '\n')
with open('zhihu.html', 'w', encoding='utf-8') as file:
    file.write(r.text)