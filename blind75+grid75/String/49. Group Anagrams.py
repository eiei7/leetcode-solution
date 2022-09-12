import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        
        for s in strs:#O(m)
            count = [0] * 26
            for c in s:#O(m * n)
                count[ord(c) - ord('a')] += 1 #a->0,b->1
            hashmap[tuple(count)].append(s)#
        return hashmap.values()
#using tuple because it's immutable. list is mutable and unhashable

#TC: O(m * n)
#SC: O(26 * m) = O(m)

"""
What in the hashmap:

defaultdict(<class 'list'>, {(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'], 
(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['tan', 'nat'], 
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat']})
"""
