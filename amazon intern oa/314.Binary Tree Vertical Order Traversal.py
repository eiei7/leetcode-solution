from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def vertical_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        hashmap = collections.defaultdict(list)

        q = collections.deque()
        q.append([root, (0, 0)])

        while q:
            for i in range(len(q)):
                node, pos = q.popleft()
                r, c = pos
                hashmap[c].append(node.val)
                if node.left:
                    q.append([node.left, (r + 1, c - 1)])
                if node.right:
                    q.append([node.right, (r + 1, c + 1)])
        
        return [val for key, val in sorted(hashmap.items(), key = lambda x: x[0])] 

#TC:O(n)
#SP:O(n)