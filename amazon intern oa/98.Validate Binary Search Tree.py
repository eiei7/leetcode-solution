# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left_b, right_b = float('-inf'), float('inf')
        
        def isvalid(root, left_b, right_b):
            if not root:
                return True
            if root.val > left_b and root.val < right_b:
                return isvalid(root.left, left_b, root.val) and isvalid(root.right, root.val, right_b)
            else:
                return False
        return isvalid(root, left_b, right_b)
