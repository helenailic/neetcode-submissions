class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def searchHelper(nums, l, r, target):
            mid = (r-l)//2 + l
            if l > r:
                return -1
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if (nums[l] <= target <= nums[mid]):
                    return searchHelper(nums, l, mid-1, target)
                else:
                    return searchHelper(nums, mid+1, r, target)
            else:
                if (nums[mid] <= target <= nums[r]):
                    return searchHelper(nums, mid+1, r, target)
                else:
                    return searchHelper(nums, l, mid-1, target)
        return searchHelper(nums, 0, len(nums)-1, target)