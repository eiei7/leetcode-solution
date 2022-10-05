class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        hashmap = {}
        for c in t:
            hashmap[c] = 1 + hashmap.get(c, 0)    
        total = len(hashmap)

        res = [0, float('inf')]
        l, r = 0, 0
        while r < len(s):
            if s[r] in hashmap:
                hashmap[s[r]] -= 1
                if hashmap[s[r]] == 0:
                    total -= 1

            if total == 0:
                while s[l] not in t or hashmap[s[l]] < 0:
                    if s[l] in t:
                        hashmap[s[l]] += 1
                    l += 1
                if hashmap[s[l]] == 0:
                    if r - l < res[1] - res[0]:
                        res = [l, r]
                    hashmap[s[l]] += 1
                    total += 1
                    l += 1
            r += 1
        return s[res[0]:res[1] + 1] if res[1] != float('inf') else ""