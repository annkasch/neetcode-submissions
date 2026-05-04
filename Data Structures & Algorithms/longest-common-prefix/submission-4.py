class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_length = len(strs[0])

        for str in strs[1:]:
            shared = True
            i = 0
            if len(str) < prefix_length:
                prefix_length = len(str)
            while shared == True and i < prefix_length:
                if str[i] != strs[0][i]:
                    prefix_length = i
                    shared = False
                i += 1
        return strs[0][:prefix_length]



        