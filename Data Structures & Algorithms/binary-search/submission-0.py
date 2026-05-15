class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L = 0
        R = len(nums)-1

        while L <= R:
            M = (R + L)//2
            if target > nums[M]:
                L = M + 1
            elif target == nums[M]:
                return M
            else:
                R = M - 1
            
        return -1

        