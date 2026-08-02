class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['{','[','(']
        for c in s:
            if len(stack) == 0 and c not in opening:
                return False
            if c == ')':
                if stack[-1] != '(':
                    return False
                else:
                    stack.pop(-1)
            elif c == ']':
                if stack[-1] != '[':
                    return False
                else:
                    stack.pop(-1)
            elif c == '}':
                if stack[-1] != '{':
                    return False
                else:
                    stack.pop(-1)
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False
