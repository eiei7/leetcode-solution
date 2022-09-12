"""
Method: sliding window
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        total = 0
        count = {}
        for c in t: #O(m)
            count[c] = 1 + count.get(c, 0)
            total += 1
        res = [0, float('inf')]
        l = 0
        for r in range(len(s)):#O(n)
            if s[r] in t:
                if count[s[r]] > 0:
                    total -= 1
                count[s[r]] -= 1
            if total == 0:
                while True:
                    if s[l] not in t:#O(m + n)
                        l += 1
                    elif s[l] in t and count[s[l]] < 0:
                        count[s[l]] += 1
                        l += 1
                    else:
                        break
                if r - l < res[1] - res[0]:
                    res = [l, r]
                count[s[l]] += 1
                if count[s[l]] > 0:
                    total += 1
                l += 1
        return s[res[0]: res[1] + 1] if res[1] != float('inf') else ""

#TC: O(m + n)
#SC: O(m + n)