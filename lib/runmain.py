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
        else:
            response = self.send_post(url,data,headers)
        return response

