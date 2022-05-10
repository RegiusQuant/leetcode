class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        dp = [0] * (len(pressedKeys) + 1) 

        dp[0] = 1
        for i in range(1, len(pressedKeys) + 1):
            maxSearchLength = 4 if pressedKeys[i - 1] in ('7', '9') else 3

            for j in range(1, maxSearchLength + 1):
                if i - j < 0 or pressedKeys[i - j] != pressedKeys[i - 1]:
                    break
                dp[i] = (dp[i] + dp[i - j]) % int(1e9 + 7)

        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.countTexts("22233"))
    print(solution.countTexts("222222222222222222222222222222222222"))
