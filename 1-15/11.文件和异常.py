import time
from math import sqrt
import  json,requests
# 文件和异常

def FileOpen():
    f = open('file_test.txt','r',encoding='utf-8')
    print(f.read())
    f.close()

def TryFinally():
    f = None
    try:
        f = open('file_test.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件')
    except  LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    finally:
        if f:
            f.close()

def WithOpen():

    try:
        # 一次性读取整个文件内容
        with open('file_test.txt', 'r', encoding='utf-8') as f:
            print(f.read())

        # 通过for-in循环逐行读取
        with open('file_test.txt', mode='r') as f:
            for line in f:
                print(line,end=' ')
                time.sleep(0.5)
        print("test---for----in")

        # 读取文件按行读取到列表中
        with open('file_test.txt') as f:
            lines = f.readlines()
        print(lines)

    except FileNotFoundError:
        print('无法打开指定的文件')
    except  LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    finally:
        if f:
            f.close()

def IsPrime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def WitePrime(n=10000):
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename  in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, n):
            if IsPrime(number):
                if number < 100 :
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
            else:
                pass
    except IOError as ex:
        print(ex)
        print("写文件时发生错误！")
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成')

def CopyImage():
    try:
        with open('mm.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data)) # <class 'bytes'>
        with open('1.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开')
    except IOError as e:
        print('读写文件时出现错误')
    print('程序执行结束')

def SaveJson():
    mydict = {
        'name': 'NB',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='gbk') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成')

def OpenJson():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if  __name__ == '__main__':


    # FileOpen()
    # TryFinally()
    # WithOpen()
    # WitePrime()
    #CopyImage()
    #SaveJson()
    OpenJson()