class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        
        self.total=0

        while(row1<=row2):
            self.total+=sum(self.matrix[row1][col1:col2+1])
            row1+=1
            print(self.total)

        
        return self.total
        
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)