class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        output = []
                
        def backtrack(countopening, countclosing):
            if (countopening == n and countclosing == n):
                output.append("".join(stack))
                return
            
            if countopening < n:
                stack.append('(')
                backtrack(countopening+1,countclosing)
                stack.pop()

            if countclosing < n and countclosing < countopening:
                stack.append(')')
                backtrack(countopening,countclosing+1)
                stack.pop()

        backtrack(0,0)

        return output