# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #[1,2,3,4,5,6,7,8] [1,8,2,7,3,6,4,5] [1,2,3,4] [8,7,6,5] [7,6,5]
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #reverser the second linklist
        head2 = slow.next
        slow.next = None
        pre = None
        while head2:
            tmp = head2.next
            head2.next = pre
            pre = head2
            head2 = tmp
        head2 = pre
        #merge two linklists
        head1 = head
        while head2:#because head2 is shorter
            p1, p2 = head1.next, head2.next
            head1.next = head2
            head2.next = p1
            head1 = p1
            head2 = p2

#TC: O(n)
#SC: O(1)
