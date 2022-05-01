class Solution:
    def appealSum(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        
        indexMap = {}
        for i, c in enumerate(s):
            dp[i + 1] = dp[i] + (i - indexMap.get(c, -1))
            indexMap[c] = i

        return sum(dp)


if __name__ == "__main__":
    solution = Solution()
    print(solution.appealSum("abbca"))
    print(solution.appealSum("code"))
