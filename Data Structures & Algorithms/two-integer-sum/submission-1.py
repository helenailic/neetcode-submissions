class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        
        for i, num in enumerate(nums):
            if num in my_dict:
                my_list = []
                if i < my_dict[num]:
                    my_list.append(i)
                    my_list.append(my_dict[num])
                    return my_list
                else:
                    my_list.append(my_dict[num])
                    my_list.append(i)
                    return my_list
            else:
                needed = target - num;
                my_dict[needed] = i;

        return []