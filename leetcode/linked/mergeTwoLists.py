from leetcode.Ltools.LinkList2 import ListNode
from leetcode.Ltools.LinkList2 import ListNode_handle


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        prehead = ListNode()
        pre = prehead
        p1 = l1
        p2 = l2
        while p1:
            p1 = p1.next
            print("p11111111111111111111111111111")
            while p2:
                # pre.val = p2.val
                pre.next = p2
                p2 = p2.next
                print("p1222222222222222222222222")
            pre.next = p1

        return pre.next
if __name__ == "__main__":
    l1 = ListNode()  # 实例化要给空链表
    l2 = ListNode()  # 实例化要给空链表
    ln = ListNode_handle() # 链表的操作
    list = [4,2,3]  # 测试数据
    # 向链表中写入数据
    for i in list:
        l1 = ln.add(i)
        l2 = ln.add(i)
    #print(l)
    #ln.print_ListNode(l)
    rev = Solution()  # 先实例化 在引用
    rev1 = rev.mergeTwoLists(l1,l2)
    while rev1:
        print(rev1.val)
        rev1 = rev1.next