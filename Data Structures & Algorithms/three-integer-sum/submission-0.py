from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        my_set = set()
        my_dict = defaultdict(int)

        for i, num in enumerate(nums):
            my_dict[0-num] = [num, i]

        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(len(nums)):
                num2 = nums[j]
                if num1+num2 in my_dict:
                    if i != j and i != my_dict[num1+num2][1] and j != my_dict[num1+num2][1]:
                        my_list = []
                        num3 = my_dict[num1+num2][0]
                        if num1 <= num2 and num1 <= num3:
                            if num2 <= num3:
                                my_list.append(num1)
                                my_list.append(num2)
                                my_list.append(num3)
                            else:
                                my_list.append(num1)
                                my_list.append(num3)
                                my_list.append(num2)
                        elif num2 <= num1 and num2 <= num3:
                            if num1 <= num3:
                                my_list.append(num2)
                                my_list.append(num1)
                                my_list.append(num3)
                            else:
                                my_list.append(num2)
                                my_list.append(num3)
                                my_list.append(num1)
                        elif num3 <= num1 and num3 <= num2:
                            if num1 <= num2:
                                my_list.append(num3)
                                my_list.append(num1)
                                my_list.append(num2)
                            else:
                                my_list.append(num3)
                                my_list.append(num2)
                                my_list.append(num1)
                        my_set.add(tuple(my_list))

        temp_list = list(my_set)
        output_list = []
        for t in temp_list:
            output_list.append(list(t))

        return output_list