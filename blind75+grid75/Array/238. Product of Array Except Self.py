"""
Method1: prefix & suffix
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) 
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix #res should be product
            postfix *= nums[i]
        return res

#Time Complexity: O(n)
#Space Complexity: O(n)