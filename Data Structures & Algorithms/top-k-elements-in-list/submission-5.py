class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_list = [0] * len(nums) 
        my_dict = {} #number : frequency

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        for key in my_dict:
            freq = my_dict[key] - 1
            if my_list[freq] == 0:
                #make list
                my_list[freq] = [key]
            else:
                my_list[freq].append(key)

        #get top k nums
        #go backwards through list indices 
        top_k = []

        curr_idx = len(my_list)-1
        gathered_items = 0
        while curr_idx >= 0 and gathered_items < k:
            if my_list[curr_idx] != 0:
                for item in my_list[curr_idx]:
                    top_k.append(item)
                    gathered_items += 1
        
            curr_idx -= 1

        return top_k
            


