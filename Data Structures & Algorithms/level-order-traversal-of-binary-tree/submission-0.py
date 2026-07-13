# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def levelOrderHelper(root: Optional[TreeNode], level: int) -> None:
            if (not root):
                return None

            if len(result) == level:
                result.append([])
            result[level].append(root.val)
            
            levelOrderHelper(root.left, level+1)
            levelOrderHelper(root.right, level+1)

        levelOrderHelper(root, 0)
        
        return result