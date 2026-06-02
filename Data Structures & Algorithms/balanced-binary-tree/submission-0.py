# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = True
        def height_balance(root):
            nonlocal balanced
            if root is None:
                return 0

            left = height_balance(root.left) + 1
            right = height_balance(root.right) + 1

            if abs(left-right) > 1:
                balanced = False
                
            return max(left,right)
        
        height_balance(root)
        return balanced
                

                


            
        