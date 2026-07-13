from collections import defaultdict

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = (''.join(c for c in s if c.isalnum())).lower()
        begin = 0
        end = len(s_clean)-1

        for i in range(len(s_clean)):
            if (begin == end) or (begin > end):
                break
            if s_clean[begin] != s_clean[end]:
                return False
            else:
                begin += 1
                end -= 1
        
        return True

