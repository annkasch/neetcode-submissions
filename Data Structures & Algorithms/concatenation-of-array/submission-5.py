class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [a for i in range(2) for a in nums]
        return ans