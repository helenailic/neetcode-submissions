class Solution:

    def encode(self, strs: List[str]) -> str:
        my_string = ""
        for s in strs:
            my_string += str(len(s))
            my_string += "#"
            my_string += s

        return my_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []

        i = 0
        while i < len(s):
            num_end_idx = s.find('#',i)
            word_length = int(s[i:num_end_idx])
            i = num_end_idx+1
            end_of_word_idx = i + word_length
            decoded_list.append(s[i:end_of_word_idx])
            i = end_of_word_idx


        return decoded_list
