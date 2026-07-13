class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = set()
        sums.add(0)
        for num in nums:
            new_sums = set()
            for s in sums:
                new_sums.add(s + num)
            sums.update(new_sums)

        total = sum(nums)
        if total % 2 == 0 and total//2 in sums:
            return True
        return False

        
