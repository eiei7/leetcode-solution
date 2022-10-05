class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for c in s:
            hashmap[c] = 1 + hashmap.get(c, 0)
        
        res = ""
        for key, val in sorted(hashmap.items(), key = lambda x: x[1], reverse = True):
            res += key * val
        return res

#TC:O(n)
#SP:O(n)