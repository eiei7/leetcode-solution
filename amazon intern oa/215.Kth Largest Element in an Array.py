"""
Method1: quick sort
"""
# second-version
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [i for i in nums if i > pivot]#put large num in left arr
        mid = [i for i in nums if i == pivot]
        right = [i for i in nums if i < pivot]#smaller num in right arr
        print(left, mid, right)
        L, M = len(left), len(mid)
        if k <= L:#count k from 1, len also count from 1
            return self.findKthLargest(left, k)
        elif k > (L + M):#pivot是随机选的，不一定是第k大元素
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]

"""
Method2: heap
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-i for i in nums]#minheap
        heapq.heapify(maxheap)
        
        while k > 1:
            heapq.heappop(maxheap)
            k -= 1
        return -maxheap[0]

#TC: AVT: O(n + klogn) the worst case: O(nlogn)

"""
Method3: sorted()
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]

#TC: O(nlogn)


