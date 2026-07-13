class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #array iding the freq of each char in string : list of all anagrams
        #ord('a') converts character to its ascii 
        #ord('a') is the smallest, 97, so we want to map to index ord(character) - ord('a') which will go between 0-25
        my_dict = {}

        for s in strs:
            #generate unique array
            arr = [0] * 26 
            for c in s:
                index = ord(c) - ord('a')
                arr[index] += 1

            #check if that's already in my_dict 
                #if yes, add to value list 
                #if no, generate new one
            if tuple(arr) in my_dict:
                my_dict[tuple(arr)].append(s)
            else:
                my_dict[tuple(arr)] = [s]

        #convert my_dict into list of lists
        #return the list 
        list_of_lists = []
        for key in my_dict:
            list_of_lists.append(my_dict[key])
        return list_of_lists


        
        