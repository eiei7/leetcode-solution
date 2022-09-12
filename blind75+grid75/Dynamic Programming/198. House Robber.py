"""
Method: DP
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        me, you = nums[-1], 0
        for i in range(len(nums) - 2, -1, -1):
            tmp = me
            me = max(nums[i] + you, me)
            you = tmp
        return me

#Time Complexity: O(n)
#Space Complexity: O(1)