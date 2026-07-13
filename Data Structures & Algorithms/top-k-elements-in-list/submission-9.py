class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #k most frequent elements in array 
        d = {} #elem: frequency
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        #BUCKETSORT
        b = [(0, []) for _ in range(len(nums)+1)] #0000000
        for key in d.keys():
            b[d[key]][1].append(key)
        
        res = []
        for p in range(len(b)-1, -1, -1):
            for j in range(0, len(b[p][1])):
                res.append(b[p][1][j])
                if len(res) == k:
                    return res

        return res