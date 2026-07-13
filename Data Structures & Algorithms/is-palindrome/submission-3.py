class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '').lower()
        s = s.replace('?','').replace(":",'').replace("'",'').replace('!','').replace('.','').replace(',','')
        print(s)

        front_index = 0
        back_index = len(s)-1
        
        while front_index < back_index:
            if s[front_index] != s[back_index]:
                return False
            front_index += 1
            back_index -= 1
        
        return True