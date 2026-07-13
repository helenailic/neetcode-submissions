class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set() #if in set, you're donezo
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)