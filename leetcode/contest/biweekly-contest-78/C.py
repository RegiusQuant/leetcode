from tkinter import Y
from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        result = 0
        tiles = sorted(tiles)

        leftIndex, currCover = 0, 0
        for leftTile, rightTile in tiles:
            currCover += rightTile - leftTile + 1
            while tiles[leftIndex][1] < rightTile - carpetLen + 1:
                currCover -= tiles[leftIndex][1] - tiles[leftIndex][0] + 1
                leftIndex += 1
            result = max(result, currCover - max(rightTile - carpetLen + 1 - tiles[leftIndex][0], 0))

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumWhiteTiles([[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]], 10))
    print(solution.maximumWhiteTiles([[10, 11], [1, 1]], 2))
