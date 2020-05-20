import unittest
import requests
import  os,sys
from readConfig import ReadConfig
import json
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

#读取配置文件
test_http_url = ReadConfig().get_url("test_http_url")
dev_http_url = ReadConfig().get_url("dev_http_url")


class AddLoginTest(unittest.TestCase):
    '''登录直连天下后台-test环境'''


    def setUp(self):
        self.base_url =test_http_url  + "admin/base/login"

    def tearDown(self):
        print(self.result)

    def test_add_login_para_all_null(self):
        '''所有参数为空'''
        payload = {'username':'','password':'','isRemember':''}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['code'],400)
        self.assertEqual(self.result['error'],'账号不能为空')

    def test_add_login_para_username_error(self):
        '''输入的账号不存在'''
        payload = {"username":"8888","password":"123456","isRemember":0}
        r = requests.post(self.base_url,data=payload)
        print(self.base_url)
        print(payload)
        self.result = r.json()
        self.assertEqual(self.result['code'],400)
        self.assertEqual(self.result['error'],'账号不存在')

    def test_add_login_para_password_error(self):
        '''输入的密码不正确'''
        payload = {'username':'lsxd','password':'09876'}

        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['code'],400)
        self.assertEqual(self.result['error'],'密码错误')

    def test_login_success(self):
        '''登录成功'''
        payload = {'username':'lsxd','password':'123456','isRember':0}
        r = requests.post(self.base_url,data=payload)
        print(self.base_url)
        self.result = r.json()
        self.assertEqual(self.result['code'],200)




if __name__ == '__main__':
    unittest.main()
