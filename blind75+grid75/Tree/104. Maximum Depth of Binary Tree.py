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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#TC: O(n) # n:number of nodes
#sc: O(n)


"""
Method1: bfs
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque()
        q.append(root)
        res = 0
        while q:
            res += 1
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

#TC: O(n)
#SC: O(n)

"""
Method1: dfs
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if not node:
                return depth
            depth += 1
            left = dfs(node.left, depth)
            right = dfs(node.right, depth)
            self.res = max(self.res, left, right)
            return depth
        
        self.res = 0
        dfs(root, 0)
        return self.res

#TC: O(n)
#SC: O(n)

