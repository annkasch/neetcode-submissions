class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit() and abbr[j]!="0":
                num = ""
                
                while j < len(abbr) and abbr[j].isdigit():
                    num = num + abbr[j]
                    j += 1

                i += int(num)
                print(num, i)
                if i == len(word) and j == len(abbr):
                    return True
                elif i >= len(word):
                    return False
            if word[i] != abbr[j]:
                return False
            i += 1
            j += 1
        
        return True