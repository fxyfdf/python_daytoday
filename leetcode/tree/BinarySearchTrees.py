
'''
二叉搜索树（BST）是一棵树，其中所有节点都遵循下述
属性- 节点的左子树具有小于或等于其父节点密钥的密钥。
节点的右子树具有大于其父节点密钥的密钥。
因此，BST将其所有子树分成两部分; 左边的子树和右边的子树，可以定义为 -
left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)

在B-tree中搜索一个值

在树中搜索值涉及比较输入值与退出节点的值。
在这里，我们也从左到右遍历节点，最后是父节点。
如果搜索到的值与任何exitign值都不匹配，则返回未找到的消息，否则返回找到的消息。

'''

class SearchTreeNode:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = SearchTreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = SearchTreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

if __name__ == '__main__' :
    root = SearchTreeNode(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    print(root.findval(7))
    print(root.findval(14))