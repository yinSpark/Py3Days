import requests

# 测试拼多多小程序链接
# anti_content参数不断变化
# 若登录，还需要AccessToken， VerifyAuthToken参数

# 拼多多可用链接
# https://wxapp.yangkeduo.com/
# http://mobile.yangkeduo.com/
# http://yangkeduo.com/

session = requests.Session()

headers = {
    'cookie': 'api_uid=rBQh2Fz4VlYO0gFyBdqTAg==; _nano_fp=XpdjX09ynpdqXqTbX9_C65aufMelHSkyILtYCLhz; pdd_user_uin=EH3OEAKU7EI72KAJPOVMFW23KE_GEXDA; msec=1800000; goods_detail=goods_detail_k6ZswG; goods_detail_mall=goods_detail_mall_Ld5SV2; rec_list_personal=rec_list_personal_KEFX8M; rec_list_index=rec_list_index_BJL928; PDDAccessToken=; ua=Mozilla%2F5.0%20(Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F74.0.3729.169%20Mobile%20Safari%2F537.36; webp=1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'
}

url_index = 'https://wxapp.yangkeduo.com/search_result.html?search_key=%E8%80%B3%E6%9C%BA&search_src=history&search_met=history_sort&search_met_track=history&refer_page_name=search&refer_page_id=10031_1560072189829_X1Y1VtorUS&refer_page_sn=10031'

tt = session.get(url_index)
# print(tt.text)

anti_content = '0anAfxn5uNcYq9dVyy7LPeMT0P_TeHYUIVf6PAK-OK1E-5OGcCE8v7UaXbZJhxKJjVn7J9Ga6OxoqHTkw81fpWMf88MibYq9C09Aq4Bb-UEQ9sREf6NqSyKjSilrLw5pzQ8I6SH2lN1l3yGKavXK8-HwuHKEiA-vfm6vPVikFywZLIz8GlcZ2dOIQMHRz6D3M_kxNDdcMN2Kp9htBbIDEbJD0wGZ8rsGptVJJENZIVZKeCiZruErZFj7TR6l44cBYJo5ACUZ5WJ9urQfL3c5izjAKE2A9yvQCE5X9D57i9OFlfnZXUgiabamdVf36rJ8QX4_ZXWMX9rC_X98Hs_PAgqBCFlXmbrUUJJSEFQCSxUzd4bP2ZrCOOYy9iaeYlmonYz0KNiTZniIl1NvPSbCAjZY3zHcOYs-FvmybP5EIH73sDHcVEsknbfae8vFyF9DrRTIB-di4k_Bj-mo9OO530p-icLyWPmtvUPNg-Uw7jBsI-c_iBghc8k75ZfDgoZOtSp1TwkHJaKAzZ0mNZ8KbcBWNiJdvryWGhe8ZzDts3TC67e_15IuusR7K16apGW08eMROhi48boOoH'

url = 'https://api.pinduoduo.com/search?gid=&source=search&search_met=history&requery=0&list_id=rDzC3bfSpT&sort=default&filter=&q=%E8%80%B3%E6%9C%BA&page=2&size=50&flip=20;4;0;0;ffaccb6c-f6ee-43f7-9b44-ce8654a4c2de&anti_content='+ anti_content +'&pdduid=0'

headers = {
    'AccessToken': '',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Origin': 'https://wxapp.yangkeduo.com',
    'Referer': 'https://wxapp.yangkeduo.com/search_result.html?search_key=%E8%80%B3%E6%9C%BA&search_src=history&search_met=history_sort&search_met_track=history&refer_page_name=search&refer_page_id=10031_1560069350474_3jjVJs6SAH&refer_page_sn=10031',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36',
    'VerifyAuthToken': 'gvBYCSf37cmUNYj5Sns_ig'
}

r = session.get(url, headers=headers)
print(r.text)