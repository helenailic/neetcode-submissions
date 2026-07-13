class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #store number and number of times its been seen
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
                if my_dict[num] > 1:
                    return True
            else: #else not in the dict yet
                my_dict[num] = 1
        
        return False

        #seen = set()
        #for num in nums:
            #if num in seen:
                #return True
            #seen.add(num)
        #return False

            
         