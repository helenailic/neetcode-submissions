from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_list = [[] for i in range(len(nums) + 1)]
        my_dict = defaultdict(int) #num: frequency 

        for num in nums:
            my_dict[num] += 1

        for key, value in my_dict.items():
            my_list[value].append(key)

        #now go through the list from reverse
        output = []
        count = 0
        for i in range(len(my_list)-1,0,-1):
            for j in range (len(my_list[i])):
                if count < k:
                    output.append(my_list[i][j])
                    count += 1
                else:
                    break

        return output


