"""
Method: hashmap
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s): return False
        count1 = {}
        count2 = {}
        for c in s:
            count1[c] = 1 + count1.get(c, 0)
        for c in t:
            count2[c] = 1 + count2.get(c, 0)
        for c in s:
            if c not in t or count1[c] != count2[c]:
                return False
        return True

"""
Method: Counter()
"""
from collection import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

"""
Method: sort
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

#TC:O(n^2) or O(nlogn)
#SC:O(1)