# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, pathNum):
            if not root.left and not root.right:
                self.res += pathNum
                return 
            if root.left:
                dfs(root.left, pathNum * 10 + root.left.val)
            if root.right:
                dfs(root.right, pathNum * 10 + root.right.val)
            return 
        
        self.res = 0
        dfs(root, root.val)
        return self.res