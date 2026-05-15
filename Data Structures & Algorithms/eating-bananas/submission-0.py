class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max = 0
        for i in piles:
            if i > max:
                max = i
        L = 1
        R = max
        while L <= R:
            M = (L + R)//2
            max_hours = 0
            for i in piles:
                max_hours += -(-i // M)
            if max_hours > h:
                L = M + 1
            elif max_hours <= h:
                if L == R:
                    return M
                R = M

        return -1
                
        