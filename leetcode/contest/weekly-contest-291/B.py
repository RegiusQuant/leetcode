from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        result = float("inf")

        indexMap = {}
        for i, x in enumerate(cards):
            if x in indexMap:
                result = min(result, i - indexMap[x] + 1)
            indexMap[x] = i

        return result if result != float("inf") else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumCardPickup([3, 4, 2, 3, 4, 7]))
    print(solution.minimumCardPickup([1, 0, 5, 3]))
