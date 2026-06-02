# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs_search(p,q):
            if not p and not q:
                return True

            if not p and q:
                return False
            if not q and p:
                return False
            
            if q.val != p.val:
                return False
            
            left = dfs_search(p.left, q.left)
            right = dfs_search(p.right, q.right)

            return (left and right)
        

        return dfs_search(p,q)
        