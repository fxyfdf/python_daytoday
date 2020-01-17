# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:23:15 2020

@author: LIPENGFEI2
"""


"""
定义类
"""

from time import sleep


class Student(object):
    
    # __init__ 是一个特殊的方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age 两个属性
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def study(self, curse_name):
        print(f'{self.name} 正在学习 {curse_name}')
        
    # PEP 8 要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分公司更倾向于使用驼峰命名法（驼峰标识）
    def watch_movie(self):
        if self.age < 18:
            print(f'{self.name} 你{self.age}太小了只能看熊大不能看熊二')
        else:
            print(f'{self.name} {self.age}  恭喜可以 看熊二')
       
class Clock(object):
  """数字时钟"""

  def __init__(self, hour=0, minute=0,second=0):
    """初始化方法

    :param hour: 时
    :param minute: 分
    :param second: 秒
    """
    self._hour = hour
    self._minute = minute
    self._second = second

  def run(self):
      """走字"""
      self._second += 1
      if self._second ==60:
          self._second = 0
          self._minute += 1
          if self._minute == 60:
              self._minute == 0
              self._hour += 1
              if self._hour == 24:
                  self._hour = 0

  def show(self):
    """显示时间"""
    return (f'{self._hour}:{self._minute}:{self._second}')


        
def main():
  clock = Clock(23, 59, 58)
  while True:
      print(clock.show())
      sleep(1)
      clock.run()       

'''
def main():

    # 创建学生对象并指定姓名和年龄
    stu1 = Student('lpf',17)
    # 给对象发 study 消息
    stu1.study('英语')
    # 给对象发 watch_av 消息
    stu1.watch_movie()
    
    stu2= Student('ll',21)
    stu2.study('搞事情')
    stu2.watch_movie()
'''
if __name__ == '__main__':
    main()
