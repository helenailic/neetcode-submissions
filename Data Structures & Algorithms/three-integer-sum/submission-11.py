class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sets = set()
        for i in range(len(nums)):
            target = -1 * nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    sets.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l]+nums[r] < target:
                    l += 1
                elif nums[l]+nums[r] > target:
                    r -= 1

        print(sets)
        res = []
        for s in sets:
            res.append(list(s))

        return list(sets)

