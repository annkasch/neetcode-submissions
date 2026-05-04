class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        map_diff = {}
        for i in range(n):
            if nums[i] in map_diff:
                return[map_diff[nums[i]], i]
            diff = target - nums[i]
            map_diff[diff] = i

        return []
        