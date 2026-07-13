class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #2 subsets where sum(subset1) = sum(subset2)
        #total sum / 2 -- can we get up to that number 
        total = sum(nums)
        if total % 2 != 0:
            return False 
        target = total // 2

        sumset = set() #set of all possible sums
        sumset.add(0)
        for i, num in enumerate(nums):
            new_sums = set()  
            for s in sumset:
                new_sums.add(s + num)
            sumset.update(new_sums)

        if target in sumset:
            return True
        else:
            return False

        #if we can get some combo up to that exact number, booyah
        #for each place in dp, what is the closest sum to the target? no!
        #what is all the sums we can get for each index 
        #is there some subset of nums that sums up to target