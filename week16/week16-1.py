# week16-1.py 學習計畫 Backtracking 第1題
# LeetCode 17. Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        table={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        def helper(i,prefix):
            if i==len(digits):
                ans.append(prefix)
                return
            for c in table[int(digits[i])]:
                helper(i+1,prefix+c)
        helper(0,"")
        return ans
