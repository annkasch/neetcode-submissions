# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max_depth_rec(root):
            if root == None:
                return 0

            left_depth = max_depth_rec(root.left) + 1
            right_depth = max_depth_rec(root.right) + 1

            return max(left_depth, right_depth)
        
        
        return max_depth_rec(root)

        