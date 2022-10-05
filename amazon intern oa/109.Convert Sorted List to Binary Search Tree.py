# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if not head: 
            return None
        if not head.next:
            return TreeNode(head.val)
        
        s, f = head, head.next
        pre = s
        while f and f.next:
            pre = s
            s = s.next
            f = f.next.next
        p = s.next
        pre.next = None
        root = TreeNode(s.val)
        if s != head:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(p)
        return root