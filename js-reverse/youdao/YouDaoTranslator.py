#!/usr/bin/python3.7
"""
    :author: yinSpark
    :createTime: 2019-6-5
    :description: 网易有道翻译器(综合比较国内翻译神器)
    :plan: 1. 有道翻译网页链接
           2. 有道词典和翻译手机链接(本篇采用)
           3. 有道智云API(有体验版，也可以注册版)
"""

import requests
from lxml import etree
from dataclasses import dataclass
from requests.exceptions import RequestException
from json.decoder import JSONDecodeError


@dataclass()
class YouDaoTranslator:
    inputtext: str

    def __post_init__(self):
        # 有道词典手机链接
        self.url_dict = 'https://m.youdao.com/dict'
        # 有道翻译手机链接
        self.url_translate = 'https://m.youdao.com/translate'
        # 有道智云文本翻译API
        self.url_ai = 'https://aidemo.youdao.com/trans'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-2009437564@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=1119649328.2919729; YOUDAO_MOBILE_ACCESS_TYPE=0; UM_distinctid=16b26b55325fc-0e113fb233d409-2e064a75-1fa400-16b26b55326161; _ntes_nnid=19468afab6ed72f8aed97a634c5d42f8,1559723080189; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcsFnWUarNJpbtWS5MSw; _yd_banner_day=5; _yd_btn_fanyi_5=true; _yd_newbanner_day=5; ___rl__test__cookies=1559727836642'
        }
        self.type = 'AUTO'
        self.dict_default = 'eng'
        self.from_ = 'Auto'
        self.to = 'Auto'

    def translate_data(self):
        data = {
            'inputtext': self.inputtext,
            'type': self.type
        }
        return data

    def dict_params(self):
        params = {
            'le': self.dict_default,
            'q': self.inputtext
        }
        return params

    def ai_data(self):
        data = {
            'q': self.inputtext,
            'from': self.from_,
            'to': self.to
        }
        return data

    def translate_content(self, data):
        try:
            response = requests.post(self.url_translate, headers=self.headers, data=data)
            if response.status_code in [200, 201]:
                html = etree.HTML(response.text)
                result = html.xpath('//ul[@id="translateResult"]/li/text()')
                return result[0]
            return None
        except RequestException:
            return None

    def dict_content(self, params):
        try:
            response = requests.post(self.url_dict, headers=self.headers, params=params)
            if response.status_code in [200, 201]:
                # print(response.text)
                html = etree.HTML(response.text)
                # 汉译英可用
                result = html.xpath('//div[contains(@class, "trans-container")]/ul/a/text()')
                # 英译汉可用
                # result = html.xpath('//div[contains(@class, "trans-container")]/ul/li/text()')
                return ';\n'.join(result)
            return None
        except RequestException:
            return None

    def ai_content(self, ai_data):
        try:
            response = requests.post(self.url_ai, headers=self.headers, data=ai_data)
            if response.status_code in [200, 201]:
                content = response.json()["translation"][0]
                # print(content)
                return content
            return None
        except JSONDecodeError:
            return None
        except RequestException:
            return None

    def run(self):
        # params = self.dict_params()
        # dict_result = self.dict_content(params)
        # print('词典搜索结果: \n{}'.format(dict_result))
        data = self.translate_data()
        translate_result = self.translate_content(data)
        print('直接翻译结果: {}'.format(translate_result))
        ai_data = self.ai_data()
        ai_result = self.ai_content(ai_data)
        print('ai翻译结果: {}'.format(ai_result))


if __name__ == '__main__':
    inputtext = input("请输入要翻译的内容(默认auto): ")

    translator = YouDaoTranslator(inputtext)
    translator.run()
