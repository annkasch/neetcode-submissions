class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        right = len(s)-1
        left = 0
        while left < len(s)/2:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            right -= 1
            left += 1



        