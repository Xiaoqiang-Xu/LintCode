"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        if root is None:
            return root
        
        left = self.maxNode(root.left)
        right = self.maxNode(root.right)
        
        return self.getMax(root, self.getMax(left, right))

    def getMax(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        if left.val > right.val:
            return left
        return right
# use the idea of recursion



        
