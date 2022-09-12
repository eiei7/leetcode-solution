class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            if start <= res[-1][1]: #res[-1][1]: the lastest interval in res array
                res[-1][1] = max(end, res[-1][1])#they are overlapping->only update end, because we had already sorted array by the first element
            else:
                res.append([start, end])
        return res

#Time Complexity: O(nlogn)(cuz sort)+ O(n) 
#Space Complexity: O(n)

