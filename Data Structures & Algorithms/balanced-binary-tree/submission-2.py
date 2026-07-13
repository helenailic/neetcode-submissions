# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #keep track of height of left, height of right true or false
        def isBalancedHelper(root: Optional[TreeNode]) -> int:
            nonlocal isBalanced
            if (root == None):
                return 0

            leftHeight = isBalancedHelper(root.left)
            rightHeight = isBalancedHelper(root.right)
            if (abs(leftHeight - rightHeight) > 1):
                isBalanced = False 
            return max(leftHeight, rightHeight) + 1

        isBalanced = True
        isBalancedHelper(root)
        return isBalanced 
