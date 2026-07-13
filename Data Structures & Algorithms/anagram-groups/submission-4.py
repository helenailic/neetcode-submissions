from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for s in strs:
            char_count = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                char_count[idx] += 1

            my_dict[tuple(char_count)].append(s)

        return list(my_dict.values())
            