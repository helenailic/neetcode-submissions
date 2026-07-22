class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #1    2    3    4
        #1    1    2    6    
        #24  12    4    1

        leftToRight = [[] for _ in range(len(nums))]
        rightToLeft = [[] for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                leftToRight[i] = 1
            else:
                leftToRight[i] = nums[i-1] * leftToRight[i-1]

        for i in range(len(nums)-1, -1, -1):
            if i == (len(nums)-1):
                rightToLeft[i] = 1
            else:
                rightToLeft[i] = nums[i+1] * rightToLeft[i+1]
                
        output = []
        for i in range(len(leftToRight)):
            output.append(leftToRight[i] * rightToLeft[i])

        return output