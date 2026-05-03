class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        nums_new = [0]*2*n
        for i in range(n):
            nums_new[i] = nums[i]
            nums_new[i+n] = nums[i]
        
        return nums_new