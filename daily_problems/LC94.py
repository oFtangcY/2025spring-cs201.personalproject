#https://leetcode.cn/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder_traversal(tree_node):
            output = []
            if tree_node:
                output.extend(inorder_traversal(tree_node.left))
                output.append(tree_node.val)
                output.extend(inorder_traversal(tree_node.right))

            return output

        return inorder_traversal(root)
