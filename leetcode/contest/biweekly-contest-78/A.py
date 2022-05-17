class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        result = 0

        num = str(num)
        for i in range(len(num)):
            if i + k - 1 >= len(num):
                break
            if int(num[i: i + k]) == 0:
                continue
            if int(num) % int(num[i: i + k]) == 0:
                result += 1

        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.divisorSubstrings(240, 2))
    print(solution.divisorSubstrings(430043, 2))
