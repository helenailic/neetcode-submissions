class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [([0] * 9) for i in range(9)]
        cols = [([0] * 9) for i in range(9)]
        boxes = [([0] * 9) for i in range(9)]

        for i, r in enumerate(board):
            for j, c in enumerate(board[i]):
                if board[i][j] != '.':
                    #row array
                    if rows[i][int(board[i][j])-1] > 0:
                        return False
                    else:
                        rows[i][int(board[i][j])-1] += 1 

                    #col array
                    if cols[j][int(board[i][j])-1] > 0:
                        return False
                    else:
                        cols[j][int(board[i][j])-1] += 1

                    #boxes array
                    arr_i = i // 3
                    arr_j = j // 3
                    box_num = arr_i * 3 + arr_j
                    if boxes[box_num][int(board[i][j])-1] > 0:
                        return False
                    else:
                        boxes[box_num][int(board[i][j])-1] += 1

        return True

        