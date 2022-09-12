"""
Method: Bottom to up DP
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
            
        return dp[0][0]

#Time Complexity: O(n * m)
#Space/Memory Complexity: O(n * m)

"""
Method: brute force
"""

#TC:O(2^(n + m)) # number of sebsequences of a string is (n 0) + (n 1) + ... + (n n) = 2^n
#SC:O(2^n + 2^m)