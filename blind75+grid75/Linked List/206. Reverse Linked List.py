"""
Method: interation
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        #when jump out of while loop, prev points to the last element = new head
        return prev

#TC: O(n)
#SC: O(1)

"""
Method: recursion
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newhead = head
        if head.next:
            newhead = self.reverseList(head.next)#subproblems of current head
            head.next.next = head#reverse
        head.next = None
        return newhead
#TC: O(n) 
#SC: O(n) 
