"""
Method1: bucket sort
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #{1: 3, 2: 2, 3: 1}
        #[0, 1, 2, 3, 4, 5, 6]
        #    3  2  1
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        fre = [[] for i in range(len(nums) + 1)]
        for num, val in hashmap.items():
            fre[val].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            for num in fre[i]:
                res.append(num)
                if len(res) == k:
                    return res

#TC:O(N)
#SP:O(n)

"""
Method2: hashmap
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        res = [key for key, val in sorted(hashmap.items(), key = lambda x: x[1], reverse = True)]
        return res[:k]
#TC:O(nlogn) the worst case
#SP:O(n)
