
from leetcode.Ltools.LinkList2 import ListNode
from leetcode.Ltools.LinkList2 import ListNode_handle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     p, rev = head, None  # 创建一个空 链表 rev
    #     while p:
    #         rev, rev.next, p = p, rev, p.next
    #     return rev

    def reverseList(self, head: ListNode) -> ListNode:
        rev = None
        p = head
        # 循环链表
        while p:
            rev = p # 保留原有
            rev.next = rev
            p = p.next
        return rev

if __name__ == "__main__":
    l = ListNode()  # 实例化要给空链表
    ln = ListNode_handle() # 链表的操作
    list = [4,2,3]  # 测试数据
    # 向链表中写入数据
    for i in list:
        l = ln.add(i)
    #print(l)
    #ln.print_ListNode(l)
    while l:
        print(l.val)
        l = l.next
    rev = Solution()  # 先实例化 在引用
    rev1 = rev.reverseList(l)
