"""
Method: using join() and split()
"""
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        return ":;".join(strs)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        return str.split(":;")

"""
Method: deal with string
"""
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += (s + ":;")
        return res 

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        l = 0
        for r in range(len(str)):
            if str[r] == ':' and str[r + 1] == ';':
                res.append(str[l:r])
                l = r + 2
        return res
