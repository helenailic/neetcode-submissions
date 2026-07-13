class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        index = int(len(nums)/2)
        median = nums[index]

        if target == median:
            return index
        elif target > median:
            found_index = self.search(nums[index+1:len(nums)], target)
            if found_index == -1:
                return -1
            return index + 1 + found_index
        elif target < median:
            found_index = self.search(nums[0:index], target)
            if found_index == -1:
                return -1
            return found_index
