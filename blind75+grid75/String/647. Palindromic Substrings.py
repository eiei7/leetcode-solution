"""
Method: expand two pointers
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]: #O(n^2)
                res += 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: #O(n^2)
                res += 1
                l -= 1
                r += 1
        return res

#TC: O(n^2)
#SC: O(1)

"""
Method: brute force
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        for i in range(len(s)):
            for j in range(i + 1, len(s)): #O(n^2)
                substr = s[i : j + 1]
                if substr == substr[::-1]: #O(n^3)
                    res += 1
        return res

#TC: O(n^3) 
#SC: O(1)
