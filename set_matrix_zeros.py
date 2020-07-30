class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        rows , cols = len(matrix), len(matrix[0])
        convert = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    convert.add((i,j))
        for pair in convert:
            x, y = pair[0], pair[1]
            self.converCOlRowtoZero(x, y, matrix)
                    
    
    def converCOlRowtoZero(self,row, col , matrix):
        rows , cols = len(matrix), len(matrix[0])
        # convert row to zeros
        for j in range(cols):
            matrix[row][j] = 0
        # convert cols to zeros
        for i in range(rows):
            matrix[i][col] = 0
        