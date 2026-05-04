class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        hash_s = {}
        hash_t = {}
        if len(t) != n:
            return False
        for i in range(n):
            hash_s[s[i]] = hash_s.get(s[i], 0) + 1
            hash_t[t[i]] = hash_t.get(t[i], 0) + 1

        print(hash_t, hash_s)
        if hash_t == hash_s:
            return True
        else:
            return False