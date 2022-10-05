"""
Method1: Dijkstra
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hashmap = collections.defaultdict(list)
        for u, v, w in times:
            hashmap[u].append((v, w))

        minheap = [(0, k)]#把w放在node前面我因为heappop的时候会将以第一个元素排序的最小值输出
        visit = set()
        time = 0
        while minheap:
            w, v = heapq.heappop(minheap)
            if v in visit:
                continue
            visit.add(v)
            time = max(time, w)
            for nei, w2 in hashmap[v]:
                if nei not in visit:
                    heapq.heappush(minheap, (w + w2, nei))
        
        return time if len(visit) == n else -1

#TC:O(VlogV + ElogV)
#SP:O(V + E)

"""
Method2: Bellman-ford
"""
class Solution:
    def networkDelayTime(self, times, n, k) -> int:
        #initialization
        dp = [float('inf') for i in range(n + 1)]
        dp[k] = 0 #dp[source] = 0
        dp[0] = 0 
        stop = True
        j = 0
        
        while j < n - 1 or stop:
            stop = False
            for u, v, w in times:
                print(1,dp[v], dp[u] + w)
                if dp[v] > min(dp[v], dp[u] + w):
                    dp[v] = min(dp[v], dp[u] + w)
                    stop = True
                print(2, dp[v], dp[u] + w)
                j += 1

        if max(dp) == float('inf'):
            return -1 
        else:
            return max(dp)

times = [[2,3,2],[1,2,59],[1,3,-46],[3,1,44],[3,2,89],[2,1,21]]
n = 5
k = 1
x = Solution()
print(x.networkDelayTime(times, n, k))