class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._prefix = self._build_prefix(matrix)

    
    def _build_prefix(self,
        matrix: List[List[int]]
    ) -> List[List[int]]:

        rows = len(matrix)
        cols = len(matrix[0])

        prefix = [
            [0] * (cols + 1)
            for _ in range(rows + 1)
        ]

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                prefix[row][col] = (
                    prefix[row - 1][col]
                    + prefix[row][col - 1]
                    - prefix[row - 1][col - 1]
                    + matrix[row - 1][col - 1]
                )

        return prefix

    def sumRegion(
        self,
        row1: int,
        col1: int,
        row2: int,
        col2: int
    ) -> int:

        return (
            self._prefix[row2 + 1][col2 + 1]
            - self._prefix[row1][col2 + 1]
            - self._prefix[row2 + 1][col1]
            + self._prefix[row1][col1]
        )
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)