#读取配置文件config.ini
import configparser
import os
path = os.path.split(os.path.realpath(__file__))[0]#获取项目绝对路径
path1 = os.path.dirname(path)
config_path = os.path.join(path,'config.ini')#在项目路径下加上config.ini的路径
conf = configparser.ConfigParser()#实例化ConfigParaser类
conf.read(config_path,encoding='utf-8')

print(path)
class ReadConfig():
    def get_url(self,name):
        #value = conf['URL']['http_url']
        value = conf.get('URL',name)
        return value

    def get_mail(self,name):
        value = conf.get("EMAIL",name)
        return value

    def get_place_order(self,name):
        value = conf.get("PLACE_ORDER",name)
        return value

    def get_db(self,name):
        value = conf.get("DATABASE",name)
        return value

if __name__ == "__main__":
    ReadConfig().get_place_order("merchantId")

