"""
Method1: dfs
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            maxleft = max(dfs(root.left), 0)
            maxright = max(dfs(root.right), 0)
            self.res = max(self.res, root.val + maxleft + maxright)#update res while visiting a new node because of edge case [-2,-1,0] 
            return max(root.val + maxleft, root.val + maxright)#plus root.val inorder to link to it's parent to form a path
        
        self.res = root.val
        dfs(root)
        return self.res

#TC:O(n)
#SC:O(1)

"""
Method1-version2
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        
        def dfs(root):
            if not root:
                return 0
            max_l = dfs(root.left)
            max_r = dfs(root.right)
            self.res = max(self.res, root.val + max_l + max_r, root.val + max_l, root.val + max_r, root.val)
            return max(root.val, root.val + max_l, root.val + max_r, 0)
        
        dfs(root)
        return self.res

#TC:O(n)
#SC:O(1)

