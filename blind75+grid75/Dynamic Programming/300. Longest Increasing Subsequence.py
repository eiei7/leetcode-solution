"""
Method: Bottom to up DP
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums) 
        for i in range(len(nums) - 2, -1, -1):#bottom-up dp base case:dp[len(nums)-1]=1
            for j in range(i + 1, len(nums)):#e.g [0,3,2,3]0<3 and 0<2，所以在通过不断更新dp[i]在nums[i+1:]里找最大dp
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

#Time Complexity: O(n^2) actually near O(nlogn)
#Space Complexity: O(n)