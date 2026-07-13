class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def searchHelper(l, r, nums, target) -> int:
            if l > r: #empty search window
                return -1
            m = (r-l)//2 + l #+l maintains correct index 
            if target == nums[m]:
                return m
            if target < nums[m]:
                return searchHelper(l, m-1, nums, target)
            if target > nums[m]:
                return searchHelper(m+1, r, nums, target)

        return searchHelper(0, len(nums)-1, nums, target)