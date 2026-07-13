class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(target, nums, i):
            l = i+1
            r = len(nums)-1
            res = []
            while l < r:
                if nums[l] + nums[r] == target and l != i and r != i:
                    res.append((l,r))
                if nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

            if len(res) == 0:
                return None
            else:
                return res 

        #if at nums[i], nums[i] is target and find 2 indices that fulfill that
        nums.sort() #O(nlogn)
        res = []
        visited = []
        
        for i in range(len(nums)):
            target = -1 * nums[i]
            twoSumRes = twoSum(target, nums, i)
            if twoSumRes != None:
                for val in twoSumRes:
                    if {nums[i], nums[val[0]], nums[val[1]]} not in visited:
                        visited.append({nums[i], nums[val[0]], nums[val[1]]})
                        res.append([nums[i], nums[val[0]], nums[val[1]]])

        return res
