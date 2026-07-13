class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        list_of_dicts = []
        for s in strs:
            my_dict = {}
            for c in s:
                if c in my_dict:
                    my_dict[c] += 1
                else:
                    my_dict[c] = 1
                
            if my_dict in list_of_dicts:
                for my_list in output:
                    other_dict = {}
                    for c in my_list[0]:
                        if c in other_dict:
                            other_dict[c] += 1
                        else:
                            other_dict[c] = 1
                    if my_dict == other_dict:
                        my_list.append(s)
            else:
                list_of_dicts.append(my_dict)
                output.append([s])

        return output


        