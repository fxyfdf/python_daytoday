#-*- coding:utf-8 -*-

# https://blog.csdn.net/qq_45353823/article/details/96641873
class linkNode():
    """
    链表节点类
    """
    def __init__(self,date):
        self.date=date
        self.next=None

class sigLink():
    """
    self.length   用于记录链表的长度
    self.head     链表的头部
    self.tail     记录链表的尾部
    """

    def __init__(self, item):
        """
        item   一位数组，存放改链表的数组
        （1）__ init__(self,item)是自动调用的，只要有sigLink这一实例化对象就会执行的，
        （2）item这一参数可以在实例化时传入一个列表。
        （3）i+=1记住一定不能忘记写！（笔者一开始就忘记写出现了没有预期的结果）
        """
        self.length = len(item)
        if self.length <= 0:
            return
        i = 0
        self.head = linkNode(item[i])
        self.tail = self.head
        i += 1  ###此句不能少
        while i < self.length:
            self.tail.next = linkNode(item[i])
            self.tail = self.tail.next
            i += 1

    def printlink(self):
        """
            正序打印该链表
        """
        if self.head == None:
            print("该链表为空链表！")
        p = self.head
        while p != None:
            print(p.date, end=" ")
            p = p.next

    def getlength(self):
        """
            获取链表的长度
        """
        print("该链表的长度为：", self.length)

    def linkAppend(self, num):
        """在链表尾部追加节点"""
        # 先将要插入的数字转换为节点（linkNode（num）），然后将tail的next域指向linkNode（num），最后在将tail指向linkNode（num）即完成了追加这一功能
        self.tail.next = linkNode(num)
        self.tail = self.tail.next
        self.length += 1

    def insertNode(self,index,num):
        """
            在链表中间插入节点
            index：插入节点的序号
            num：插入点的值
        """
        if index>self.length:
            print("index参数超出范围")
            return
        if index==self.length:
            self.linkAppend(num)
            return
        if index==0:
            p=linkNode(num)
            p.next=self.head
            self.head=p
            self.length+=1
            return
        ptemp=self.head
        while index>1:
            ptemp=ptemp.next
            index-=1
        p=linkNode(num)
        p.next=ptemp.next
        ptemp.next=p
        self.length+=1



class ListNode():
    """
    链表节点类
    """
    def __init__(self,x):
        self.date=x
        self.next=None


class singLinkNode():
    """
    self.length   用于记录链表的长度
    self.head     链表的头部
    self.tail     记录链表的尾部
    """

    def __init__(self, item):
        """
        item   一位数组，存放改链表的数组
        （1）__ init__(self,item)是自动调用的，只要有sigLink这一实例化对象就会执行的，
        （2）item这一参数可以在实例化时传入一个列表。
        （3）i+=1记住一定不能忘记写！（笔者一开始就忘记写出现了没有预期的结果）
        """
        self.length = len(item)
        if self.length <= 0:
            return
        i = 0
        self.head = linkNode(item[i])
        self.tail = self.head
        i += 1  ###此句不能少
        while i < self.length:
            self.tail.next = linkNode(item[i])
            self.tail = self.tail.next
            i += 1

    def printlink(self):
        """
            正序打印该链表
        """
        if self.head == None:
            print("该链表为空链表！")
        p = self.head
        while p != None:
            print(p.date, end=" ")
            p = p.next

    def getlength(self):
        """
            获取链表的长度
        """
        print("该链表的长度为：", self.length)

    def linkAppend(self, num):
        """在链表尾部追加节点"""
        # 先将要插入的数字转换为节点（linkNode（num）），然后将tail的next域指向linkNode（num），最后在将tail指向linkNode（num）即完成了追加这一功能
        self.tail.next = linkNode(num)
        self.tail = self.tail.next
        self.length += 1

    def insertNode(self,index,num):
        """
            在链表中间插入节点
            index：插入节点的序号
            num：插入点的值
        """
        if index>self.length:
            print("index参数超出范围")
            return
        if index==self.length:
            self.linkAppend(num)
            return
        if index==0:
            p=linkNode(num)
            p.next=self.head
            self.head=p
            self.length+=1
            return
        ptemp=self.head
        while index>1:
            ptemp=ptemp.next
            index-=1
        p=linkNode(num)
        p.next=ptemp.next
        ptemp.next=p
        self.length+=1


#链接：https: // leetcode - cn.com / problems / add - two - numbers / solution / python3ti - jie - fang - leetcodeguan - fang - lei - listnoded /

class ListNode1():
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"


