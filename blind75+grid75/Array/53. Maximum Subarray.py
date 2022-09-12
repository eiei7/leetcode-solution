class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = max(nums)
        tmp = 0
        for num in nums:
            tmp += num
            maxsum = max(maxsum, tmp)
            if tmp <= 0:
                tmp = 0
        return maxsum

#TC:O(n)
#SC:O(1)

