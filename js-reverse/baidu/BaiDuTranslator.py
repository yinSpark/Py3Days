#!/usr/bin/python3.7
"""
    :author: yinSpark
    :createTime: 2019-6-5
    :description: 百度翻译器
    :plan: 1. 百度翻译网页链接(参数多)
           2. 百度翻译手机链接(参数少，本篇采用)
           3. 百度翻译开放平台API(需注册，有免费限制)
"""

import requests
import js2py
from dataclasses import dataclass
from requests.exceptions import RequestException
from json.decoder import JSONDecodeError


# 使用模块级数据类
@dataclass()
class BaiDuTranslator:
    query: str
    from_: str
    to: str

    def __post_init__(self):
        # 为了减少参数,使用百度翻译手机端链接,Chromium手机模式调试分析
        self.url = 'https://fanyi.baidu.com/basetrans'
        self.headers = {
            'referer': 'https://fanyi.baidu.com/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36',
            'cookie': 'BAIDUID=9EF57B3B7D5E7D5A5396972B8D8AEB12:FG=1; PSTM=1559296800; BIDUPSID=1DF2D56F86264BE1FBAE08C7A54B31F9; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1442_21085_29064_28518_29099_28837_28585_26350_29133; delPer=0; PSINO=5; locale=zh; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1559301358; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1559301358; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1559301302,1559301320,1559301358; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1559301358; yjs_js_security_passport=1da56b0c6b412ad902a9dcaad52008962010dc3a_1559301364_js'
        }
        # 使用js2py模块执行js函数
        self.context = js2py.EvalJs()
        if not self.from_:
            self.from_ = 'auto'
        if not self.to:
            self.to = 'auto'

    # js逆向破解sign参数
    def generate_sign(self):
        with open('crack_sign.js', 'r', encoding='utf-8') as f:
            self.context.execute(f.read())
            sign = self.context.a(self.query)
        return sign

    def generate_data(self, sign):
        data = {
            'query': self.query,
            'from': self.from_,
            'to': self.to,
            'token': '47680e7eb72909b5fb1a2c4ceff2fbda',
            # 'sign': '54706.276099',
            'sign': sign
        }
        return data

    def get_content(self, data):
        try:
            response = requests.post(self.url, headers=self.headers, data=data)
            if response.status_code in [200, 201]:
                content = response.json()["trans"][0]["dst"]
                return content
            return None
        except JSONDecodeError:
            return None
        except RequestException:
            return None

    def run(self):
        sign = self.generate_sign()
        data = self.generate_data(sign)
        content = self.get_content(data)
        print('翻译结果: {}'.format(content))


if __name__ == '__main__':
    query = input("请输入要翻译的内容(默认auto): ")
    from_ = input("请输入翻译前语言(如en/zh, 默认auto): ")
    to = input("请输入翻译后语言(如en/zh, 默认auto): ")

    translator = BaiDuTranslator(query, from_, to)
    translator.run()
