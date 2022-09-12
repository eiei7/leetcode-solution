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
        # 小心这段，node是nei的邻居，nei也是node的邻居
        hashmap = {i: set() for i in range(n)}
        for node, nei in edges:
            hashmap[node].add(nei)
            hashmap[nei].add(node)
        
        visited = set()

        def dfs(node, pre):
            if node in visted:#有loop存在，不是树
                return False
            visited.add(node)
            for nei in hashmap[node]:
                if nei == pre:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        #default pre = -1 ; 存在非连通分量，不是树<-> n > len(visited)
        return dfs(0, -1) and n == len(visited)