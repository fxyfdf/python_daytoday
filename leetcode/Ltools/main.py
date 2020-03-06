
from leetcode.Ltools.LinkList2 import ListNode
from leetcode.Ltools.LinkList2 import ListNode_handle

if __name__ == "__main__":
    ll = ListNode()  # 定义一个链表
    print(ll)
    #且需要吧1,8,3按1 -->8 -->3的顺序放入链表中,需要进行的操作则
    ListNode_1 = ListNode_handle()
    # ll = ListNode()
    l1_list = [1, 8, 3]
    for i in l1_list:
        ll = ListNode_1.add(i)

    ll = ListNode_1._reverse(ll)

    while ll:
        print(ll.val)
        ll = ll.next
