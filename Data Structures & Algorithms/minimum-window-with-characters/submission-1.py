from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLength = float("inf")
        minIndices = (0, 0)
        char_freqs = defaultdict(int)
        goal_char_freqs = defaultdict(int)
        for c in t:
            goal_char_freqs[c] += 1
        need = len(goal_char_freqs)
        have = 0 #unique chars matching their frequency

        l = 0
        for r in range(len(s)):
            char_freqs[s[r]] += 1

            if char_freqs[s[r]] == goal_char_freqs[s[r]]:
                have += 1
            
            while have == need:
                if r-l+1 < minLength:
                    minLength = r-l+1
                    minIndices = (l, r)
                char_freqs[s[l]] -= 1
                if char_freqs[s[l]] < goal_char_freqs[s[l]]:
                    have -= 1
                l += 1
            
        if minLength == float("inf"):
            return ""
        else:
            return s[minIndices[0]: minIndices[1] + 1]