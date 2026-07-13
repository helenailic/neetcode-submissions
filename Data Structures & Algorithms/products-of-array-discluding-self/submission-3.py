class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        output = []

        if 0 not in nums:
            for num in nums:
                total_product *= num
            
            for i in range(len(nums)):
                output.append(int(total_product / nums[i]))

        else:
            num_zeros = 0
            for num in nums:
                if num != 0:
                    total_product *= num
                else:
                    num_zeros += 1
            
            for i in range(len(nums)):
                if nums[i] != 0 or num_zeros > 1:
                    output.append(0)

                elif nums[i] == 0:
                    output.append(int(total_product))

        return output
