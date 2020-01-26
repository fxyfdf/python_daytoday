# coding=utf-8
#-*-coding:utf-8-*-
aa = 1 if 1> 2 else 33
print (aa)

def maker (N):
    def action(X):
        return X ** N
    return action

f = maker(2)
f3 = f(3)
print (f3)

#   yield   return
def gensquare(N):
    for i in range(N):
        yield i **2
for i in gensquare(3):
    print (i)

x =gensquare(3)
next(x)
next(x)

a = 1000
try:
    if a > 100:
        b = 1111
        print(b)
except:
    print ("ddddddddd")
finally:
    print("aaaaa汉族")


