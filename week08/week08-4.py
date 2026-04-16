#week08-4.py 學習計畫 Binary Search 第2題
# LeetCode 2300. Successful Pairs of Spells and Potions
# 想知某種 spells[i]魔法,配幾種藥水可以成功?
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()#藥水小到大排好
        P=len(potions)#有P種藥水
        ans=[]
        for spell in spells:#每一種魔法都試一次
            now= P-bisect_left(potions,success/spell)
            ans.append(now)#全部藥水有P瓶-會失敗的藥水??瓶
        return ans
