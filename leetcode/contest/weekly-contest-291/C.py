from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        result = set()

        for i in range(len(nums)):
            count = 0
            for j in range(i, len(nums)):
                if nums[j] % p == 0:
                    count += 1
                if count > k:
                    break
                result.add(tuple(nums[i:j + 1]))

        return len(result)


if __name__ == "__main__":
    solution = Solution()
    print(solution.countDistinct([2, 3, 3, 2, 2], 2, 2))
    print(solution.countDistinct([1, 2, 3, 4], 4, 1))
