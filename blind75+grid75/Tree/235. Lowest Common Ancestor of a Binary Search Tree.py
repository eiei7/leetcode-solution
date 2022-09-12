"""
Method1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur_node = root
        while cur_node:
            if p.val < cur_node.val and q.val < cur_node.val:
                cur_node = cur_node.left
            elif p.val > cur_node.val and q.val > cur_node.val:
                cur_node = cur_node.right
            else:
                return cur_node

TC:O(logn) #binary search time cost
SC:O(1)


"""
Method1-version2
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val - p.val) * (root.val - q.val) <= 0:#current node == ancestor if product == 0；
        #current node == the lowest common ancestor if two ndoes located in subleft tree and subright tree sepratively
            return root
        return self.lowestCommonAncestor(root.left if p.val < root.val else root.right, p, q)
