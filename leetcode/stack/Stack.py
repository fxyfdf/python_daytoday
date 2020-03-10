

class Stack(object):
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return self.stack == []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.isEmpty():
            # 如果列表是空，抛出异常
            raise IndexError('pop from empty stack')
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)



if __name__ =='__main__':
    s = Stack()
    list = [1,3,6,3,2,1]
    for i in list:
        s.push(i)
    print(s)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
