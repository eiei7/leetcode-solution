class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        nums = []
        for log in logs:
            data = log.split(" ")
            if not data[1].isnumeric():
                letters.append((" ".join(data[1:]), data[0]))
            else:
                nums.append(log)
        letters.sort(key = lambda x: (x[0], x[1]))
        return [letter[1] + " " + letter[0] for letter in letters] + nums

#TC:O(n) or O(nlogn)
#SP:O(n)