from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        _, _, result = self.traverse(root)
        return result

    def traverse(self, root: Optional[TreeNode]) -> Tuple[int, int, int]:
        if not root:
            return 0, 0, 0

        leftSum, leftCount, leftResult = self.traverse(root.left)
        rightSum, rightCount, rightResult = self.traverse(root.right)

        totalSum = leftSum + rightSum + root.val
        totalCount = leftCount + rightCount + 1
        totalResult = leftResult + rightResult
        if root.val == totalSum // totalCount:
            totalResult += 1

        return totalSum, totalCount, totalResult


if __name__ == "__main__":
    solution = Solution()
    
    root = TreeNode(1)
    print(solution.averageOfSubtree(root))
    