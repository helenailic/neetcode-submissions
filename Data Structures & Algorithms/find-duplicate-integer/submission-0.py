from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_dict = defaultdict(int) #num: amount of times 
        for num in nums:
            if num in my_dict:
                return num
            else:
                my_dict[num] = 1