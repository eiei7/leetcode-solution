"""
Method1: count # of '1' in string
"""

"""
Method2: bit operation
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if n % 2 == 1:
                res += 1
            n = n >> 1
        return res

#Time Complexity: O(32) = O(1)

"""
Method3: n = n & (n - 1)
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res

#Time Complexity: O(1) depends on # of '1'

"""
Method4: bit << i, (n & bit) >> i
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = 1 << i #为了判断n的第i位是否为1or0
            res += ((n & bit) >> i)#res每次只需要计数加1，因此(n&bit)要移到最低位
        return res

#TC: O(1)
#SC: O(1)