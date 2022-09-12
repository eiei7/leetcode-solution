"""
Method1: sum([0, .., len(nums])) - sum(nums) = missing value 
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) # the last element's value
        for i in range(len(nums)):
            res += (i - nums[i]) # equals to sum([0,..,len(nums)]) - sum(nums) = missing value
        return res

#Time Complexity: O(n)
#Space Complexity: O(1)

"""
Method2: x ^ x = 0, x ^ 0 = x
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= (i ^ nums[i])
        return res

#Time Complexity: O(n)
#Space Complexity: O(1)

"""
Method3: hashmap
"""
import collections as co
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashmap = co.defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        for i in range(len(nums) + 1):
            if i not in hashmap:
                return i
#TC:O(n * m)
#SC:O(n)

"""
Method4: brute force
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #brute force
        for i in range(len(nums) + 1):
            if i not in nums:
                return i

#TC:O(n * m) = O(n^2)
#SC:O(1)
