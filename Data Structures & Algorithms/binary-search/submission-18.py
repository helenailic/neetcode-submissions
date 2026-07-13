class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def search_helper(nums, target, start):
            if len(nums) == 0:  # Base case: target not found
                return -1
            idx = int(len(nums)/2)
            
            if target == nums[idx]:
                return start+idx
            elif target > nums[idx]:
                return search_helper(nums[idx+1:len(nums)], target, idx+start+1)
            elif target < nums[idx]:
                return search_helper(nums[0:idx], target, 0+start)

        return search_helper(nums, target, 0)
