class Solution:
    def findMin(self, nums: List[int]) -> int:
        minval = nums[0]

        def findMinHelper(nums, l, r):
            nonlocal minval
            #if fully sorted, return leftmost
            if (nums[l] <= nums[r]):
                minval = min(minval, nums[l])
                return
            
            mid = (r-l)//2+l
            minval = min(minval, nums[mid])

            if (nums[l] <= nums[mid]):
                findMinHelper(nums, mid+1, r)
            else:
                findMinHelper(nums, l, mid-1)
        
        
        findMinHelper(nums, 0, len(nums)-1)
        return minval
            
