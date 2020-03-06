import sys

sys.path.append('../')

from leetcode.Ltools.LinkList import *

a=sigLink([1,2,3,4])
a.printlink()

a.insertNode(2,10)#插入操作
print("\n")
a.printlink()#遍历操作
print("\n")
a.getlength()#获取长度
print("\n")
a.linkAppend(15)#追加节点
a.printlink()

print (a.head)
print (a.head.next)
print (a.head.next)
print (a.head.next)
print (a.head.next)






