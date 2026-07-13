class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        output = [0] * len(nums)

        for i, num in enumerate(nums):
            if i == 0:
                prefix[0] = num
                suffix[len(nums)-1] = nums[len(nums)-1]
            else:
                prefix[i] = prefix[i-1] * num
                suffix[len(nums)-1-i] = suffix[len(nums)-i] * nums[len(nums)-1-i]

        for i, num in enumerate(prefix):
            if i == 0:
                output[i] = suffix[i+1]
            elif i == len(prefix)-1:
                output[i] = prefix[i-1]
            else:
                output[i] = prefix[i-1] * suffix[i+1]

        return output