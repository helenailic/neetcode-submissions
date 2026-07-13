# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def goodNodesHelper(root: TreeNode, currMax: int) -> int:
            if root == None:
                return 0
            elif root.val >= currMax:
                currMax = root.val
                return 1 + goodNodesHelper(root.left, currMax) + goodNodesHelper(root.right, currMax)
            else:
                return goodNodesHelper(root.left, currMax) + goodNodesHelper(root.right, currMax)
        

        return goodNodesHelper(root, float("-inf"))