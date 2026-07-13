class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums) #converts nums to set
        curr_length = 0
        max_length = 0

        for num in my_set:
            if num-1 not in my_set:
                #start sequence counting
                curr_num = num
                curr_length = 1
                while curr_num+1 in my_set:
                    curr_length += 1
                    curr_num += 1
                if curr_length > max_length:
                    max_length = curr_length

        return max_length
            