"""
Method: stack
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}
        for c in s:#O(n)
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:#stack不为空且括号匹配上了
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False #stack为空，返回true，因为题给条件是s.length>1，所以stack为空的情况只能是成功了
#e.g stack=['(','('] we should return False

#TC: O(n)
#SC: O(n)

"""
Method-version2
"""
class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in range(len(s)):
            if not stack:
                if s[i] in hashmap:
                    stack.append(s[i])
                else:
                    return False
            elif stack[-1] in hashmap and s[i] == hashmap[stack[-1]]:
                stack.pop()
            else:
                stack.append(s[i])
        return True if not stack else False

#TC: O(n)
#SC: O(n) 