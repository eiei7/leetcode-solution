# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1, l2 = ListNode(), ListNode()
        t1, t2 = l1, l2
        while head:
            if head.val < x:
                t1.next = head
                t1 = t1.next
            else:
                t2.next = head
                t2 = t2.next
            head = head.next
        t1.next = l2.next
        t2.next = None
        return l1.next

#TC:O(n)
#SP:O(1)