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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isvalid(root, lower_b, upper_b):
            if not root:
                return True
            if not(root.val > lower_b and root.val < upper_b):
                return False
            return isvalid(root.left, lower_b, root.val) and isvalid(root.right, root.val, upper_b)
        
        return isvalid(root, float('-inf'), float('inf'))

#TC:O(n) #2*n
#SC:O(1)
