import unittest
import requests
import os
import ddt
path = os.path.join(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]),"data"),"login.yaml")

@ddt.ddt
class Login(unittest.TestCase):

    @ddt.file_data(path)
    def test_login(self,**case):
        url = case.get('url')
        method = case.get('method')
        data = case.get('data')
        print(url,method,data)

        try:
            if method.lower() =='post':
                res = requests.post(url,data = data)
                resp = res.text
                print(resp)
            else:
                res = requests.get(url,params = data)
                resp =res.text
                print(resp)
        except Exception as e:
            print("接口出错了！！！")
            resp = e
        result = resp.json()

        check = case.get('check')
        for c in check:
            self.assertIn(c,result)

if __name__ == "__main__":
    Login().test_login()


