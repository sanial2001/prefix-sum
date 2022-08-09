class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        t = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                t[i][j] = t[i][j - 1] + t[i - 1][j] - t[i - 1][j - 1] + mat[i - 1][j - 1]

        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                start = 1
                end = min(i, j)
                while start <= end:
                    mid = (start + end) // 2
                    sums = t[i][j] - t[i - mid][j] - t[i][j - mid] + t[i - mid][j - mid]
                    if sums <= threshold:
                        ans = max(ans, mid)
                        start = mid + 1
                    else:
                        end = mid - 1

        return ans
