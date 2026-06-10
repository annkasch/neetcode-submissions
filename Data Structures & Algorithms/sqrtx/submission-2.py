class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        if x == 0:
            return 0
        elif x == 1:
            return 1
        while l < r:
            m = (l + r) // 2
            sqrt = m * m
            if sqrt == x:
                return m
            elif sqrt > x:
                r = m
            else:
                if m == l:
                    return m
                l = m
                
