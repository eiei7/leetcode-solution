class Solution:
  def minimumHealth(self, damage, armor) -> int:
    maxdamage = max(damage)
    return sum(damage) + 1 - min(armor, maxdamage) # armor只在某个level，抵挡伤害，如果armor比当前的伤害值大，也只会帮助不减少当前的伤害值的大小

damage = [2,5,3,4]
armor = 7
obj = Solution()
obj.minimumHealth(damage, armor)