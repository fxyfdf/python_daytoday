


'''
来自Stack的POP
正如我们所知道的，我们只能从堆栈中移除太多的数据元素，我们实现了一个可以实现这一点的python程序。
以下程序中的remove函数返回最上面的元素。我们首先通过计算堆栈的大小来检查顶层元素，然后使用内置的pop（）方法找出最顶层的元素。
'''

class Stack:
    '''用列表的方式实现栈'''
    def __init__(self):
        self.stack = []

    def add(self, dataval):
    # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

if __name__ == '__main__' :
    AStack = Stack()
    AStack.add('A')
    AStack.add("B")
    print(AStack.remove())
    print(AStack.remove())
    AStack.add("C")
    AStack.add("D")
    print(AStack.remove())