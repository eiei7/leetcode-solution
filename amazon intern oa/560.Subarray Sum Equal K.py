class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        total = 0
        res = 0
        for num in nums:
            total += num
            differ = total - k
            res += hashmap.get(differ, 0)
            hashmap[total] = 1 + hashmap.get(total, 0)
        return res
#TC:O(n)
#SP:O(n)