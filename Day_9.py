# https://leetcode.com/problems/magic-squares-in-grid/description/?envType=daily-question&envId=2024-08-09

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(square):
            if sorted(square) != list(range(1, 10)):
                return False
            
            row_sum1 = square[0] + square[1] + square[2]
            row_sum2 = square[3] + square[4] + square[5]
            row_sum3 = square[6] + square[7] + square[8]
            
            col_sum1 = square[0] + square[3] + square[6]
            col_sum2 = square[1] + square[4] + square[7]
            col_sum3 = square[2] + square[5] + square[8]
            
            diag_sum1 = square[0] + square[4] + square[8]
            diag_sum2 = square[2] + square[4] + square[6]
            
            return (row_sum1 == row_sum2 == row_sum3 == 
                    col_sum1 == col_sum2 == col_sum3 == 
                    diag_sum1 == diag_sum2)

        count = 0
        
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                square = [
                    grid[i][j], grid[i][j+1], grid[i][j+2],
                    grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                    grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]
                ]
                if is_magic(square):
                    count += 1
        
        return count
