"""
Method: find the start of the subsequence
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:#O(1)*n = O(n)
            if (num - 1) not in nums:
                count = 0
                while count + num in nums:
                    count += 1
                res = max(res, count)
        return res

#Time Complexity: O(n)
#Space Complexity: O(1)

"""
Method: two pointers
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()#O(nlogn)
        res = 1
        count = 1
        for i in range(1, len(nums)): #O(n)
            if nums[i] == nums[i - 1] + 1:
                count += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                res = max(res, count)
                count = 1
#res = max(res, count) need to be update again
        return max(res, count) if nums else 0

#TC: O(nlogn)