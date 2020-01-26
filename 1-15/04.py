
'''
用for循环实现1~100求和
'''
'''
sum = 0
for x in range (1,101,1):
    sum = sum + x
print (sum)
'''
'''
用for循环实现1~100之间的偶数求和
'''
'''
sum = 0
for x in range(0,101,2):
    #print (x)
    sum = sum + x
print ("100以内偶数求和:",sum)
'''
'''
sum = 0
for x in range(0,100,1):
    if x % 2 ==0:
        sum = sum + x
    else:
        print ("奇数:",x)
print("偶数求和为:", sum)
'''

'''
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
'''
'''
import random
# 生成随机数
answer = random.randint(1,100)
if answer:
    answer = int(answer)
print(answer)
# 统计出猜的次数
counter = 0
while True:
    counter = counter + 1
    number =  input("输入猜测数字:")
    if  number.isdigit():
        number = int(number)
        if number > answer:
            print('猜测次数:%d,您猜测的:%d偏大' % (counter,number))
        elif number < answer:
            print('猜测次数:%d,您猜测的:%d偏小'% (counter, number))
        else:
            # number == answer
            print('猜测次数:%d,您猜测的: %d ,恭喜才对了' % (counter, number))
            # 跳出while 循环
            break;
    else:
        print ("输入有误")
        break;
'''
'''
输入一个正整数判断它是不是素数：
质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数
'''
'''
format math import sqrt
num = int(input('请输入一个正整数:'))
# 求平方根，取整数
end = int(sqrt(num))
is_prime = True
# 判断一个数不是批量查找
for x in range(2, end + 1):
    # 如果模 等于0 说明是非 质数
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
'''

'''
练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
最大公约数：最大被除的
最小公倍： 
'''
'''
x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x
# 从两个数中较的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
'''
'''
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()
'''








