

class Node:


    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        '''只能打印单个节点数据'''
        print(self.data)

    def insert(self, data):


if __name__ == '__main__':
    n = Node
    n = n(10)
    n.PrintTree()