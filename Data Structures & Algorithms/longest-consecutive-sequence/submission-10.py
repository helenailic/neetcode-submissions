class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      if len(nums) == 0:
        return 0

      my_set = set()
      for num in nums:
        my_set.add(num)

      starts = []
      for num in my_set:
        if (num-1) not in my_set:
            #you are the first of a sequence
            starts.append(num)

      max_length = 1
      for start in starts:
            curr = start
            length = 1
            while (curr+1) in my_set:
                curr += 1
                length += 1
            max_length = max(length, max_length)


      return max_length

