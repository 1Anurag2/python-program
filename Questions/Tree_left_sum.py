# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # Helper function to check if a node is a leaf
        def isLeaf(node):
            return node is not None and node.left is None and node.right is None
        
        # Main recursive function
        def sumLeftLeaves(node, isLeft):
            if node is None:
                return 0
            
            # If it's a left leaf, add its value to the sum
            if isLeaf(node) and isLeft:
                return node.val
            
            # Recursively sum left and right children
            return sumLeftLeaves(node.left, True) + sumLeftLeaves(node.right, False)
        
        # Start the recursion from the root, root is not a left child
        return sumLeftLeaves(root, False)
