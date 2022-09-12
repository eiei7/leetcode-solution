"""
Method1: shift bit
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 #提取最低位/最右
            res |= bit << (31 - i) #i从0开始，需移动31-i位
        return res

#TC:O(1)
#SP:O(1)

"""
Method1: zfill + bottom to up
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:].zfill(32)
        res = 0
        for i in range(32):
            res += int(n[i]) * 2 ** i #pow(2,i)
        return res
#TC:O(1)
#SP:O(1)