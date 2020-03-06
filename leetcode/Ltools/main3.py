class Node():
    # 定义一个链表，初始时需要赋予值
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.length = 0  # 对链表操作，添加一个 统计长度的值
        self.head = None
    #判断链表是否为空
    def is_empty(self):
        return self.length == 0
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
            p.next = this_node  # 直接吧 p.next 赋值给新添加的object,
        self.length += 1

if __name__ == "__main__":
    # n = Node(None)
    # print(n.next,n.data)
    l = LinkedList()
    list=[1,2,3,4]
    l.append(list)
    print(l.head.data)
    print(l.head.next)
    for i in list:
        l.append(i)
        #print(n)
    n = l.head
    while n:
        #print(n.next)
        print(n.data)
        n = n.next