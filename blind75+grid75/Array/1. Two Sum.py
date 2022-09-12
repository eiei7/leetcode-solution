"""
Method1: hashmap
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i

#TC:O(n)
#SC:O(n)


"""
Method2: brute force
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

#TC:O(n^2)
#SC:O(1)
