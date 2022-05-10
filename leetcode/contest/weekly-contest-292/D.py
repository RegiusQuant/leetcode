from functools import cache
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(x: int, y: int, c: int) -> bool:
            if x >= m or y >= n:
                return False

            c += 1 if grid[x][y] == '(' else -1
            if c < 0:
                return False

            if x == m - 1 and y == n - 1:
                return c == 0
            return dfs(x + 1, y, c) or dfs(x, y + 1, c)

        return dfs(0, 0, 0)


if __name__ == "__main__":
    solution = Solution()
    print(solution.hasValidPath([["(", "(", "("], [")", "(", ")"],
                                 ["(", "(", ")"], ["(", "(", ")"]]))
    print(solution.hasValidPath([[")", ")"], ["(", "("]]))
