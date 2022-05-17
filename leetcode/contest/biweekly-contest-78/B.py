from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        result = 0

        totalSum, currSum = sum(nums), 0
        for i in range(len(nums) - 1):
            currSum += nums[i]
            if currSum >= totalSum - currSum:
                result += 1

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.waysToSplitArray([10, 4, -8, 7]))
    print(solution.waysToSplitArray([10, 4, -8, 7]))
