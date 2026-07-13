from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for num in nums:
            if num in d:
                return True
            d[num] += 1
            
        return False