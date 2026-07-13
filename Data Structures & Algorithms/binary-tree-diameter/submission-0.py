# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #longest on the left + longest to the right

        bestDiam = 0
        def diameterHelper(root: Optional[TreeNode]) -> int:
            nonlocal bestDiam
            if (root == None):
                return 0

            leftHeight = diameterHelper(root.left)
            rightHeight = diameterHelper(root.right)
            if (leftHeight + rightHeight > bestDiam):
                bestDiam = leftHeight+rightHeight

            return max(leftHeight, rightHeight) + 1

        if (root == None):
            return 0

        diameterHelper(root)
        return bestDiam
        