# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergetwo(l1, l2):
            if not l1 and not l2:
                return None
            if not l1 and l2:
                return l2
            elif l1 and not l2:
                return l1
            res = ListNode()
            p = res
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            p.next = l1 if l1 else l2
            return res.next
            
        res = lists
        while len(res) > 1:
            tmp = []
            for i in range(0, len(res), 2):
                tmp.append(mergetwo(res[i], res[i + 1] if i + 1 < len(res) else None))
            res = tmp
        return res[0] if lists else None