# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

            def invert(root):

                if root == None:
                    return None

                root_left = invert(root.left)
                root_right = invert(root.right)

                root.left = root_right
                root.right = root_left

                return root
                
                
            
            invert(root)

            return root
        