"""
Method1: recursion
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sametree(tr1, tr2):
            if not tr1 and not tr2:
                return True
            if tr1 and tr2 and tr1.val == tr2.val:
                return sametree(tr1.left, tr2.left) and sametree(tr1.right, tr2.right)
            return False
        
        if not subRoot:
            return True
        if not root:#equals to if not root and subRoot, because if not subRoot will be executed at first
            return False
        if sametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

#TC:O(n) #n depends on the tree which has fewer nodes.
#SC:O(1)
