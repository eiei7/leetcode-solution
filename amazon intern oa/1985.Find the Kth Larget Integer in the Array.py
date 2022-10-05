class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxheap = [-int(num) for num in nums]
        heapq.heapify(maxheap) # logn
        for i in range(k):
            res = heapq.heappop(maxheap)#logn
        return str(-res)
#TC:O(klogn)
#SP:O(n)