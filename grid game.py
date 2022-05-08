class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top, bottom = sum(grid[0]), 0
        ans = float("inf")

        for i in range(n):
            top -= grid[0][i]
            ans = min(ans, max(top, bottom))
            bottom += grid[1][i]

        return ans
