"""
Method1: hashset
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

#Time Complexity: O(n)
#Space Complexity: O(n)

"""
Method2: two pointers
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #sort + two points
        nums.sort()
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                return True
        return False

#Time Complexity: O(nlogn)
#Space Complexity: O(1)

"""
Method3: hashmap
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #brute force
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        return True if max(hashmap.values()) > 1 else False

#Time Complexity: O(n)
#Space Complexity: O(n)

"""
Method3: brute force
"""
#use two layer for loops 

#Time Complexity: O(n^2)
#Space Complexity: O(1)