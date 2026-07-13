from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1

        for key, value in count.items():
            freq[value].append(key)

        output = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output




