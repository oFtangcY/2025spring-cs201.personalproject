#https://leetcode.cn/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        elif matrix == [[]]:
            return False

        i = 0
        n = min(len(matrix), len(matrix[0]))
        while i < n:
            if matrix[i][i] == target:
                return True
            elif matrix[i][i] > target and matrix[i - 1][i - 1] < target:
                if Solution.searchMatrix(self, [matrix[j][i:] for j in range(i)], target) or Solution.searchMatrix(self, [matrix[j][:i] for j in range(i, n)], target):
                    return True
            i += 1

        if len(matrix) > n:
            return Solution.searchMatrix(self, matrix[n:], target)
        elif len(matrix[0]) > n:
            return Solution.searchMatrix(self, [matrix[j][n:] for j in range(n)], target)

        return False
