class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x: -x[1])
        print(boxTypes)
        res = 0
        for num, units in boxTypes:
            if truckSize > 0:
                res += num * units if num <= truckSize else truckSize * units
                truckSize -= num
        return res
#TC:O(n)
#SP:O(1)