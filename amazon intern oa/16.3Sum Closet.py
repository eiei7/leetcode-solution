class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        distance = float('inf')
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(target - total) < distance:
                    distance = abs(target - total)
                    res = total
                if total < target:
                    l += 1
                else:
                    r -= 1
        return res

#TC:O(n^2)
#SP:O(1)