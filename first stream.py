#Eaazzzzyyyy Peaaazzyyy: Palindrome generation- 1 (Without converting it to a string)
# How to know if a number is Power of 2 (perform bitwise anding b/w x and x-1)
# How to know if a number is Power of 4 (pattern: (rule for power of 2) and len(the number)%2==0)
# Rotate a n x n matrix clockwise(90 degrees, inplace)
# Given a sudoku formation, find out if its valid or not

import math
def test(board):
    seen = {}
    for row in range(0,9):
        for col in range(0,9):
            v = board[row][col]
            if v!=".":
                row_sig = "{}({})".format(row, v)
                col_sig = "({}){}".format(v, col)
                box_sig = "{}({}){}".format(row // 3, v, col // 3) 
                print("rw: " ,row_sig)
                print("cw: " ,col_sig)
                print("bw: " ,box_sig)
                
                if (row_sig in seen or col_sig in seen or box_sig in seen):
                    return False
                
                seen[row_sig] = True
                seen[col_sig] = True
                seen[box_sig] = True
    return True

if __name__=="__main__":
    print(test([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))