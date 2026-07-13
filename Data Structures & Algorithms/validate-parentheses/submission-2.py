class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) < 2:
            return False
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif len(stack) != 0 and stack[len(stack)-1] == '(' and c == ')':
                stack.pop()
            elif len(stack) != 0 and stack[len(stack)-1] == '{' and c == '}':
                stack.pop()
            elif len(stack) != 0 and stack[len(stack)-1] == '[' and c == ']':
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False