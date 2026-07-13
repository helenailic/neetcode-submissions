class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens: 
                if token == '*':
                    val2 = stack.pop()
                    val1 = stack.pop()
                    result = val2 * val1 
                    stack.append(result)

                elif token == '/':
                    val2 = stack.pop()
                    val1 = stack.pop()
                    result = int(val1 / val2)
                    stack.append(result)

                elif token == '+':
                    val2 = stack.pop()
                    val1 = stack.pop()
                    result = val2 + val1 
                    stack.append(result)

                elif token == '-':
                    val2 = stack.pop()
                    val1 = stack.pop()
                    result = val1 - val2 
                    stack.append(result)

                else:
                    stack.append(int(token))

        return stack[0]
        