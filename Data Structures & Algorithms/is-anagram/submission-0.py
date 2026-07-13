class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #order characters can be different
        #must have same frequency of all same characters 
        #so dictionary populate for one, depopulate for other
        #return true if all zeros at this point 

        my_dict = {}
        for c in s:
            if c in my_dict:
                my_dict[c] += 1
            else:
                my_dict[c] = 1
        
        for c in t:
            if c in my_dict:
                my_dict[c] -= 1
            else:
                return False

        for key in my_dict:
            if my_dict[key] != 0:
                return False

        return True
        