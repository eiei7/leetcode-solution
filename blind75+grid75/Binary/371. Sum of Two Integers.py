"""
mid = left + (right - left) / 2
func getmid(a, b):
     return (a & b) + (a ^ b) >> 1
2 * left + right - left = left + right
= (a & b) << 1 + (a ^ b)
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        MIN = 0x80000000 # 4*8 = 32
        mask = 0xFFFFFFFF
        
        while b != 0:
            tmp = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = tmp
        return a if a < MAX else ~(a ^ mask) #deal with negative number