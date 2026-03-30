class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Using the hashmap structure to store letters as keys and
        # counting their string appearances in values
        # .get(s[i], 0) - 0 is the default value
        # We could use sort, but that is O(nlogn) at best, which is worse then O(s+t)
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for letter in countS:
            if countS[letter] != countT.get(letter, 0):
                return False

        return True
