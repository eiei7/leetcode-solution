"""
Method1: Counter
"""
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first_word = Counter(words[0])
        #result like Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1})
        for word in words[1:]:
            first_word &= Counter(word)
        
        res = []
        for c, val in first_word.items():
            res += [c] * val
        return res

"""
Method2: bucket sort
"""

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        buckt = []
        for w in words:
            tmp = [0] * 26
            for c in w:
                tmp[ord(c) - ord('a')] += 1
            buckt.append(tmp)
        
        res = []
        for i in range(26):
            count = float('inf')
            for w in buckt:
                count = min(count, w[i])
            if count:
                res += [chr(ord('a') + i)] * count
        return res
#TC:O(n)
#SP:O(26*n)=O(n)