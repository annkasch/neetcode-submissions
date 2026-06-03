class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        

        if target > nums[n-1]:
            return n
        elif target < nums[0]:
            return 0
        
        i = 0
        j = n-1
        m = 0
        while i < j:
            m = (j + i) // 2
            if target > nums[m]:
                if i != m:
                    i = m
                else:
                    break
            else:
                if j!=m:
                    j = m

        k = m
        if nums[k] > target:
            k -=1
        elif nums[k] < target:
            k += 1
        return k