class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if not s:
            return ""

        dp = [False] * n
        start, max_len = 0, 1

        for r in range(n):
            new_dp = dp[:]
            for l in range(r, -1, -1):
                if s[l] == s[r] and (r - l <= 2 or dp[l+1]):
                    new_dp[l] = True
                    if r - l + 1 > max_len:
                        max_len = r - l + 1
                        start = l
                else:
                    new_dp[l] = False
            dp = new_dp

        return s[start:start+max_len]
