"""
Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q are descendants. The ancestor is allowed to be a descendant of itself.
"""

"""
Example 1:
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

Output: 5
"""

"""
Example 2:
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

Output: 3
"""
"""
Whiteboard:
We use an iterative approach here.
if p and q values are less than root value than the LCA will be in the left subtree and vice versa
Other wise the LCA will be root
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
            