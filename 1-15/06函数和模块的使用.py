
from random import randint
import  math

def foll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return  total

'''
def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c
'''

'''
# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
'''

def factorial(num):
    """求阶乘"""
    result = 1
    for n in range(1,num + 1):
        result *= n
    return result


"""
练习1：实现计算求两个数的最大公约数和最小公倍数的函数。
"""
def gcd(x1,x2):
    '''计算最大公约数
    公约数，亦称“公因数”。它是一个能被若干个整数同时均整除的 整数。
    如果一个整数同时是几个整数的 约数，称这个整数为它们的“公约数”；
    公约数中最大的称为最大公约数。
    1 循环最小数，找出公约数
    2 求出公约数中的最大数
    3 优化， 公倍数最大时的可能时 最小数的本身，如果不是，最大的就是 最小数的二次方根减1
    '''

    # x1 存最大数 x2 存最小数
    (x1, x2) = (x1, x2) if x1 > x2  else (x2, x1)
    for factor in range(x1, 0, -1):
        if x1 % factor == 0 and x2 % factor == 0:
            pass
            #return factor
            #print (factor)
    if x1 // x2 == 0: factor2 = x2
    else:
        for factor2 in range(int(math.sqrt(x1))+1, 0, -1):
            if x1 % factor2 == 0 and x2 % factor2 == 0:
                print (factor2)
                return factor2

def lcm(x,y):
    """最小公倍数"""
    # 两数乘积，除以公倍数
    lcm = x * y // gcd(x,y)
    return lcm

def is_palindrome(num):
    """判断一个数是不是回文，正着和倒着一样"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp = temp // 10
    # if total == num:
    #     return (num)
    # else:
    #     return (0)
    #  返回True  或 False
    return total == num

"""判断一个数是否数素数"""
def is_prie(num):
    for factor in range(2,num):
        if num % factor == 0 :
            return  False
    return True if num != 1 else  False


if __name__ == '__main__':
    #print(factorial(2))
    #print(gcd(4,8))
    #print(lcm(4,8))
    #print (is_palindrome(12321))
    print(is_prie(1))
