import os
from conf import readConfig
import yagmail as yagmail

read_conf = readConfig.ReadConfig()#实例化类
#从配置文件中读取email各信息
mail_host = read_conf.get_mail("mail_host")
mail_user = read_conf.get_mail("mail_user")
mail_pass = read_conf.get_mail("mail_pass")
subject = read_conf.get_mail("subject")
sender = read_conf.get_mail("sender")
receiver = read_conf.get_mail("receiver")
receivers = receiver.split(",")#将receivers以逗号为间隔转换为列表，因为在yag.send中直接传入列表是不能发送邮件的


class Send_Mail():
    def send_mail(self):
        path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        report_dir = os.path.join(path, 'report')
        # print(report_dir)
        lists = os.listdir(report_dir)
        # print(lists)
        lists.sort()
        recent = lists[-2]
        # print(recent)

        file = os.path.join(report_dir, recent)
        # print(file)
        yag = yagmail.SMTP(mail_user, mail_pass, mail_host)
        content = """
         hi all：
            接口自动化已执行完毕
            邮件已发送
            请查收附件"""
        yag.send(receivers, '接口自动化测试报告', content, file)

if __name__ == "__main__":
    Send_Mail().send_mail()