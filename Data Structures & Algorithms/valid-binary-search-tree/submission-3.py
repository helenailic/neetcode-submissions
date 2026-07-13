# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #0 means no limit
        def isValidBSTHelper(root: Optional[TreeNode], lowerbound: Optional[int], upperbound: Optional[int]) -> bool:
            if (not root):
                return True

            if ((lowerbound != None and root.val <= lowerbound) or (upperbound != None and root.val >= upperbound)):
                return False

            return isValidBSTHelper(root.left, lowerbound, root.val) and isValidBSTHelper(root.right, root.val, upperbound)

        return isValidBSTHelper(root, None, None)