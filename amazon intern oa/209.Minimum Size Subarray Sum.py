class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l, r = 0, 0
        total = 0
        while r < len(nums):
            total += nums[r] 
            while l <= r and  total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
            r += 1
        return res if res != float('inf') else 0

#limited exceed time when using sum(nums[l:r + 1])
#TC:O(nlogn)
#SP:O(1)