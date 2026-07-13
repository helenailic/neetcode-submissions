class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        i = 0
        while i < len(nums) - 2 and nums[i] <= 0:
            if i == 0 or nums[i] != nums[i-1]:
                front = i+1
                back = len(nums)-1
                target = -1 * nums[i]
                while front < back:
                    if nums[front] + nums[back] < target:
                        front += 1
                    elif nums[front] + nums[back] > target:
                        back -= 1
                    else:
                        my_list = []
                        my_list.append(nums[i])
                        my_list.append(nums[front])
                        my_list.append(nums[back])
                        output.append(my_list)
                        while front < back and nums[front] == nums[front + 1]: 
                            front += 1
                        while front < back and nums[back] == nums[back - 1]: 
                            back -= 1

                        front += 1
                        back -= 1
            
            i += 1

        return output