# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def find_min(root):
    cur = root
    while cur and cur.left:
        cur = cur.left
    return cur

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root == None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key == root.val:
            if root.right:
                tmp = root.left
                root = root.right
                min = find_min(root)
                min.left = tmp
            elif root.left:
                root = root.left
            else:
                root = None
        
        
        return root
            

        