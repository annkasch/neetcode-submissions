class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        pairs = {"(":")", "{":"}", "[":"]"}

        if n % 2 != 0:
            return False
        valid = True
        i=0
        while i < n:
            print(i, s[i])
            if s[i] not in pairs:
                return False
            if s[i+1] == pairs[s[i]]:
                i += 2
            elif s[n-1] == pairs[s[i]]:
                n -= 1
                i+=1
            else:
                return False

        return valid
