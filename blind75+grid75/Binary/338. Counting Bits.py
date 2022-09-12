"""
Method1: DP
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp [0] * (n + 1) # array
        offset = 1 #[1,2,4,8,...,2^n]
        
        for i in range(1, n + 1):
            if offset * 2 == i:#需要改变offset
                offset = i
            dp[i] = 1 + dp[i - offset]#每2的倍数，dp都会在i-offset对应元素的dp基础上增加1
            
        return dp

#TC:O(n)
#SP:O(n)


"""
Method1-version2
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            if i & 1:#odd
                dp[i] = 1 + dp[i - 1]
            else:#even
                dp[i] = dp[i >> 1]
        return dp

"""
Method2: refer to 191. Number of 1 bits
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1): #O(n+1)
            count = 0
            while num: #
                num &= (num - 1)
                count += 1
            res.append(count)
        return res

#Time Complexity: O(nlogn)
