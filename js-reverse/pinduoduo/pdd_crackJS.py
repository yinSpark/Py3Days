import requests
import json
from lxml import etree
import execjs
import os

# 测试破解anti_content参数
# 1. 通过执行js
# 2. 通过执行nodejs

session = requests.Session()

headers = {
    'cookie': 'api_uid=rBQh2Fz4VlYO0gFyBdqTAg==; rec_list_index=rec_list_index_9LRusd; _nano_fp=XpdjX09ynpdqXqTbX9_C65aufMelHSkyILtYCLhz; pdd_user_id=3101932292178; pdd_user_uin=EH3OEAKU7EI72KAJPOVMFW23KE_GEXDA; PDDAccessToken=NIENBWIXK43GP23JLPFKDBTQQVT3IFH2YVXKFSWCN6EUUSJW6OWQ1005224; ua=Mozilla%2F5.0%20(Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F74.0.3729.169%20Mobile%20Safari%2F537.36; webp=1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'
}

url_index = 'https://wxapp.yangkeduo.com/search_result.html?search_key=%E8%80%B3%E6%9C%BA&search_src=new&search_met=rec_sort&search_met_track=suggestion&refer_page_name=login&refer_page_id=10169_1560055837039_To4g6twlcs&refer_page_sn=10169&page_id=10015_1560055874089_V7NZ9YNEnl&list_id=oRw1YV53IV&flip=60%3B3%3B0%3B40%3Ba78e3a3f-049b-48e8-a33c-9b8dada632c7&is_back=1'

r = session.get(url_index, headers=headers)

doc = etree.HTML(r.text)
items = doc.xpath('//script[@id="__NEXT_DATA__"]/text()')[0]
print(items)
json_str = json.loads(items, encoding='utf-8').get('props').get('pageProps').get('data').get('ssrResult').get('ssrListData')
print(json_str)
# for item in json_str:
#     goodsName = item.get('goodsName')
#     # print(goodsName)
#
# headers.update({
#     'AccessToken': 'NIENBWIXK43GP23JLPFKDBTQQVT3IFH2YVXKFSWCN6EUUSJW6OWQ1005224',
#     'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
#     'Origin': 'https://wxapp.yangkeduo.com',
#     # 'Referer': 'https://wxapp.yangkeduo.com/search_result.html?search_key=%E8%80%B3%E6%9C%BA&search_src=new&search_met=rec_sort&search_met_track=suggestion&refer_page_name=login&refer_page_id=10169_1560055837039_To4g6twlcs&refer_page_sn=10169&page_id=10015_1560055874089_V7NZ9YNEnl&list_id=oRw1YV53IV&flip=60%3B3%3B0%3B40%3Ba78e3a3f-049b-48e8-a33c-9b8dada632c7&is_back=1',
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36',
#     'VerifyAuthToken': 'z_urg2VKv9YN4D-tb6nfNg'
# })
#
# # with open('get_antiContent.js', 'r', encoding='utf-8') as f:
# #     js = execjs.compile(f.read())
# #     anti_content = js.call('get_anti', 'http://mobile.yangkeduo.com/search_result.html?search_key=%E6%83%85%E4%BE%A3%E8%A1%A3%E6%9C%8D')
# # print(anti_content)
#
# anti_content = os.popen(f"node merge.js").read().strip()
#
# url = 'https://api.pinduoduo.com/search?gid=&source=search&search_met=suggestion&requery=0&list_id=oRw1YV53IV&sort=default&filter=&q=%E8%80%B3%E6%9C%BA&page=4&size=50&flip=180;3;0;160;c1eb4d9f-3557-4ba3-9208-11ebf6dc371d&anti_content='+anti_content+'&pdduid=3101932292178&is_back=1'
#
# r = session.get(url, headers=headers)
# print(r.text)

