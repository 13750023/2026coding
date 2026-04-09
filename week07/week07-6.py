# week07-6.py 學習計畫 queue 第2題
# LeetCode 649. Dota2 Senate
# Dota2 兩個陣營 Radiant/聖輝 和 Dire/魔豔 照 senate 字串的順序出現
# 從左到右輪、輪到的人、可把後面任一個敵對陣營除掉。
# 巡完一輪，繞道前面繼續，直到全部字母皆相同，問最後哪個陣營得勝
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        print(senate, type(senate)) # 先印出 senate
        print(list(senate),type(list(senate))) # 印出 list(senate)
        # 樓上兩行, 印出字串、list(...)。下面印出 deque(...)
        queue = deque(list(senate))
        print(queue,type(queue)) # 印出來,瞭蹶它是進階資料結構
        banR, banD = 0, 0 #目前被消滅的次數, 都還是0
        R, D = senate.count('R'),senate.count('D') # 字串裡,數一數,目前各有幾個人?
        while queue: # 只要還有人在排隊,就繼續進行互相 Ban對方的遊戲
            now = queue.popleft() # 左邊吐出個字母, 他要消滅敵對陣營
            if now=='R':
                if banR>0: # 已經紀錄要消滅1個人
                    banR -= 1 # 用掉1個被消滅的名額
                    R -= 1 # 馬上少掉1個人
                    #continue # 你一出現, 就已經被消滅了(換下一位)
                else: # 你沒有被消滅,太好了,你可以反過來消滅堆方
                    banD += 1
                    queue.append(now) #再到最右邊排隊
            else: # now=='D'
                if banD > 0:
                    banD -= 1
                    D -= 1
                    #continue
                else:
                    banR += 1
                    queue.append(now)
            if R==0: return 'Dire' # 把 R 消滅光, 'D' 就得勝
            if D==0: return 'Radiant' # 把 D 消滅光, 'R' 就得勝
