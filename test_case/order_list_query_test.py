import unittest
import requests
from toolclass.login_success import LoginSuccess
import json
from readConfig import ReadConfig

test_http_url = ReadConfig().get_url("test_http_url")
dev_http_url = ReadConfig().get_url("dev_http_url")

class OrderListQueryTest(unittest.TestCase):
    '''查询订单列表'''
    def setUp(self):
        self.base_url = test_http_url + "admin/order"
        self.headlist = LoginSuccess().loginsuccess()

    def test_order_list_query(self):
        headers = {
            "authKey":self.headlist[0],
            "sessionId":self.headlist[1]
        }
        payload = {"status": 1}
        r = requests.get(self.base_url,headers=headers,params=payload)
        #print(r.text)
        self.result = json.loads(r.text)
        print(self.result)
        self.assertEqual(self.result["code"],200)

if __name__ == "__main__":
    OrderListQueryTest().test_order_list_query()