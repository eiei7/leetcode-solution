# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        count = 0
        while q:
            len_q = len(q)
            tmp = []
            for i in range(len_q):
                node = q.popleft()
                if node:
                    if count % 2 == 0:
                        tmp = tmp + [node.val]
                    else:
                        tmp = [node.val] + tmp
                    q.append(node.left)
                    q.append(node.right)
            count += 1
            if tmp:
                res.append(tmp)
        return res

#TC:O(n)
#SP:O(2^n)