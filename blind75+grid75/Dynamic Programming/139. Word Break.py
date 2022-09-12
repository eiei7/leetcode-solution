"""
Method: Bottom to up DP
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) + [True]
        
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:#下面第一个判断句加括号执行更快
                if (i + len(word)) <= len(s) and s[i: i + len(word)] == word:#在保证当前下标开始读len(word)长度的字母时，没有超出s的最大下标的前提下，判断两个单词是否相同
                    dp[i] = dp[i + len(word)]
                if dp[i]:#找到了，就跳出当前内循环
                    break
        return dp[0]

# Time Complexity: O(n*m) (O(n*m*n)：若考虑判断单词是否相等的时间)
# Space Complexity: O(n)

"""
Method: dfs
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)
        
        while q:
            cur_index = q.popleft()#bfs也可以，visited的作用都是一样的
            for i in range(cur_index + 1, len(s) + 1):
                if i in visited:#如果不用visited检测的话，已经被标记过的i可能又会被标记一次，太耗时(因为cur_index < 被标记的i，所以新的循环中，i可能会走到之前被标记的i的位置，为了避免再次执行下面的四句话，必须使用visited记录),eg.["aaaaaa"] ["aaa","aa"]
                    continue
                if s[cur_index : i] in wordDict:
                    if i == len(s):
                        return True
                    q.append(i)
                    visited.add(i)#标记i表示i下标之前的subtring满足目标函数
        return False

# Time Complexity: O(n^2) (O(n^3)若考虑比较字符串的时间)
# Space Complexity: O(n)