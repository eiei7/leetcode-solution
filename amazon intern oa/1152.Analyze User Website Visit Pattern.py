import collections
import itertools
class Solution:
  def mostVisitedPattern(self, username, timestamp, website):
    packaged = sorted(zip(timestamp, username, website), key = lambda x: x[0])
    hashmap = collections.defaultdict(list)
    for t, u, w in packaged:
      hashmap[u].append(w)
    count = collections.defaultdict(int)
    for acts in hashmap.values():
      combs = set(itertools.combinations(acts, 3))#O(3!)
      for comb in combs:
        count[comb] += 1
    count = sorted(count, key = lambda x: (-count[x], x))
    return count[0]

username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10] 
website = ["home","about","career","home","cart","maps","home","home","about","career"]
x = Solution()
x.mostVisitedPattern(username, timestamp, website)

#TC:O(n)
#SP:O(n) # of combinatiomns: nCr = n! / r! * (n - r)! 