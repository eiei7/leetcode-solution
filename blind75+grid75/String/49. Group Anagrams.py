import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        
        for s in strs:#O(m)
            count = [0] * 26#定长的list，将某个字符串中字符出现的次数映射到对应的下标中
            for c in s:#O(m * n)
                count[ord(c) - ord('a')] += 1 #a->0,b->1以此类推
            hashmap[tuple(count)].append(s)#将count pattern一样的str加入到hashmap中
        return hashmap.values()#只返回hashmap中的值
#using tuple 因为不可变，而list可变，且list unhashable

#TC: O(m * n)
#SC: O(26 * m) = O(m)

"""
What in the hashmap:

defaultdict(<class 'list'>, {(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'], 
(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['tan', 'nat'], 
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat']})
"""