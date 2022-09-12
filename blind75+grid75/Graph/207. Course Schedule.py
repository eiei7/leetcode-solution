"""
Method: dfs
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i : [] for i in range(numCourses)}
        #eg.[[0,1],[0,2],[1,3],[1,4],[3,4]] -> {0:[1,2],1:[3,4],2:[],3:[4],4:[]}
        #course with no outdegree can be finished without requiring prerequisites.
        for crs, pre in prerequisites:
            hashmap[crs].append(pre)
        
        visited = set() #record the node along with the current path
        
        def dfs(crs):
            if crs in visited:#loop existing
                return False
            if hashmap[crs] == []:#must can be finished
                return True
            
            visited.add(crs)
            for pre in hashmap[crs]:#一旦出现loop就返回False
                if not dfs(pre): return False
            visited.remove(crs)
            hashmap[crs] = [] #只要上面程序能走完，就表示当前的course能上，在hashmap可以标记为[] (no prerequisites' requirement)
            return True
        
        for crs in range(numCourses):#可能存在非连通子图，如1234是连通的，5->6单独连通
            if not dfs(crs):
                return False
        return True

#Time Complexity: O(n + p) #n是numCourses的大小，P是prerequisites的表长（一维）
#Space Complexity: O(n + p)

