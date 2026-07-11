class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCnt = 0 
        cnt = 0
        for n in nums:
            if n == 1:
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            else:
                cnt = 0
        return maxCnt
