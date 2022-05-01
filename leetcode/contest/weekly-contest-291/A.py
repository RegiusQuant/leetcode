class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = 0
        for i, c in enumerate(number):
            if c == digit:
                result = max(result, int(number[:i] + number[i + 1:]))
        return str(result)


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDigit("123", "3"))
    print(solution.removeDigit("1231", "1"))
    print(solution.removeDigit("551", "5"))
