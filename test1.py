# _*_coding: utf-8 _*_

def countdown(n):
    print("start")
    while n > 0:
        yield n
        n -= 1
    print ("DONE")

c = countdown(2)
print(next(c))
print(next(c))
print(next(c))
