class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphanumeric(c):
            if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (c in '0123456789'):
                return True
            return False
        
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not isAlphanumeric(s[l]):
                l += 1
            while l < r and not isAlphanumeric(s[r]):
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True