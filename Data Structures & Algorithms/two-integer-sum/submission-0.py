class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #integer target
        #return indices such that i != j and num at i + num at j = target 

        #dictionary, 
        #save num that's needed to get to target for that num and the indice (save earliest)
        my_dict = {}
        for i, num in enumerate(nums):
            if num in my_dict:
                if (i < my_dict[num]):
                    return [i, my_dict[num]]
                else:
                    return [my_dict[num], i]
            else:
                #adding protocol
                my_dict[target-num] = i
        