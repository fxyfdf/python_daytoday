from socket import  socket
from json import loads
from base64 import b64decode
import yaml
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main3():
    # 1.创建套接字对象默认使用IPV4 和 TCP 协议
    client = socket()
    # 2.连接到服务器（需要知道IP地址和端口）
    client.connect(('127.0.0.1', 6789))
    # 3.从服务器接收数据
    print(client.recv(1024).decode('utf-8'))
    client.close()


def main4():
    client = socket()
    client.connect(('127.0.0.1', 5566))
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收1024 字节
    data = client.recv(1024)
    while data:
        # 将收到的数据拼接起来
        in_data += data
        data = client.recv(1024)
    # 将收到的二进制数据解码成JSON字符串并转换成字典
    # loads函数的作用 是将JSON字符串转换成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    print(my_dict)
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    print(filedata)
    with open(filename, 'wb') as f:
        # 将base64 格式的数据解码成二进制数据并写入
        f.write(b64decode(filedata))
    print('图片已经保存')

def main5():
    dit = {}
    str = 'sssss'
    dit['name']=str
    dit['id'] = '{{aaaa}}'


    print(dit)
    # print(dit['name'])
    # print(dit['id'])
    aa = yaml.dump(dit, default_style=None)
    print(aa)
    print(yaml.dump(dit,default_style=None))

def min6():
    """发送邮件测试"""
    sender = 'fxyfdf@sina.com'
    receivers = ['fxyfdf2@sina.com']
    message = MIMEText('PYTHON 邮件测试', 'plain', 'utf-8')
    message['From'] = Header('fxyfdf', 'utf-8')
    message['To'] = Header('邮件实验例子', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.sina.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, '132@Pengfei')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')



if __name__ == '__main__':
    # main3()
    # main4()
    # main5()
    min6()