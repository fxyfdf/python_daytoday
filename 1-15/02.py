
"""
2 小试牛刀
input()
int()
print()

Version: 0.1
Autor: fxyfdf
"""

'''
练习1：华氏温度转换为摄氏温度。
提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \di

f = float(input("请输入华氏温度:"))
c = (f - 32) / 1.8
print('%.1f 华氏度 = %.1f 摄氏度' % (f, c))
'''

'''
练习2：输入圆的半径计算计算周长和面积。

import math
radius = float(input('请输入圆半径:'))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print("圆面积: %.2f " % perimeter)
print("圆周长: %.2f" % area)
'''

'''
练习3：输入年份判断是不是闰年。
普通闰年:公历年份是4的倍数的，且不是100的倍数，为闰年。（如2004年就是闰年）；
世纪闰年:公历年份是整百数的，必须是400的倍数才是闰年（如1900年不是世纪闰年，2000年是世纪闰年）；
'''
year = input("输入年:")
is_leap = (year % 4 == 0 and year % 100 != 0) or \
           year % 400 == 0
print(is_leap)













