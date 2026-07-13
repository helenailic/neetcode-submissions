class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            #base case
            if openN == closedN == n:
                res.append("".join(stack))
                return 
            
            if openN < n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop() #remove bc of backtracking

            if closedN < openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop() #remove bc of backtracking

        backtrack(0,0)
        return res
            