class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counts = 0
        precounts = 0
        for i in range(len(nums)):
            
            if nums[i] == 1:
                counts += 1
            else:
                counts = 0
            if precounts < counts:
                    precounts = counts
        
        return precounts


        