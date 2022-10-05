class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:#char元素也有大小
                k -= 1
                stack.pop()
            stack.append(c)
        #e.g ['1','2','3','4'] (after for loop), k still be 1
        stack = stack[:len(stack) - k]
        res = "".join(stack) #there might be some leading '0'
        return str(int(res)) if res else '0' #if res != ""
#TC:O(n)
#SP:O(n)