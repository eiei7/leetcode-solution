"""
Method: stack
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}
        for c in s:#O(n)
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False 
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
