# week07-2b.py 學習計畫 Stack 第2題
# LeetCode 735. Asteroid Collision
# 正的向右、負的向左, 大的會把小的消滅。一樣大、一起死
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a<0: # 正的向右, 不會跟左邊的相撞

                while stack and stack[-1]>0: # 目前有存, 且右邊正的、向右,會相撞
                    if abs(stack[-1]) == abs(a): # 絕對值大小都相同,都消滅!
                        stack.pop() #消滅了、吐掉
                        a = 0 # 也消滅了
                        break # 離開迴圈
                    elif abs(stack[-1]) > abs(a): # 右邊的比較小, 消滅右邊
                        a = 0 # 消滅右邊
                        break
                    else: # 左邊比較小, 消滅左邊
                        stack.pop() # 消滅、吐掉 (這裡不用 break)
            if a != 0: stack.append(a)
        return stack
