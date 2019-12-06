
#yield
#lambda

#-- 最普通的类
class C1( ):
    spam = 42                       # 数据属性
    def __init__(self, name):       # 函数属性:构造函数
        self.name = name
    def __del__(self):              # 函数属性:析构函数
        print("goodbey ", self.name)
I1 = C1('bob')

#-- Python的类没有基于参数的函数重载
class FirstClass(object):
    def test(self, string):
        print(string)
    def test(self):                 # 此时类中只有一个test函数 即后者test(self) 它覆盖掉前者带参数的test函数
        print("hello world")

#-- 子类扩展超类: 尽量调用超类的方法
class Manager(Person):
    def giveRaise(self, percent, bonus = .10):
        self.pay = int(self.pay*(1 + percent + bonus))     # 不好的方式 复制粘贴超类代码
        Person.giveRaise(self, percent + bonus)            # 好的方式 尽量调用超类方法

#-- 类内省工具
bob = Person('bob')
bob.__class__                       # <class 'Person'>
bob.__class__.__name__              # 'Person'
bob.__dict__                        # {'pay':0, 'name':'bob', 'job':'Manager'}

#-- 返回1中 数据属性spam是属于类 而不是对象
I1 = C1('bob'); I2 = C2('tom')      # 此时I1和I2的spam都为42 但是都是返回的C1的spam属性
C1.spam = 24                        # 此时I1和I2的spam都为24
I1.spam = 3                         # 此时I1新增自有属性spam 值为3 I2和C1的spam还都为24

#-- 类方法调用的两种方式
instance.method(arg...)
class.method(instance, arg...)

#-- 抽象超类的实现方法
# (1)某个函数中调用未定义的函数 子类中定义该函数
    def delegate(self):
        self.action()               # 本类中不定义action函数 所以使用delegate函数时就会出错
# (2)定义action函数 但是返回异常
    def action(self):
        raise NotImplementedError("action must be defined")
# (3)上述的两种方法还都可以定义实例对象 实际上可以利用@装饰器语法生成不能定义的抽象超类
    from abc import ABCMeta, abstractmethod
    class Super(metaclass = ABCMeta):
        @abstractmethod
        def action(self): pass
    x = Super()                     # 返回 TypeError: Can't instantiate abstract class Super with abstract methods action

#-- # OOP和继承: "is-a"的关系
class A(B):
    pass
a = A()
isinstance(a, B)                    # 返回True, A是B的子类 a也是B的一种
# OOP和组合: "has-a"的关系
pass
# OOP和委托: "包装"对象 在Python中委托通常是以"__getattr__"钩子方法实现的, 这个方法会拦截对不存在属性的读取
# 包装类(或者称为代理类)可以使用__getattr__把任意读取转发给被包装的对象
class wrapper(object):
    def __init__(self, object):
        self.wrapped = object
    def __getattr(self, attrname):
        print('Trace: ', attrname)
        return getattr(self.wrapped, attrname)
# 注:这里使用getattr(X, N)内置函数以变量名字符串N从包装对象X中取出属性 类似于X.__dict__[N]
x = wrapper([1, 2, 3])
x.append(4)                         # 返回 "Trace: append" [1, 2, 3, 4]
x = wrapper({'a':1, 'b':2})
list(x.keys())                      # 返回 "Trace: keys" ['a', 'b']

#-- 类的伪私有属性:使用__attr
class C1(object):
    def __init__(self, name):
        self.__name = name          # 此时类的__name属性为伪私有属性 原理 它会自动变成self._C1__name = name
    def __str__(self):
        return 'self.name = %s' % self.__name
I = C1('tom')
print(I)                            # 返回 self.name = tom
I.__name = 'jeey'                   # 这里无法访问 __name为伪私有属性
I._C1__name = 'jeey'                # 这里可以修改成功 self.name = jeey

#-- 类方法是对象:无绑定类方法对象 / 绑定实例方法对象
class Spam(object):
    def doit(self, message):
        print(message)
    def selfless(message)
        print(message)
obj = Spam()
x = obj.doit                        # 类的绑定方法对象 实例 + 函数
x('hello world')
x = Spam.doit                       # 类的无绑定方法对象 类名 + 函数
x(obj, 'hello world')
x = Spam.selfless                   # 类的无绑定方法函数 在3.0之前无效
x('hello world')

#-- 获取对象信息: 属性和方法
a = MyObject()
dir(a)                              # 使用dir函数
hasattr(a, 'x')                     # 测试是否有x属性或方法 即a.x是否已经存在
setattr(a, 'y', 19)                 # 设置属性或方法 等同于a.y = 19
getattr(a, 'z', 0)                  # 获取属性或方法 如果属性不存在 则返回默认值0
#这里有个小技巧，setattr可以设置一个不能访问到的属性，即只能用getattr获取
setattr(a, "can't touch", 100)      # 这里的属性名带有空格，不能直接访问
getattr(a, "can't touch", 0)        # 但是可以用getattr获取

#-- 为类动态绑定属性或方法: MethodType方法
# 一般创建了一个class的实例后, 可以给该实例绑定任何属性和方法, 这就是动态语言的灵活性
class Student(object):
    pass
s = Student()
s.name = 'Michael'                  # 动态给实例绑定一个属性
def set_age(self, age):             # 定义一个函数作为实例方法
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法 类的其他实例不受此影响
s.set_age(25)                       # 调用实例方法
Student.set_age = MethodType(set_age, Student)    # 为类绑定一个方法 类的所有实例都拥有该方法

'''