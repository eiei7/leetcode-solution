"""
Method: DP
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,1]
        for i in range(n - 1):
            tmp = dp[0]
            dp[0] = dp[0] + dp[1]
            dp[1] = tmp
        return dp[0]

#Time Complexity: O(n)
#Space Complexity: O(1)
