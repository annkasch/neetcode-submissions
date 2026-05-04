class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        map_diff = {}
        for i, num in enumerate(nums):
            if num in map_diff:
                return[map_diff[num], i]
            diff = target - num
            map_diff[diff] = i

        return []
        