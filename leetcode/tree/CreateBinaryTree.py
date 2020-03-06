# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
树表示由边连接的节点。它是一个非线性数据结构。它具有以下属性。

    一个节点被标记为根节点。
    除根之外的每个节点都与一个父节点相关联。
    每个节点可以有一个数字的节点号。

我们使用前面讨论的概念os节点在python中创建一个树数据结构。
我们将一个节点指定为根节点，然后将更多节点添加为子节点。下面是创建根节点的程序。
创建根

我们只需创建一个Node类并添加一个值给节点。这变成只有根节点的树。
Travesring一棵树

树可以通过决定访问每个节点的序列来遍历。
我们可以清楚地看到，我们可以从一个节点开始，
然后访问左侧子树第一个和右侧子树。或者我们也可以先访问右边的子树，
然后访问左边的子树。因此，这些树遍历方法有不同的名称。

'''
class TreeNode:


    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # def PrintTree(self):
    #     '''只能打印单个节点数据'''
    #     print(self.data)

    def insert(self, data):
        def insert(self, data):
            # Compare the new value with the parent node
            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = TreeNode(data)
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = TreeNode(data)
                    else:
                        self.right.insert(data)
            else:
                self.data = data

        # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

if __name__ == '__main__':
    n = TreeNode
    n = n(10)
    n.PrintTree()