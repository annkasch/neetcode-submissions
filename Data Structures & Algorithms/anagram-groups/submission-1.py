class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = []
        hash_list = []
        for str in strs:
            hash_map = {}
            for ch in str:
                hash_map[ch] = hash_map.get(ch,0) + 1
            
            add = -1
            for i, ana in enumerate(hash_list):
                if ana == hash_map:
                    add = i
                    break

            if add > -1: 
                anagram_list[add].append(str)
            else:
                hash_list.append(hash_map)
                anagram_list.append([str])
        
        return anagram_list

        