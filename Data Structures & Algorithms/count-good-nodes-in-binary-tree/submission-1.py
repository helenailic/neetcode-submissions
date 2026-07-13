# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        number = 0
        
        def goodNodesHelper(root: Optional[TreeNode], maxAtp: int) -> None:
            nonlocal number
            if (not root):
                return None
            
            if (root.val >= maxAtp):
                number = number + 1
                goodNodesHelper(root.right, root.val)
                goodNodesHelper(root.left, root.val)
            else:
                goodNodesHelper(root.right, maxAtp)
                goodNodesHelper(root.left, maxAtp)    

        goodNodesHelper(root, root.val)
        return number