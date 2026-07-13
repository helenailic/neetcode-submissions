class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #number, frequency
        my_dict = {}

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        #organize now by ... frequency : list of nums
        dict2 = {}
        for key in my_dict:
            value = my_dict[key]
            if value in dict2:
                dict2[value].append(key)
            else:
                dict2[value] = [key]

        #sort by keys in descending order 
        sorted_by_keys = dict(sorted(dict2.items(), reverse=True))
        top_k = []
        for key in sorted_by_keys:
            for num in sorted_by_keys[key]:
                if (len(top_k) < k):
                    top_k.append(num)
                else:
                    break

        return top_k
            


