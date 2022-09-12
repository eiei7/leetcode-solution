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
            newhead = self.reverseList(head.next)#当前head的子问题
            head.next.next = head#倒序指向
        head.next = None#最后一次结束后，最后一个元素指向null
        return newhead
#TC: O(n) 
#SC: O(n) 
