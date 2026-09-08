class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        if len(nums) < 3:
            return []

        result_set = set()

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            target = -1 * nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    result_set.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        result_list = []
        for item in result_set:
            result_list.append(list(item))
        return result_list
