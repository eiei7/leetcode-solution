"""
Method: Bottom to up DP
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) + [True]
        
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
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
            cur_index = q.popleft()
            for i in range(cur_index + 1, len(s) + 1):
                if i in visited:#edge case eg.["aaaaaa"] ["aaa","aa"]
                    continue
                if s[cur_index : i] in wordDict:
                    if i == len(s):
                        return True
                    q.append(i)
                    visited.add(i)
        return False

# Time Complexity: O(n^2) (O(n^3)若考虑比较字符串的时间)
# Space Complexity: O(n)
