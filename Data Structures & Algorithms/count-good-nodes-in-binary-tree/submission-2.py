# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def goodNodesHelper(self, root: TreeNode, currMax: int) -> int:
            if root == None:
                return 0
            elif root.val >= currMax:
                currMax = root.val
                return 1 + goodNodesHelper(self, root.left, currMax) + goodNodesHelper(self, root.right, currMax)
            else:
                return goodNodesHelper(self, root.left, currMax) + goodNodesHelper(self, root.right, currMax)
        

        return goodNodesHelper(self, root, float("-inf"))