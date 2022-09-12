"""
Method: DP
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for total in range(1, target + 1):#O(n)
            dp[total] = 0 #total理解为决策树中得到该值的路径的个数，如dp[1]=1,dp[2]=2,dp[3]=4,dp[4]=7，能够得到4（结点的值）的路径的个数是7
            for num in nums:#O(n * m)
                dp[total] += dp.get(total - num, 0)
        return dp[target]
    
#Time Complexity: O(n * m) #n=target, m=len(nums)
#Space Complexity: O(n)