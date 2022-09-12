"""
Method: Greedy
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * (len(nums) - 1) + [True]
        destination = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = True if i + nums[i] > destination else dp[i + nums[i]]
            if dp[i]:
                destination = i
        return dp[0]
    #TC:O(n)
    #SC:O(n)
"""
Method: Brute force
"""
    #TC:O(n^n)
    #SC:O(n^2)