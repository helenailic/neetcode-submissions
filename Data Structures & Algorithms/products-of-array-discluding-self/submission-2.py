class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #with numbers, division has problems with zeros
        prefixes = [0] * len(nums)
        suffixes = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefixes[i] = 1
            elif i == 1:
                prefixes[i] = nums[i-1]
            else:
                prefixes[i] = prefixes[i-1] * nums[i-1]

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffixes[i] = 1
            elif i == len(nums)-2:
                suffixes[i] = nums[i+1]
            else:
                suffixes[i] = suffixes[i+1] * nums[i+1]

        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = prefixes[i] * suffixes[i]

        return output

        