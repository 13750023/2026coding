# week16-2.py 學習計畫 Backtracking 第2題
# LeetCode 216. Combination Sum III
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def helper(now,i,k,n):
            if k==0 and n==0:
                ans.append(now)
            if k<=0 or n<=0:return
            for ii in range(i,10):
                helper(now+[ii],ii+1,k-1,n-ii)
        helper([],1,k,n)
        return ans
