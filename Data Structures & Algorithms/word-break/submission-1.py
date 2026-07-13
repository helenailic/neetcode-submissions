class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #unlimited # times -- so forwards?
        #if s can be turned into spaceseparated sequence of dictionary words
        set(wordDict)
        #dp[i] true if substring s[0:i] can be segmented into words from the dictionary
        dp = [False] * (len(s)+1)
        dp[0] = True #empty string can always be done 

        for i in range(1, len(s)+1):
            print(i)
            for word in wordDict:
                #check if any word in it works
                substring = s[0:i]
                print(dp[i-(len(word)-1)])
                print(s[i-(len(word)-1):i+1])
                if i-(len(word)-1) >= 0 and dp[i-(len(word))] and s[i-len(word):i] == word:
                    print(word)
                    dp[i] = True 

        return dp[len(s)]
            