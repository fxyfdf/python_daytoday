"""
python 并发编程的三种方式:
多进程，多线程，多进程+多线程
进程
线程

fork()   创建进程，调用fork()  函数的是父进程，创建出的是子进程，  子进程是父进程的拷贝，但是子进程拥有自己的PID


"""

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep
from threading import Thread, Lock


def download_task1(filename):
    print('开始下载%s.....' %filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d 秒' % (filename, time_to_download))

def main1():
    start = time()
    download_task1('Python.pdf')
    download_task1('Pig.avi')
    end = time()
    print('总共耗时 %.2f s' % (end - start))

def download_task2(filename):
    """多进程样例测试"""
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s.....' %filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d 秒' % (filename, time_to_download))

def main2():
    '''多进程测试方法'''
    start = time()
    p1 = Process(target=download_task2, args=('Python.pdf',))
    p1.start()
    p2 =Process(target=download_task2, args=('Pig.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗时 %.2f s' % (end - start))

counter = 0
def sub_task(string):
    global counter
    while counter < 10:
        print(string, end=' ', flush=True)
        counter += 1
        sleep(0.01)

def main3():
    Process(target=sub_task, args=('Ping', )).start()
    Process(target=sub_task, args=('Pong',)).start()

def download(filename):
    """多线程测试"""
    print('开始下载%s....' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s 下载完成！ 耗费了%d s' % (filename, time_to_download))

def main4():
    """多线程测试
    多线程共享进程得内存空间
    """
    start = time()
    t1 = Thread(target=download, args=('Python.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('hh.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了 %.3f s' % (end - start))

class Account(object):

    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        # 计算存款后的余额
        new_balance = self._balance + money
        # 模拟受理存款业务需要0.01s的时间
        sleep(0.01)
        # 修改账户余额
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main5():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
        #t.join()
    print(threads)
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print(f'账户余额为: ￥ {account.balance}元')


"""
Python的多线程并不能发挥CPU的多核特性，比如执行几个死循环的线程测试
"""
class Account2(object):
    """添加锁"""
    def __init__(self):
        self._balance = 0
        self._lock = Lock()


    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:

            # 计算存款后的余额
            new_balance = self._balance + money
            # 模拟受理存款业务需要0.01s的时间
            sleep(0.01)
            # 修改账户余额
            self._balance = new_balance
        finally:
            #  finally  中执行释放锁的操作保证正常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance

class AddMoneyThread2(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main6():
    account = Account2()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread2(account, 1)
        threads.append(t)
        t.start()
        #t.join()
    print(threads)
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print(f'账户余额为: ￥ {account.balance}元')

if __name__ =='__main__':
    # main1()
    # main2()
    # main3()
    # main4()
    # main5()
    main6()