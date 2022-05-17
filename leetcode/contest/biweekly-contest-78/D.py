from cmath import inf
from string import ascii_lowercase


class Solution:
    def largestVariance(self, s: str) -> int:
        if len(set(s)) == 1 or len(set(s)) == len(s):
            return 0

        result = 0
        for x in set(s):
            for y in set(s):
                if x == y:
                    continue
                result = max(result, self.calculate(x, y, s))

        return result

    def calculate(self, x: str, y: str, s: str) -> int:
        result = 0

        currDiff, currDiffWithY = 0, -inf
        for c in s:
            if c == x:
                currDiff += 1
                currDiffWithY += 1
            if c == y:
                currDiff -= 1
                currDiffWithY = currDiff
                currDiff = max(0, currDiff)
            result = max(result, currDiffWithY)
        
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestVariance("aababbb"))
    print(solution.largestVariance("abcde"))
    print(solution.largestVariance("lripaa"))