class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #O(nlogn)
        #O(n^2)
        res = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                if nums[l] + nums[r] > target:
                    r -= 1
                if nums[l] + nums[r] < target:
                    l += 1

        return [list(t) for t in res]
                