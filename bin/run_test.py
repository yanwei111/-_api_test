import time
from BeautifulReport import BeautifulReport
import unittest
import os
from lib.send_mail import Send_Mail

path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
#print(path)
test_dir = os.path.join(path,'test_case')

discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')
send = Send_Mail()


if __name__ == "__main__":
    report_dir = 'D:\\pycharm\\project\\直连天下后台管理系统\\report\\'
    print(report_dir)
    title = "接口自动化测试报告"
    now = time.strftime('%Y-%m-%d %H.%M.%S',time.localtime(time.time()))
    runner = BeautifulReport(discover)
    runner.report(
        title,
        filename='%s_接口测试报告'%now,
        report_dir=report_dir
    )
    send.send_mail()
