"""
Method: hashset
"""
import collections as co
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in hashset:#从左开始去重
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            res = max(res, r - l + 1)#len(hashset)=r - l + 1
        return res

#TC: O(n)
#SC: O(n)