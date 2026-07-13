# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> Optional[int]:
        kth = 1
        #iterate from left to right
        
        def kthSmallestHelper(root, k) -> int:
            nonlocal kth

            if (not root):
                return None

            if (root.left):
                val = kthSmallestHelper(root.left, k)
                if (val != None):
                    return val

            if kth == k:
                return root.val
                
            kth += 1
            val = kthSmallestHelper(root.right, k)
            if val != None:
                return val
            return None

        return kthSmallestHelper(root, k)