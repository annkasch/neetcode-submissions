# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        same_subtree = self.p_q_same_subtree(root, p,q)
        if same_subtree==0:
            return root
        elif same_subtree==1:
            return self.lowestCommonAncestor(root.left,p,q)
        elif same_subtree == 2:
            return self.lowestCommonAncestor(root.right,p,q)
        


    def p_q_same_subtree(self,root,p,q):

        if (p.val <= root.val and q.val >= root.val) or (p.val >= root.val and q.val<= root.val):
            return 0
        elif p.val < root.val and q.val < root.val:
            return 1
        elif p.val > root.val and q.val > root.val:
            return 2