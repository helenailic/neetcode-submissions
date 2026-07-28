class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != '.':
                    if board[row][col] in rows[row]:
                        return False
                    if board[row][col] in cols[col]:
                        return False
                    
                    box_num = int((row//3)*3 + (col//3))
                    print(box_num)
                    if board[row][col] in boxes[box_num]:
                        return False

                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    boxes[box_num].add(board[row][col])

        return True
