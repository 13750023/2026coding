#week08-5.py 學習計畫 Binary Search 第3題
#LeetCode 162. Find Peak Element 找到比左右鄰居大的那個
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #笨方法:for迴圈不行嗎(因為這題只有1000個數)
        N=len(nums) #陣列大小N
        if N==1:return 0 #i:0最大(只有1個數，就是最大，別再nums[i-1]nums[i+1]了啦)
        for i in range(N):#每個index i 都去試左邊，右邊
            if i==0: #沒有左邊,只測右邊(要比右邊大)
                if nums[i]>nums[i+1]:return i
            elif i==N-1:#最右邊，沒有右邊，只測左邊(要比左邊大)
                if nums[i]>nums[i-1]:return i
            #下面可能會當機，因i-1或i+1會超過範圍，所以加上面的if
            elif nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
            #這題其實希望你用Binary Search但題目有漏，竟然暴力for迴圈也可解
