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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root 

#TC: O(n)
#SC: O(1)


"""
Method1: bfs
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.left and node.right:
                q.append(node.left)
                q.append(node.right)
            elif not node.left and node.right:
                q.append(node.right)
            elif node.left and not node.right:
                q.append(node.left)
            node.left, node.right = node.right, node.left
        return root

#TC: O(n)
#SC: O(1)
