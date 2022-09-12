"""
Method: DP
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxprofit(nums):
            sum1, sum2 = 0, 0
            for num in nums:
                tmp = max(sum1 + num, sum2)
                sum1 = sum2
                sum2 = tmp
            return sum2
        
        return max(maxprofit(nums[:-1]), maxprofit(nums[1:])) if len(nums) != 1 else nums[0]

#Time Complexity: O(n)
#Space Complexity: O(1)