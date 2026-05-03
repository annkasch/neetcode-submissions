class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = n_new = len(nums)

        for i in range(n-1, -1, -1):
            if nums[i] == val:
                nums[i] = nums[n_new-1] if i != n-1 else 0
                nums[n_new-1] = 0
                n_new -= 1
        return n_new