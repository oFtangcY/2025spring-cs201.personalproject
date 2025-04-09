#https://leetcode.cn/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        current_lap = []
        next_lap = [root]
        output = []
        while next_lap:
            current_lap = next_lap[:]
            next_lap = []
            out_lap = []
            for node in current_lap:
                if node:
                    out_lap.append(node.val)
                    if node.left:
                        next_lap.append(node.left)
                    if node.right:
                        next_lap.append(node.right)
            
            if out_lap:
                output.append(out_lap)

        return output