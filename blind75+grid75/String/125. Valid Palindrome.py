"""
Method: lower()
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        for c in s:
            if (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122) or c.isnumeric():
                tmp += c
        tmp = tmp.lower()
        return tmp == tmp[::-1]

#TC: O(n)
#SC: O(1)

"""
Method: two pointers
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalphanumeric(c):
            return (ord('a') <= ord(c) and ord(c) <= ord('z')) or (ord('A') <= ord(c) and ord(c) <= ord('Z')) or (ord('0') <= ord(c) and ord(c) <= ord('9'))
        
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not isalphanumeric(s[l]):
                l += 1
            while l < r and not isalphanumeric(s[r]):
                r -=1 
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

#TC: O(logn)
#SC: O(1)