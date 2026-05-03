class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = best = 0

        for num in nums:
            current = current + 1 if num == 1 else 0
            best = max(best, current)

        return best


        