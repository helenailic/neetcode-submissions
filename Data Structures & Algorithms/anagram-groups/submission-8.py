class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group all anagrams tgt into sublists 
        res = {}

        for s in strs:
            curr = [0]*26
            for c in s:
                idx = ord(c) - ord('a') #turn into index 
                if curr[idx] != 0:
                    curr[idx] += 1
                else:
                    curr[idx] = 1

            if tuple(curr) in res.keys():
                res[tuple(curr)].append(s)
            else:
                res[tuple(curr)] = []
                res[tuple(curr)].append(s)

        #if anagram...
        #same length, dict for each 
        #key one we compare it to
        #dict is unordered so it can be a key

        #CAN'T DO DICT AS KEY NEED TO DO HASHABLE REPRESENTATION

        return list(res.values())