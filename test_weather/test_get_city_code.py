# coding:utf-8


import requests
import json
import unittest


class GetCityCode(unittest.TestCase):
    def setUp(self):
        print('开始测试')


    def tearDown(self):
        print('测试结束')


    def test_1get_city_code(self):
        self.url = 'http://cdn.sojson.com/_city.json'
        self.r = requests.get(self.url)
        t = self.r.text
        js = json.loads(t)
        print(js)
        # print(js[0]['city_code'], type(js[0]['city_code']))
        # return js[0]['city_code']
        # 返回城市列表
        return js

    # def test_get_weather(self):
    #     self.url1 = 'http://t.weather.sojson.com/api/weather/city/'
    #     # 循环前40个城市列表
    #     for self.params in self.test_1get_city_code()[0: 40]:
    #         # 获取城市列表
    #         self.data = self.params['city_code']
    #         if self.data != '':
    #         # self.data = self.test_1get_city_code()
    #             r = requests.get(self.url1+self.data)
    #             print('----->{}天气预报'.format(self.params['city_name']), r.text)


if __name__ == '__main__':
    unittest.main()

















