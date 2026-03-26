# week05-4.py 昨天 2025-03-25 的挑戰題
# LeetCode 3546. Equal Sum Grid Partition I
# grid 矩陣，能否切一刀兩邊和剛好相同
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum( [sum(row) for row in grid] ) # 全部加起來

        preSum = 0 # 對應橫切一刀
        for row in grid: # 逐個 row 處理
            preSum += sum(row) #把 row 整行加進來
            if preSum == total - preSum: # 上半部 == 下半部
                return True
        preSum = 0 # 對應直切一刀
        for col in zip(*grid): # 把 transpose轉置矩陣, 逐個 處理
            preSum += sum(col)
            if preSum == total - preSum:
                return True
        return False
