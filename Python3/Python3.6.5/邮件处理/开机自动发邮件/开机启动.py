#!/usr/bin/env python3
#coding:utf-8
import smtplib
from email.header import Header
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
import time

mail_host = 'smtp.163.com'           #邮箱服务器名
mail_user = '18271676080@163.com'      #邮箱用户名
mail_pass = 'FBLATPX4869'            #登录密码（授权码）
sender = '18271676080@163.com'            #发送者
receivers = ['204206705@qq.com','846058904@qq.com']    #收件人

message = MIMEMultipart()
print(dir(message))
message['From'] = sender
message['To'] = '846058904@qq.com'
subject = u'开机 Python SMTP'
message['Subject'] = Header(subject)

content = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
body = '本次打开电脑的时间是:'+ content

message.attach(MIMEText(body))
att1 = MIMEText(open(r'K:\vip\001.jpg','rb').read(),'base64','utf-8')
att1['Content-Type']='application/octet-stream'
att1['Content-Disposition']='attachment;filename="001.jpg"'
message.attach(att1)

# try:
print('Connecting...')
smtpobj = smtplib.SMTP_SSL(mail_host) #连接服务器
print("登录账户")
smtpobj.login(mail_user,mail_pass)    #登录账户
print("发送邮件")
print("""
    发送人:%s
    接收人:%s
    邮件内容:%s
    """%(sender,receivers,message.as_string()))
smtpobj.sendmail(sender,receivers,message.as_string())   #发送邮件
print("""
    发送人:%s
    接收人:%s
    邮件内容:%s
    """%(sender,receivers,message.as_string()))
smtpobj.quit()                        #退出登录
print('邮件发送成功')
# except smtplib.SMTPException :
#     print('Error:无法发送邮件')

