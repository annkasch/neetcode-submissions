# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        output_list = []
        if not root:
            return []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                output_list.append(node.val)
            else:
                right = node.right
                left = node.left
                node.left = None
                node.right = None
                stack.append(node)
                if right:
                    stack.append(right)
                if left:
                    stack.append(left)

        return output_list

        
        