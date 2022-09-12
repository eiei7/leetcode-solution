"""
Method: dfs
"""

from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        hashmap = {c: set() for word in words for c in word}
        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[: min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    hashmap[w1[j]].add(w2[j])
                    break
                    
        visited = {}
        res = []
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nbs in hashmap[c]:
                if dfs(nbs):
                    return True
            visited[c] = False
            res.append(c)
            return False
        
        for c in sorted(hashmap.keys(), reverse=True):
            if dfs(c):
                return ""
        
        res.reverse()
        return ''.join(res)

#Time Complexity: O((n-1) * m) + O(logn)
#Space Complexity: O(n * m) near