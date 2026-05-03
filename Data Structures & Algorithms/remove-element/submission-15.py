class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = n_new = len(nums)
    
        for i in range(n-1,-1,-1):
            if nums[i] == val:
                for j in range(i+1,n, 1):
                    nums[j-1] = nums[j]
                
                nums[n-1] = 0
                n_new -= 1
        return n_new
        