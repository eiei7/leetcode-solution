"""
Method1: DP
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[], [nums[-1]]]
        for i in range(len(nums) - 2, -1, -1):
            res += [[nums[i]] + x for x in res]
        return res

#TC: O(n * 2^n)
#SP: O(2^n) # complete set

"""
Method2: dfs
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(i, path):
            self.res.append(path)
            for k in range(i, len(nums)):
                dfs(k + 1, path + [nums[k]])
        
        self.res = []
        dfs(0, [])
        return self.res

#TC: O(n * 2^n)
#SP: O(2^n) # complete set