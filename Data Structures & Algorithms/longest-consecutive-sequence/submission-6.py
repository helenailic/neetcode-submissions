from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        if len(nums) == 0:
            return 0

        beginnings = []
        curr_length = 1
        max_length = 1

        for num in nums:
            #identify all ONLY beginning of sequences
            if (num+1 in nums_set) and (num-1 not in nums_set): 
                beginnings.append(num)
        
        for num in beginnings:
            curr_num = num
            while curr_num+1 in nums_set:
                curr_length += 1
                curr_num += 1
            
            if curr_length > max_length:
                max_length = curr_length
            
            curr_length = 1

        return max_length


            