# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergetwoLists(l1, l2):
            res = ListNode()
            p = res
            while l1 and l2:
                if l1.val <= l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            if l1:
                p.next = l1
            if l2:
                p.next = l2
            return res.next
        
        if not lists:
            return None
        
        while len(lists) > 1:
            tmp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                tmp.append(mergetwoLists(l1, l2))
            lists = tmp
        return lists[0]

#TC: O(n*logk)
#SC: O(k/2 + 1) -> O(1)