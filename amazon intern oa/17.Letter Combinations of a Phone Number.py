"""
Method1: backtracking
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        hashmap = {'2': 'abc', '3': 'def', 
                   '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs',
                   '8': 'tuv', '9': 'wxyz'}
        res = []
        def dfs(i, word):
            if i == len(digits):
                res.append(word)
                return
            for c in hashmap[digits[i]]:
                dfs(i + 1, word + c)
                
        dfs(0, "")
        return res
#TC:O(4^n) or O(n * 4^n) why *n ?
#SP:O(4^n)

#why it doesn't work?
#word += [c]
#dfs(i + 1, word)
#word.remove([word[-1])

"""
Method2: Interation
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        hashmap = {'2': 'abc', '3': 'def', 
                   '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs',
                   '8': 'tuv', '9': 'wxyz'}
        
        res = ['']
        for num in digits:
            tmp = []
            for c in hashmap[num]:
                tmp += [c2 + c for c2 in res]
            res = tmp
        return res

