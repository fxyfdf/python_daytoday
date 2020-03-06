# -*- coding:utf-8 -*-
'''
用Python实现链表。
'''
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.length = 0
        self.head = None
    #判断链表是否为空
    def is_empty(self):
        return self.length == 0
    #插入节点this_node
    def append(self, this_node):
        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(this_node)
        if self.is_empty():
            self.head = this_node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = this_node
        self.length+=1
    #在第index处插入节点this_node
    def insert(self, this_node, index):
        if index > self.length:
            return 'Error'
        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(this_node)
        if index == 0:
            this_node.next = self.head
            self.head = this_node
        else:
            p = self.head
            while index-1:
                p = p.next
                index-=1
            this_node.next = p.next
            p.next = this_node
        self.length+=1
    #删除第index个节点
    def delete(self, index):
        if not 0<= index < self.length:
            return 'Error'
        if index == 0:
            self.head = self.head.next
        else:
            p = self.head
            while index-1:
                p = p.next
                index-=1
            p.next = p.next.next
        self.length-=1
    #更新第index节点的值
    def update(self, data, index):
        if not 0<= index < self.length:
            return 'Error'
        if index == 0:
            self.head.data = data
        else:
            p = self.head
            while index:
                p = p.next
                index-=1
            p.data = data
    #获取第index节点的值
    def get_data(self, index):
        if not 0<= index < self.length:
            return 'Error'
        if index == 0:
            return self.head.data
        else:
            p = self.head
            while index:
                p = p.next
                index-=1
            return p.data
    #获取链表长度
    def get_length(self):
        return self.length
    #清空链表
    def clear(self):
        self.head = None
        self.length = 0
    #打印链表
    def PrintList(self):
        if self.length ==0:
            return None
        else:
            p = self.head
            while p.next:
                print(p.data,'-->',end = '')
                p = p.next
            print(p.data)

if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    s = LinkedList()
    s.append(a)
    s.append(b)
    s.append(c)
    s.PrintList()
    s.insert(e,2)
    print(s.head.data)
    print(s.head.next.data)
    print(s.head.next.next.data)
    s.insert(d,0)
    print(s.head.data)
    print(s.head.next.data)
    print(s.head.next.next.data)
    s.delete(0)
    print(s.head.data)
    print(s.head.next.data)
    print(s.head.next.next.data)
    s.delete(2)
    print(s.head.data)
    print(s.head.next.data)
    print(s.head.next.next.data)
    s.update(0,1)
    print(s.head.data)
    print(s.head.next.data)
    print(s.get_data(0))
    print(s.get_data(1))
    print(s.get_length())
    s.PrintList()

# https://blog.csdn.net/qq_34364995/article/details/80787090
# ps:链表需要用一个变量来存储头节点，通过使用变量.next属性，来遍历后续结点。
# 一般头节点是不存储数值的，只存储第一个结点的位置。