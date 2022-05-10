class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""

        for i in range(len(num) - 3 + 1):
            if len(set(num[i:i + 3])) == 1 and num[i:i + 3] > result:
                result = num[i:i + 3]

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestGoodInteger("6777133339"))
    print(solution.largestGoodInteger("2300019"))
    print(solution.largestGoodInteger("42352338"))
    print(solution.largestGoodInteger("222"))
