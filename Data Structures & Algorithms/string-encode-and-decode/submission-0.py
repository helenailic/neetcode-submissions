class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode naive is by some delimiter
        #encode better is the lengthdelimeterstringlengthdelimiterstring
        big_string = ""
        for s in strs:
            length = len(s)
            big_string += str(length)
            big_string += '#'
            big_string += s

        return big_string 

    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        start = 0
        end = s.find('#')
        while i < len(s):
            length = s[start:end] #don't include delimiter
            word = s[end+1:end+1+int(length)]
            i = end + 1 + int(length)
            strs.append(word)

            start = i
            end = s.find('#',i) #from current index next delimiter

        return strs
