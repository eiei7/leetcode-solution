class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        hashset = set(words)
        
        def check(word):
            for i in range(1, len(word)):
                if word[:i] in hashset and (word[i:] in hashset or check(word[i:])):
                    return True
            return False
        
        res =[]
        for w in hashset:
            if check(w):
                res.append(w)
        return res

#TC:O(m * n)
#SP:O(n)