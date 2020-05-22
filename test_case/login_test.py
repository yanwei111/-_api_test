import requests
from lib.yaml_list import ReadYamlList
from lib.runmain import RunMain
import unittest
from conf.readConfig import ReadConfig
import ddt
import os
from lib.utils import Utils

utils = Utils()
test_http_url = ReadConfig().get_url("test_http_url")
dev_http_url = ReadConfig().get_url("dev_http_url")
read_list = ReadYamlList()
request = RunMain()
YAML_PATH = os.path.join(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]),"data"),"login.yaml")
@ddt.ddt
class Login(unittest.TestCase):
    def setUp(self):
        print("********开始执行用例********")

    def tearDown(self):
        print("********用例执行完成********")

    @ddt.file_data(YAML_PATH)
    def test_login(self,**case):
        url = case.get('url')
        method = case.get('method')
        data = case.get('data')
        try:
            if method.lower() == 'post':
                r = requests.post(url,data=data)
                resp = r.text

            else:
                r = requests.get(url,params=data)
                resp = r.text

        except Exception as e:
            print("接口请求出错")
            resp =e

        result = utils.set_res_data(resp)
        print(result)
        check = case.get('check')
        print(check)

        for c in check:
            self.assertIn(c,result)

if __name__ == "__main__":
    Login().test_login()
