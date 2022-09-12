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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:#在递归中，若当前的preorder为空或当前的inorder为空，则没有结点需要再填充了，应返回None
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid + 1])#新数组的第二个元素做根
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

#TC:O(n)
#SC:O(1)

"""
Method1-version2
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder: return None
        self.i = 0
        
        def dfs(inorder):
            if not inorder:
                self.i -= 1
                return None
            node = TreeNode(preorder[self.i])
            idx = inorder.index(preorder[self.i])
            self.i += 1
            node.left = dfs(inorder[:idx])
            self.i += 1
            node.right = dfs(inorder[idx + 1:])
            return node
        
        return dfs(inorder)

#TC:O(n)
#SC:O(1)
