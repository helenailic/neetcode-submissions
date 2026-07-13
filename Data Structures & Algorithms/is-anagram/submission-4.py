from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_dict = defaultdict(int)
        for c in s:
            my_dict[c] += 1
        
        for c in t:
            my_dict[c] -= 1

        for key in my_dict:
            if my_dict[key] != 0:
                return False

        return True