# week16-4.py 學習計畫 Intervals 第2題
# LeetCode 452. Minimum Number of Arrows to Burst Balloons
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        ans = 0
        previous_end=-inf
        for start,end in points:
            if previous_end < start:
                ans += 1
                previous_end = end
        return ans
