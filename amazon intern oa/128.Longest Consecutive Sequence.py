class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            curSum = 0
            if num - 1 not in nums:
                while num + curSum in nums:
                    curSum += 1
                    res = max(res, curSum)
        return res