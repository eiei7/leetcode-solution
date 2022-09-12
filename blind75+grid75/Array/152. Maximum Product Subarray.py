"""
Method1: DP
"""
from functools import reduce
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #max:2 6 -2 4     -2 0 0
        #min:2 3 -12 -48  -2 0 0
        maxpro = nums[0]
        minpro = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            tmp = maxpro
            maxpro = max(maxpro * nums[i], nums[i], minpro * nums[i])
            minpro = min(minpro * nums[i], nums[i], tmp * nums[i])
            res = max(res, maxpro)
        return res

#Time Complexity: O(n)
#Space Complexity: O(1)

"""
Method2: Brute force
"""
from functools import reduce
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #brute force
        #[2],[3],[-2],[4];[2,3],[3,-2],[-2,4];[2,3,-2],[3,-2,4],[2,3,-2,4]
        res = max(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res = max(reduce((lambda x, y: x * y), nums[i: j + 1]), res)
        return res

#Time Complexity: O(n^2)
#Space Complexity: O(1)
