"""
Method: DP
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for total in range(1, target + 1):#O(n)
            dp[total] = 0 #dp[1]=1,dp[2]=2,dp[3]=4,dp[4]=7
            for num in nums:#O(n * m)
                dp[total] += dp.get(total - num, 0)
        return dp[target]
    
#Time Complexity: O(n * m) #n=target, m=len(nums)
#Space Complexity: O(n)
