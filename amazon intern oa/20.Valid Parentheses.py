class Solution:
    def isValid(self, s: str) -> bool:
        #fasle: (], )(, [
        hashmap = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if not stack or stack[-1] != hashmap[c]:
                    return False
                else:
                    stack.pop()
        return False if stack else True