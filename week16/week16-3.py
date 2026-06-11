# week16-3.py 學習計畫 Intervals 第1題
# LeetCode 435. Non-overlapping Intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        ans = 0
        previous_end=-inf
        for start,end in intervals:
            if previous_end <= start:
                previous_end = end
            else:
                ans += 1
        return ans
