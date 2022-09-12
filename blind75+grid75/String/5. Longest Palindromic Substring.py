class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [0, 0]
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > res[1] - res[0]:
                    res = [l, r]
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > res[1] - res[0]:
                    res = [l, r]
                l -= 1
                r += 1
        return s[res[0]:res[1] + 1]

#TC: O(n^2)
#sc: O(1)