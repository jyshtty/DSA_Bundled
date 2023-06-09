class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        make_row_zero = False
        make_col_zero = False
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                make_col_zero = True
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                make_row_zero = True
                

        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
            
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if make_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if make_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        
