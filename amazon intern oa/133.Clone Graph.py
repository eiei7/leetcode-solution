"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        hashmap = {}
        
        def clone(root):
            if root in hashmap:
                return hashmap[root]
            hashmap[root] = Node(root.val)
            for nbs in root.neighbors:
                hashmap[root].neighbors.append(clone(nbs))
            return hashmap[root]
        clone(node)
        return hashmap[node]