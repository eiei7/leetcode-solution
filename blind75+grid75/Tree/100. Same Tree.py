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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        return (p and q) and (p.val == q. val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # (p and q) -> when p or q == None, but we assume it's not None, so it'll be False

TC: O(n)
SC: O(n)

"""
Method1-version2
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q. val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

TC: O(n)
SC: O(n)

"""
Method2: bfs
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        que = deque()
        que.append([p, q])
        while que:
            node1, node2 = que.popleft()
            if not node1 and not node2:
                continue
            if (not node1 and node2) or (node1 and not node2) or (node1.val != node2.val):
                return False
            que.append([node1.left, node2.left])
            que.append([node1.right, node2.right])
        return True

TC: O(n)
SC: O(n)

"""
Method3: dfs
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que = deque()
        que.append([p, q])
        
        while que:
            node1, node2 = que.pop() #first in last out
            if not node1 and not node2:
                continue
            elif node1 and node2 and node1.val == node2.val:
                que.append([node1.left, node2.left])
                que.append([node1.right, node2.right])
            else:
                return False
        return True
#TC: O(n)
#SC: O(n)
