
'''
在堆栈中，顺序排列的最后一个元素将首先出现，因为我们只能从堆栈顶部移除。
这种功能称为后进先出（LIFO）功能。添加和删​​除元素的操作称为 PUSH 和 POP 。
在下面的程序中，我们将它实现为add和remove函数。
我们声明一个空列表并使用append（）和pop（）方法添加和删除数据元素。

'''
class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
    # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # Use peek to look at the top of the stack
    def peek(self):
        return self.stack[0]


if __name__ == '__main__' :
    #  只打印栈顶
    AStack = Stack()
    AStack.add("A")
    AStack.add("B")
    AStack.peek()
    print(AStack.peek())
    AStack.add("C")
    AStack.add("D")
    print(AStack.peek())
    print(AStack.peek())