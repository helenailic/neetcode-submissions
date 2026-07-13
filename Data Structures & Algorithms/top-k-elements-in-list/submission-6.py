from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(int)
        output = []

        for num in nums:
            my_dict[num] += 1
        
        sorted_topk_values = sorted(list(my_dict.values()), reverse=True)[0:k]

        for key in my_dict:
            if my_dict[key] in sorted_topk_values:
                output.append(key)

        return output




