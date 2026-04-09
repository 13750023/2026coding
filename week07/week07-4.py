# week07-4.py 學習計畫 Stack 第3題, 有點難
# LeetCode 394. Decode String
# 將字串解碼 數字代表重複的次數 會把右邊方括號裡的字串重複
class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] # 利用 stack 處理方括號及對應數字
        nowN, nowS = 0, '' # 左邊 nowN 數字 vs.右邊 nowS 字串
        for c in s:
            if c.isdigit(): # 若是數字 就用十進位組合起來
                nowN = nowN*10+int(c)
            elif c.isalpha(): # 如果是字母 就讓字串變長
                nowS += c
            elif c =='[': # 上括號: 數字字串放入 stack
                stack.append( (nowN, nowS) )
                nowN, nowS = 0, '' # 一組新的數字字串
            elif c==']': # 下括號:取出數字字串
                prevN, prevS = stack.pop()
                nowS = prevS + prevN * nowS #重複的次數 * 字串
        return nowS
