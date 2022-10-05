#use two set + one list
#use set() for search is faster but more extra space cost
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hashmap[crs].append(pre)
        
        visited = set()
        record = set()
        res = []
        def dfs(course):
            if course in visited:
                return False
            if course in record:
                return True
            
            visited.add(course)
            for nbs in hashmap[course]:
                if not dfs(nbs):
                    return False
            visited.remove(course)
            record.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

