from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make it a set, do in operation on the set 
        #ord(ch) #ch(ord(ch))

        #set of these list thingies 
        #my_set = set()
        my_dict = defaultdict(list) #the word list thingie : list of all words with it
        for string in strs:
            my_list = [0] * 26
            for c in string:
                my_list[ord(c)-97] += 1
            my_string = str(my_list)
            print(my_string)

            my_dict[my_string].append(string)

            #my_set.add(my_list)

        my_final_list = []
        for key in my_dict:
            my_final_list.append(my_dict[key])

        return my_final_list
            
