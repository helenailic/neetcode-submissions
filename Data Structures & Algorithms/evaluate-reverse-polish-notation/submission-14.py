class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        ops = {'+','-','*','/'}

        for c in tokens:
            if c not in ops:
                s.append(c)
            else:
                second = int(s.pop(-1))
                first = int(s.pop(-1))
                if c == '+':
                    s.append(first+second)
                elif c == '-':
                    s.append(first-second)
                elif c == '*':
                    s.append(first*second)
                elif c == '/':
                    s.append(first/second)

        return int(s[-1])
                

            