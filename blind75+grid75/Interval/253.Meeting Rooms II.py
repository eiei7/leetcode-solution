from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        i, j = 0, 0
        res, count = 0, 0
        while i < len(start):
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
        return res

#TC: O(nlogn) + O(n) ~= O(nlogn)
#SC: O(2n) = O(n)