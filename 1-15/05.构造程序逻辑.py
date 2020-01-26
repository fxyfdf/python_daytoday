
'''
寻找水仙花数
说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
'''
'''
for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if  num ==low ** 3 + mid ** 3 + high ** 3:
        print (num)
'''

'''
正整数的反转
'''
'''
number = int(input("输入一个正整数："))
reversed_num = 0
while number > 0:
    reversed_num = reversed_num * 10 +  number % 10
    number = number // 10
print (reversed_num)
'''

'''
百钱百鸡问题。

说明：百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
'''

'''
for gj in range (0,20):
    for mj in range(0,34):
        for xj in range(0,300):
            count = 5 * gj + 3 * mj + xj / 3
            if count == 100 and  gj + mj + xj == 100:
                print (gj,mj,xj)
            else:
                pass
'''

'''
CRAPS赌博游戏。

说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
'''
'''
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
'''
'''
from random import randint
# 1-6 随机生成两个数字
jetton = 1000
print ("欢迎进入Craps游戏")
#print (''游戏规则如下：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
#玩家第一次如果摇出2点、3点或12点，庄家胜；
#其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
#如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。 '')

first = randint(1,6) + randint(1,6)
# 加入筹码：
print("游戏开始")
#先无赌注，单纯得逻辑

is_true = 2
while is_true != 1:
    # pass

    debt = int(input("请输入本次加入筹码:"))
    print("第一次点数为：%d" % (first))
    if first == 11 or first == 7:
        jetton_new = jetton + debt
        print("玩家胜利")
    elif first == 2 or first == 3 or first == 12:
        print("庄家胜利")
        jetton_new = jetton - debt
    else:
        while True:
            first2 = randint(1, 6) + randint(1, 6)
            if first2 == 7:
                jetton_new = jetton - debt
                print ("庄家胜利")
                break;
            elif first == first2:
                jetton_new = jetton + debt
                print("玩家胜利")
                break;
            else:
                continue;
        print ("11111111111111111111111111111111111111111111")
    if debt == 8 : 
        print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
    else:
        pass 

    print ("剩余筹码:%d" % (jetton_new))
    is_true = int(input("不继续按非 1:"))
print ("欢迎下次光临，您剩余筹码:%d" % (jetton_new))
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
'''''

'''
生成斐波那契数列的前20个数。
说明：斐波那契数列（Fibonacci sequence），又称黄金分割数列，是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）
在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，所以这个数列也被戏称为"兔子数列"。
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，
每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
       {  1  x = 1
f(x) = |  1  x = 2
       {  f(x-1) + f(x-2) x > 2
'''

'''
# f(0) = 0
# f(1) =1
# f(2) = 1
# f(x) = f(x -1) + f(x - 2) (x > 1)
# f(2) = f(1) + f(0) = 1 + 0 = 1
# fib1 = 1
# fib2 = 2
# x = n 是 f(x) 等于多少
def fib_loop(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        print (a)
    return  a
fib_loop(20)

#for i in range(20):
#  print(fib_loop(i), end=' ')
'''

'''
找出10000以内的完美数。
说明：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。。
'''

# 找出10000 以内的完美数字.
# 完美数的定义，它的所有的真因子(除了它本身以外的因子)的和 （即因子函数） 恰好等于他本身
# 什么是因子： 假如整数n除以m，结果是无余数的整数，那么我们称m就是n的因子。
# 找出一个数的所有因子，即 从1 到 n 它本身 递归 被除 后 无余数

# 1 找出一个数的所有因子，以列表方式输出
# 2 对列表求和，如果和与给出的数字相等，说明是完美数字
'''
def PerfectNumber(x):
    yzlist=[]
    count, i, j = 0, 0, 0
    for i in range(1, x // 2 + 1):
        if x % i == 0: yzlist.append(i)
        else: pass
    #return  yzlist
    for j in yzlist:
        count = count + j
    if x == count: return (x,yzlist)
    #else: return 0
for i in range(1, 10000+1):
    #print (i)
    a = PerfectNumber(i)
    if a is not None:
        print (a)
'''

'''
输出100以内所有的素数。
说明：素数指的是只能被1和自身整除的正整数（不包括1）。
'''
def PrimeNumber (x):
    i = 1
    # 如果有一个数能被整除，is_true = 0
    is_true = 1
    while is_true:
        for i in range (2,x):
            if x % i == 0:
                is_true = 0
                break;
            else:
                is_true = 1
                continue;
        #print (is_true)
        if is_true : return x;
        else: return (0)
#print(PrimeNumber(7))
for i in range(1,100):
    if PrimeNumber(i):
        print(PrimeNumber(i))
    else:
        pass


