class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        
        for num in my_dict:
            my_dict[num] -= 1

        for num in nums:
            if my_dict[num] != 0:
                return True
        
        return False
         