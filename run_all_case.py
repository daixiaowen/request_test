# coding:utf-8

import unittest
import os
import HTMLTestRunner


# 用例路径
case_path = os.path.join(os.getcwd(), 'test_weather')

# 测试报告路径
report_path = os.path.join(os.getcwd(), 'report.html')

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py', top_level_dir=None)
    return discover

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())

    f = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                           title='天气预报测试报告',
                                           description='用例执行情况')
    runner.run(all_case())
    f.close()



















