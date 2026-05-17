class Solution:
    def validPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s)-1
        counter = 0

        while l <= r:
            
            while not s[l].isalnum() and l < r:
                l +=1
            
            while not s[r].isalnum() and l < r:
                r -=1
            
            if s[l].lower() != s[r].lower():

                if l < r-1 and s[l+1].lower() == s[r].lower() and s[l+2].lower() == s[r-1].lower():
                    l += 1
                elif l < r-1 and s[r-1].lower() == s[l].lower() and s[r-2].lower() == s[l+1].lower():
                    r -= 1
                elif l == r-1:
                    l +=1
                counter += 1

            if s[l].lower() != s[r].lower() or counter >= 2:
                    return False
            
            l += 1
            r -= 1
        
        return True