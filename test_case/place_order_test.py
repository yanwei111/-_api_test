import unittest
from toolclass.sign import Sign
from readConfig import ReadConfig
import requests

test_xiadan_url = ReadConfig().get_url("test_xiadan_url")

class PlaceOrderTest(unittest.TestCase):
    def setUp(self):
        self.http_url = test_xiadan_url + "recharge/order"
        self.sign = Sign().sign()

    def test_oder(self):
        accounType = self.sign[0]
        merchanId = self.sign[1]
        outTradeNo = self.sign[2]
        productId = self.sign[3]
        rechargeAccount = self.sign[4]
        time = self.sign[5]
        sign = self.sign[6].upper()
        # sign1 =sign.upper()
        print(accounType,merchanId,outTradeNo,productId,rechargeAccount,time,sign)
        payload = {"merchantId":merchanId,"outTradeNo":outTradeNo,"productId":productId,"rechargeAccount":rechargeAccount,"accountType":accounType,"timeStamp":time,"sign":sign}
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        r = requests.post(self.http_url,headers=headers,data=payload)
        print(r.text)
        self.result = r.json()
        self.assertEqual(self.result['code'],"2000")
        self.assertEqual(self.result["message"],"ok")

if __name__ =="__main__":
    PlaceOrderTest.test_oder()