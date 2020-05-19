import time,sys
#sys.path.append('./test_case')
from HTMLTestRunner import HTMLTestRunner
import unittest
from lib.send_mail import Send_Mail
import os

#指定测试用例为当前文件下的interface目录
path = os.path.split(os.path.realpath(__file__))[0]
#print(path)
test_dir = os.path.join(path,'test_case')
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')
send = Send_Mail()

#生成报告并发送邮件
if __name__ == '__main__':

    #now = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    #now = time.strftime("%Y-%m-%d #H:%M:%S", time.localtime(time.time()))  # 获取系统时间
    now = time.strftime('%Y-%m-%d %H.%M.%S',time.localtime(time.time()))
    filename = 'D:/pycharm/project/直连天下后台管理系统/report/' + now + '_result.html'
    print(filename)
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = '直连天下系统接口自动化测试报告',
                            description = 'Implementation Example with:颜蔚')
    runner.run(discover)
    fp.close()
    send.send_mail()

