class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = defaultdict(int)
        n = len(nums)
        max_count = 0
        max_num = 0
        for num in nums:
            count_map[num] += 1
            if max_count < count_map[num]:
                max_num = num
                max_count = count_map[num]
        
        return max_num
        