# coding_utf-8


import requests
import unittest
from test_weather import test_get_city_code


class getWeather(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        print('开始测试')


    def tearDown(self):
        print('测试结束')



    def test_get_weather(self):
        self.url1 = 'http://t.weather.sojson.com/api/weather/city/'
        # 实例化GetCityCode类
        get_code = test_get_city_code.GetCityCode()
        # 循环前40个城市列表
        for self.params in get_code.test_1get_city_code()[0: 40]:
            # 获取城市列表
            self.data = self.params['city_code']
            if self.data != '':
                r = requests.get(self.url1+self.data)
                self.assertIn('time', r.text)
                print('----->{}天气预报'.format(self.params['city_name']), r.text)


if __name__ == '__main__':
    unittest.main()