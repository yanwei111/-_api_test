import yaml
import os

# fp = open("D:\pycharm\project\直连天下后台管理系统\data\login.yaml",encoding='utf-8')
# testdata = yaml.load(fp,Loader=yaml.FullLoader)
# print(testdata)
YAML_PATH = os.path.join(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]),"data"),"login.yaml")
print(YAML_PATH)

class ReadYamlList():
    def read_yaml_list(self):
        """
        读取yaml，返回列表形式
        :param case_row:
        :return:
        """
        with open(YAML_PATH,encoding='utf8') as yaml_file:
            yaml_txt = yaml_file.read()
            yaml_dict = yaml.load(yaml_txt,Loader=yaml.FullLoader)
            return yaml_dict


if __name__ == "__main__":
    ReadYamlList().read_yaml_list()
