
"""
@property装饰器
使用@property包装器来包装getter和setter方法
想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作
"""
from math import sqrt
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter 方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter 方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋。' % self._name)
        else:
            print(f'{self._name}正在玩斗地主')

def main():
    person = Person('王大拿',66)
    person.play()
    person.age = 2
    person.play()

"""
__slots__魔法： 变量的限定只对当前类的对象生效，对子类并不起任何作用
python 是动态语言，通常动态语言允许在程序允许时给对象绑定新的属性或方法，当然也可以对已绑定的属性和方法进行解绑。
"""

class Person1(object):
    # 限定Person对象只能绑定_name,_age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 18:
            print(f'{self._name}正在玩飞行棋')
        else:
            print(f'{self._name}在斗地主')
def main1():
    person = Person1('王大拿',22)
    person.play()
    person._gender = 'man'

"""
静态方法和类方法
"""

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


def main3():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用得
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入消息得对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形')

"""
类方法，和静态方法类似
类方法得第一个参数约定名为 cls , 代表得是当前类相关的信息的
"""
from time import time, localtime, sleep

class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour =0

    def show(self):
        """显示时间"""
        return (f'{self._hour}:{self._minute}:{self._second}')

def main4():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

"""
类之间的关系： is-a   has-a  use-a 
is-a  继承或泛化
has-a 关联
use-a 依赖
"""

"""
继承和多态
"""


"""
Pet 类处理成一个抽象类，所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。Python从语法层面并没有像
通过 abc 模块的ABCMeta元类 和 abstractmethod 包装器来达到抽象类的效果，如果一个类中存在抽象方法那么这类就不能够实例化
"""
from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)

class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()





"""案例3 工资结算系统"""
"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成

"""
from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        """
        初始化方法

        :param name: 姓名
        """
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """
        获得月薪

        :return: 月薪
        """
        pass



#if __name__ == '__main__':
    #main()
    #main3()
    #main4()