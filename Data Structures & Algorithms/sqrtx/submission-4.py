class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0
        while l <= r:
            m = (l + r) // 2
            power_2 = m * m
            if power_2 > x:
                r = m - 1
            elif power_2 < x:
                l = m + 1
                res = m
            else:
                return m
        return res
