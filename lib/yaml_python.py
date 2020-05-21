# from ruamel.yaml import YAML
# import os
# path = os.path.join(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]),"data"),"login.yaml")
# print(path)
#
# # 第一步: 创建YAML对象
# yaml = YAML(typ='safe')
#
#
# # 第二步: 读取yaml格式的文件
# with open(path, encoding='utf-8') as file:
#     data = yaml.load(file)  # 为列表类型
#
# # print(f"data:\n{data}")
# print(data)
import yaml

fp = open("D:\pycharm\project\直连天下后台管理系统\data\login.yaml",encoding='utf-8')
testdata = yaml.load(fp,Loader=yaml.FullLoader)
print(testdata)