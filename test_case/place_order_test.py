import unittest
import requests
from toolclass.time_samp import time_samp
from toolclass.random_number import random_number


class PlaceOrderTest(unittest.TestCase):
    """下游下单"""
    def setUp(self):
        self.http_url = "http://api.dev.1688sup.cn/recharge/order"
        self.time_samp = time_samp()
        print(self.time_samp)
        self.random_number = random_number()
        print(self.random_number)

    def tearDown(self):
        print(self.result)

    def test_place_order(self):
        """下单成功"""
        payload = {"merchantId":23505,"outTradeNo":self.random_number,"productId":"104","rechargeAccount":"18000000005","accountType":0,"timeStamp":self.time_samp,"sign":"F3B9CEC8C3D575E94B9CD879C5DD99B8"}
        headers = {
            "Content-Type":"application/x-www-form-urlencoded"
        }
        r=requests.post(self.http_url,headers=headers,data=payload)
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result["code"],'2000')
        self.assertEqual(self.result["message"],"ok")

    def test_order_repetition(self):
        """订单重复"""

if __name__ == "__main__":
    PlaceOrderTest().test_place_order()
