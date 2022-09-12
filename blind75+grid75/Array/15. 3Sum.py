"""
Method1: two pointers
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, val in enumerate(nums):
            if val > 0:#若当前的数大于0，因为数组递增，所以另外两个也大于0，不可能存在和为0的情况
                break
            if i > 0 and val == nums[i - 1]:#跳过重复出现的元素
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if val + nums[l] + nums[r] > 0:
                    r -= 1
                elif val + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    while l + 1 < r and nums[l + 1] == nums[l]:#跳过重复出现的元素,先处理左边或右边都可以，因为上面的if语句会调整参数
                        l += 1
                    l += 1
        return res

#Time Complexity: O(nlogn)(sorting) + O(n^2) = O(n^2)
#Space Complexity: O(1) or O(n)(some sorting method did use some memory)