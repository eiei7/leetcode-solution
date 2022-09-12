# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        p = head
        count = 0
        while p:
            p = p.next
            count += 1
        
        p= head
        i = 0
        pre = head
        while p:
            if i == (count - n):
                if i == 0:
                    p = p.next
                    return p
                else:
                    pre.next = p.next
                    return head
            pre = p
            p = p.next
            i += 1

#TC: O(n)
#SC: O(1)