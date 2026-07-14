class Solution:

    def encode(self, strs: List[str]) -> str:
        my_string = ""

        for s in strs:
            num = len(s)
            my_string += str(num)
            my_string += '#'
            my_string += s

        print(my_string)
        return my_string

    def decode(self, s: str) -> List[str]:
        my_list = []
        
        i = 0
        while i < len(s):
            num = ""
            while s[i] != '#':
                num += str(s[i])
                i += 1

            i += 1
            print(num)

            if num == '0':
                my_list.append('')
            elif i == len(s):
                my_list.append(num)
                return my_list
            else:
                num = int(num)
                print(i)
                string = s[i:i+num]
                print(string)
                my_list.append(string)
                i = i + num
        
        return my_list
