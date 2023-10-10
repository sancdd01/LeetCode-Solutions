""" 
110. Balanced Binary Tree
Given a binary tree, determine if it is 
height-balanced

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
"""


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return 0
            left_height = helper(node.left)
            if left_height == -1:
                return -1
            right_height = helper(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)

        return helper(root) != -1
