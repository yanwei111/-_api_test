from lib.md5_hash import Md5_Hash
from conf.readConfig import ReadConfig
from toolclass import time_samp,random_number

timesamp = time_samp.time_samp()
random_number = random_number.random_number()


merchantId = ReadConfig().get_place_order("merchantId")
outTradeNo = ReadConfig().get_place_order("outTradeNo") + str(random_number)
productId = ReadConfig().get_place_order("productId")
rechargeAccount = ReadConfig().get_place_order("rechargeAccount")
accountType = ReadConfig().get_place_order("accountType")
timeStamp = timesamp
key = ReadConfig().get_place_order("key")

class Sign():
    def __init__(self):
        self.md5_hash = Md5_Hash().hash_md5
    def sign(self):
        data = {
            "accountType":accountType,
            "merchantId":merchantId,
            "outTradeNo":outTradeNo,
            "productId":productId,
            "rechargeAccount":rechargeAccount,
            "timeStamp":str(timesamp),
            "key":key
        }

        print(sorted(data.keys()))
        fenxiaoshang_accout = data["accountType"]
        fenxiaoshang_merchanId = data["merchantId"]
        fenxiaoshang_outTradeNo = data["outTradeNo"]
        fenxiaoshang_productId = data["productId"]
        fenxiaoshang_rechargeAccount = data["rechargeAccount"]
        fenxiaoshang_time = data["timeStamp"]
        param = '&'.join([k + '=' + v for k, v in data.items()])
        print(param)
        sign = self.md5_hash(param)
        lis =[fenxiaoshang_accout,fenxiaoshang_merchanId,fenxiaoshang_outTradeNo,fenxiaoshang_productId,fenxiaoshang_rechargeAccount,fenxiaoshang_time,sign]
        print(lis)
        return lis

if __name__ == "__main__":
    Sign().sign()






