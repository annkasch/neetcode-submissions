# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0
        def max_dia_rec(root):
            nonlocal res
            if root == None:
                return 0
            
            left = max_dia_rec(root.left)
            right = max_dia_rec(root.right)
            res = max(res, left + right)
            
            return max(left+1,right+1)


        max_dia_rec(root)
        return res
        