
'''
用户身份验证
'''
'''
username = input('请输入用户名:')
password = input('请输入密码:')
# admin/admin
if username == 'admin' and password == 'admin':
    print('身份验证成功')
else:
    print("身份验证失败")
'''

'''
分段函数
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
'''
'''
x = float(input("x = "))
if x > 1:
    y = 3 * x -5
elif x > -1 and x < 1 :
    y = x + 2
else:
    y = 5 * x + 3
print ("f(%0.2f) = %0.2f" % (x,y) )
'''
'''
方法二
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
'''
'''
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x <=1 and x >=-1:
        y = x + 2
    else:
        if x < -1:
            y = 5 * x + 3
        else:
            y = 1000
print ("f(%0.2f) = %0.2f" % (x,y) )
'''

'''
练习1：英制单位英寸与公制单位厘米互换。
'''
'''
values = float(input("输入长度：")）
unit = input("输入单位")
if unit ==in or unit == "英寸" :
    print("%0.2f 英寸 = %0.2f 厘米" % (values,))
'''

'''
练习2：百分制成绩转换为等级制成绩。
要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
'''
'''
sore = float(input("输出成绩:"))
if sore > 100:
    grad = "ERROR"
elif sore >= 90:
    grad = "A"
elif sore >= 80:
    grad = 'B'
elif sore >= 70:
    grad = 'C'
elif sore >= 60:
    grad = 'd'
else:
    grad  = 'D'
print("对应的成绩等级:", grad)
'''
'''
练习3：输入三条边长，如果能构成三角形就计算周长和面积。
'''
print("一次输入三条边长")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
# 1 构成三角形的必要条件，两边之和大于第三边
if a + b > c and a + c > b and b + c > a :
    print ("可以构成三角形")
    #周长
    print('周长： %f' % (a + b + c))
    # 海伦公式求面积
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) **0.5
    print('面积： %f' % (area))
else:
    print("输入值不能构成三角形")












