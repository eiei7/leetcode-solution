"""
Method1: two pointers
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and val == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if val + nums[l] + nums[r] > 0:
                    r -= 1
                elif val + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    while l + 1 < r and nums[l + 1] == nums[l]:
                        l += 1
                    l += 1
        return res

#Time Complexity: O(nlogn)(sorting) + O(n^2) = O(n^2)
#Space Complexity: O(1) or O(n)(some sorting method did use some memory)
