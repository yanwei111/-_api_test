import requests

class RunMain():
    def send_post(self,url,data,headers):
        response = requests.post(url=url,data=data,headers=headers)
        return response

    def send_get(self,url,params,headers):
        response = requests.get(url=url,params=params,headers=headers)
        return response

    def run_main(self, url, params, data, headers, method):
        response = None
        if method =='GET':
            response = self.send_get(url,params,headers)
            print(response.text)
        else:
            response = self.send_post(url,data,headers)
            print(response.text)
        return response

if __name__ == "__main__":
    url = "http://test.openapi.1688sup.cn/admin/base/login"
    payload = {'username': 'lsxd', 'password': '123456', 'isRember': 0}
    method = "post"
    headers = {
        "Content - Type": "application / json"
    }
    RunMain().run_main(url=url,data=payload,params=payload,method=method,headers=headers)