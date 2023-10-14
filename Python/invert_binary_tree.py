""" 
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # Swap left and right children
        root.left, root.right = root.right, root.left
        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
