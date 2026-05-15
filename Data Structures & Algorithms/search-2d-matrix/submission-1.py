class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])-1
        for i in range(m):
            if (i < m-1 and target >= matrix[i+1][0]):
                continue

            L = 0
            R = n
            while L <= R:
                Mid = (R + L)//2
                if matrix[i][Mid] < target:
                    L = Mid + 1
                elif matrix[i][Mid] == target:
                    return True
                else:
                    R = Mid - 1
        
        return False