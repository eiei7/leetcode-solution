"""
Method: binary search 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []: return None
        
        def mergetwolists(list1, list2):
            res = ListNode()
            p = res
            while list1 and list2:
                if list1.val < list2.val:
                    p.next = list1
                    list1 = list1.next
                else:
                    p.next = list2
                    list2 = list2.next
                p = p.next
            if list1:
                p.next = list1
            if list2:
                p.next = list2
            return res.next
        
        l1 = lists[0]
        for i in range(1, len(lists)):
            l1 = mergetwolists(l1, lists[i])
        return l1

#TC:O(k * n)
#SC:O(1)
