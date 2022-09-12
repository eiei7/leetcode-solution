"""
Method: hashmap
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        maxf = 0
        hashmap = {}
        for r in range(len(s)):#O(n)
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            maxf = max(maxf, hashmap[s[r]])#O(1)
            
            while (r - l + 1) - maxf > k:#invalid, so we need to remove the most left character off the current sliding window and hashmap, L move forward one step
                hashmap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

#TC: O(n)
#SC: O(1) #O(26)