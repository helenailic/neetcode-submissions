from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #1 3 4 6 9
        #dict: (other num needed): index of og guy 

        my_dict = defaultdict(int)
        for i, num in enumerate(nums):
            if num in my_dict and my_dict[num] != i:
                return [min(my_dict[num], i), max(my_dict[num], i)]
            else:
                my_dict[target-num] = i
