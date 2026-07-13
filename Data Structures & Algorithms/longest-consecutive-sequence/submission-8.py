class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #need to know the start 
        #"does the next number exist"
        #how do i know if a number is the start of a sequence...
        #if x-1 is not in the array 
        numset = set(nums) #so that you can do 0(1) check
        maxseq = 0
        currseq = 0
        for num in nums:
            if num-1 not in numset:
                #it's start of sequence 
                currseq = 1
                currnum = num
                while currnum+1 in numset:
                    currseq += 1
                    currnum+=1
                maxseq = max(maxseq, currseq)

        return maxseq
