class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda x: x[0])
        preEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            if preEnd > start:#overlapping-> so, count+1 and update preEnd(pick the smaller one)
                preEnd = min(preEnd, end)
                res += 1
            else:
                preEnd = end
        return res
#Time Complexity: O(nlogn) + O(n - 1)
#Space Complexity: O(1)