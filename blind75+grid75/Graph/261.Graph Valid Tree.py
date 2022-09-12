"""
Method: dfs
"""
from typing import (
    List,
)
import collections
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # node is neighbor of nei, nei is neighbor of node
        hashmap = {i: set() for i in range(n)}
        for node, nei in edges:
            hashmap[node].add(nei)
            hashmap[nei].add(node)
        
        visited = set()

        def dfs(node, pre):
            if node in visted:#existing a loop
                return False
            visited.add(node)
            for nei in hashmap[node]:
                if nei == pre:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        #default pre = -1 ; more than 1 connected components <-> not a tree <-> n > len(visited)
        return dfs(0, -1) and n == len(visited)
