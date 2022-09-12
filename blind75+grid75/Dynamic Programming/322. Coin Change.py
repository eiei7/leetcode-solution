"""
Method: DP
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)#no shortest path-> get infinity
        dp[0] = 0 #as long as amount=0, output shoulbe be 0 (satisfies the goal)
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:#i > coin: 1+dp[i -coin];i==coin:dp[i]=dp[coin]
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != float('inf') else -1

#Time Complexity: O(n)
#Space Complexity: O(n)