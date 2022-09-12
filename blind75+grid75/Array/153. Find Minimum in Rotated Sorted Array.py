"""
Method1: binary search
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        mid = (len(nums) - 1) // 2
        if mid == 0 or mid == len(nums):#e.g nums=[1] or nums=[2,1]
            return min(nums)
        if nums[0] < nums[-1]:
            return nums[0]
        if nums[0] < nums[mid]:
            return self.findMin(nums[mid + 1:])
        else:
            return self.findMin(nums[:mid + 1])

#Time Complexity: O(logn)
#Space Complexity: O(1)

"""
Method1-version2
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] > nums[l] or nums[mid] > nums[mid - 1]:
                r = mid - 1
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
        mid = (l + r) // 2
        return nums[mid]

#Time Complexity: O(logn)
#Space Complexity: O(1)
