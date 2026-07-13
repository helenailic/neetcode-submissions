class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stack = []

        for i, c in enumerate(s):
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif i != 0:
                if len(stack) == 0:
                    return False
                elif c == ')' and (stack[len(stack)-1] != '('):
                    return False
                elif c == ']' and (stack[len(stack)-1] != '['):
                    return False
                elif c == '}' and (stack[len(stack)-1] != '{'):
                    return False
                else:
                    stack.pop()
            else:
                return False
        
        if (len(stack) == 0):
            return True
        else:
            return False
        