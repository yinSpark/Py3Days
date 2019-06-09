import requests
from lxml import etree
import json


# 获取拼多多搜索首页
# 现已失效，必须拿到anti_content参数

headers = {
    'Host': 'wxapp.yangkeduo.com',
    'Cookie': 'api_uid=rBQh2Fz4VlYO0gFyBdqTAg==; _nano_fp=XpdjX09ynpdqXqTbX9_C65aufMelHSkyILtYCLhz; pdd_user_uin=EH3OEAKU7EI72KAJPOVMFW23KE_GEXDA; msec=1800000; goods_detail=goods_detail_k6ZswG; goods_detail_mall=goods_detail_mall_Ld5SV2; rec_list_personal=rec_list_personal_KEFX8M; JSESSIONID=A24406907D6B2D48E69548E85801CE56; rec_list_index=rec_list_index_NIZrBN; PDDAccessToken=; ua=Mozilla%2F5.0%20(X11%3B%20Linux%20x86_64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Ubuntu%20Chromium%2F74.0.3729.169%20Chrome%2F74.0.3729.169%20Safari%2F537.36; webp=1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'
}

url = 'https://wxapp.yangkeduo.com/search_result.html?search_key=%E8%80%B3%E6%9C%BA&search_src=history&search_met=history_sort&search_met_track=history&refer_page_name=search&refer_page_id=10031_1560069350474_3jjVJs6SAH&refer_page_sn=10031'

r = requests.get(url, headers=headers)

# print(r.text)
doc = etree.HTML(r.text)
items = doc.xpath('//script[@id="__NEXT_DATA__"]/text()')[0]
print(items)
# json_str = json.loads(items, encoding='utf-8').get('props').get('pageProps').get('data').get('ssrResult').get('ssrListData').get('list')
# print(len(json_str))
# for item in json_str:
#     goodsName = item.get('goodsName')
#     print(goodsName)