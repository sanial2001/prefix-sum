class Solution:
    def solve(self, matrix):
        m = len(matrix)
        if m == 0:
            return matrix
        n = len(matrix[0])
        if n == 0:
            return matrix
        t = [[0 for _ in range(n)] for _ in range(m)]
        t[0][0] = matrix[0][0]

        for i in range(1, m):
            t[i][0] = t[i - 1][0] + matrix[i][0]

        for i in range(1, n):
            t[0][i] = t[0][i - 1] + matrix[0][i]

        for i in range(1, m):
            for j in range(1, n):
                t[i][j] = t[i - 1][j] + t[i][j - 1] + matrix[i][j] - t[i - 1][j - 1]

        return t
