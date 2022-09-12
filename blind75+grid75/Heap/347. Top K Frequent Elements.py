"""
Method: hashmap
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        res = list(sorted(hashmap, key = lambda x: hashmap[x], reverse=True))
        return res[:k]

#TC:O(n)
#SC:O(n)

"""
Method: bucket sort
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #[1,1,1,2,2,3]
        #[0,3,2,1]
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        count = [[] for i in range(len(nums) + 1)]
        for key, val in hashmap.items():
            count[val].append(key)
        res = []
        for i in range(len(count) - 1, -1, -1):
            if count[i] != []:
                res.extend(count[i])
            if len(res) == k:
                return 
                
#TC:O(n)
#SC:O(n)