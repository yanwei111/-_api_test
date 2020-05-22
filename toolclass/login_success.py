"""工具类，用于被调用"""
import  os,sys
from conf.readConfig import ReadConfig
from lib.runmain import *
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

test_http_url = ReadConfig().get_url("test_http_url")
dev_http_url = ReadConfig().get_url("dev_http_url")

class LoginSuccess():
    def __init__(self):
        self.base_url = test_http_url + "admin/base/login"

    def loginsuccess(self):
        url = self.base_url + 'admin/base/login'
        payload = {'username': 'lsxd', 'password': '123456', 'isRember': 0}
        r = requests.post(self.base_url,data=payload)
        self.result =r.json()
        print(r.text)
        authkey = self.result['data']['authKey']
        sessionid = self.result['data']['sessionId']
        headlist = [authkey, sessionid]
        return headlist


if __name__=="__main__":
    LoginSuccess().loginsuccess()
