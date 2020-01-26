from time import time
from threading import Thread

import requests
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime
from base64 import b64decode, b64encode
from json import dumps


# 继承Thread类创建自定义的线程类
class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1: ]
        print(filename)
        resp = requests.get(self.url)
        with open('test/' + filename, 'wb') as f:
            f.write(resp.content)

def main():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的网络API
    # 要使用该数据接口需要在天行数据的网站上注册
    # 然后用自己的Key替换掉下面代码的中APIKey即可
    for i in  [20]:
        url = f'http://api.tianapi.com/meinv/?key=96146d2403f7548131383dcbda02eb5f&num={i}'
        url1 = 'http://api.tianapi.com/txapi/verse/index/?key=96146d2403f7548131383dcbda02eb5f'
        print(url)
        resp = requests.get(url)
        # 将服务器返回的JSON格式的数据解析为字典
        data_model = resp.json()
        print(data_model)
        for mm_dict in data_model['newslist']:
            url = mm_dict['picUrl']
            # 通过多线程的方式实现图片下载
            DownloadHanlder(url).start()

def main2():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的网络API
    # 要使用该数据接口需要在天行数据的网站上注册
    # 然后用自己的Key替换掉下面代码的中APIKey即可
    for i in  [20]:
        #url = f'http://api.tianapi.com/meinv/?key=96146d2403f7548131383dcbda02eb5f&num={i}'
        #url = 'http://api.tianapi.com/txapi/verse/index?key=96146d2403f7548131383dcbda02eb5f&num=1'
        url = 'http://api.tianapi.com/txapi/verse/index'
        #print(url)
        resp = requests.get(url)
        #print(resp)
        # 将服务器返回的JSON格式的数据解析为字典
        data_model = resp.json()
        print(data_model)
        for mm_dict in data_model['newslist']:
            content = mm_dict['content']
            # 通过多线程的方式实现图片下载
            print(content)
            #DownloadHanlder(url).start()

def main3():
    """套接字测试"""
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定IP地址和端口(端口用于区分不同的服务)
    # 同一时间在同一个端口上只能绑定一个服务否则报错
    server.bind(('0.0.0.0', 6789))
    # 3.开启监听 - 监听客户端连接到服务器
    # 参数512可以理解为连接队列的大小
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器.')
        print(client)
        # 5.发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6.断开连接
        client.close()

def main4():
    """多线程，多用户"""

    # 自定义类
    class FileTransferHander(Thread):

        def __init__(self, cclient, data, filename):
            super().__init__()
            self.cclient = cclient
            self.data =data
            self.filename = filename

        def run(self):
            my_dict = {}
            my_dict['filename'] = self.filename
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = self.data
            # 通过dumps函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送JSON 字符串
            # ('127.0.0.1', 58143)
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1 创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 2 绑定IP地址和端口（区分不同的服务）
    server.bind(('127.0.0.1', 5566))
    # 3 开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听')
    with open('test/92_5538.jpg', 'rb') as f :
        # 将二进制数据 编码处理成base64 再解码成utf-8字符串
        data = b64encode(f.read()).decode('utf-8')
        filename = '92_5538.jpg'
        print(data)
    while True:
        client, addr = server.accept()
        print(client)
        print(addr,"客户端接入")
        # 启动一个线程来处理客户端的请求
        FileTransferHander(client, data, filename).start()



if __name__ == '__main__':
    # main()
    # main2()
    # main3()
    main4()














