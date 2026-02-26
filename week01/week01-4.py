# week01-4.py 學習計畫 Array/String 第3題
# LeetCode 1431. Kids With the Greatest Number of Candies
# 你給額外的extracandies後,小朋友手裡的糖果,會不會是最多的?
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # 救命用，只要test、result有綠色accept就好了
        ans = [] # 答案的true和false將塞在裡面
        best = max(candies) #目前小朋友最多有幾個糖?
        for candie in candies: # 逐一檢查，如果把extracandies給小朋友
            if candie + extraCandies >= best:ans.append(True)
            else: ans.append(False) # 他會不會 >= 最多的<依序塞入ans
        return ans
