# Definition for singly-linked list.
class ListNode(object):
    """定义链表"""
    def __init__(self):
        self.val = None
        self.next = None


class ListNode_handle:
    """对链表进行操作"""
    def __init__(self):
        # self.cur_node = None
        self.head = None

    def add(self, data):
        #add a new node pointed to previous node
        node = ListNode()  # 添加指向前一个节点的新节点，
        node.val = data
        node.next = self.head  # 新阶段 next 指向 None
        self.head = node # 原来的头，指向 新的对象, 链表的两个部分，一部分本身值(data), 指针结构体，此处指像下一个object
        return node

    def print_ListNode(self, node):
        while node:
            print ('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
            node = node.next

    def _reverse(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        result = ListNode()
        result_handle = ListNode_handle()
        for i in list:
            result = result_handle.add(i)
        return result

"""
其中对链表进行操作部分,大致是包括添加新的node, 反向排列链表, 打印链表.
添加链表节点时候操作如下:
假设有要完成链表操作为: ListNode_1
"""

# if __name__ == "__main__":
#     l1 = ListNode()  # 定义一个链表
#     print(l1)
#     #且需要吧1,8,3按1 -->8 -->3的顺序放入链表中,需要进行的操作则
#     ListNode_1 = ListNode_handle()
#     l1 = ListNode()
#     l1_list = [1, 8, 3]
#     for i in l1_list:
#         l1 = ListNode_1.add(i)
#
#     l1 = ListNode_1._reverse(l1)
#
#     while l1:
#         print(l1.val)
#         l1 = l1.next






