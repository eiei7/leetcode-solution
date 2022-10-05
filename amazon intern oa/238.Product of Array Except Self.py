class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 [1, 2, 3, 4 ]
        #    1  1  2  6
        #   [1, 2, 3, 4] 1
        #    24  12  4  1  
        prefix, postfix = 1, 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
#TC:O(n)
#SP:O(n)