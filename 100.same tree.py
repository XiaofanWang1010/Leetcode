# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:   # p and q are both None
            return True
        if p == None or p == None:    # one of p and q is None
            return False
        if p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left):
            return True 
        else:
            return False

# time complexity: O(N), N is a number of nodes in the tree, since one visits each node exactly once.
# space complexity: O(log(N)), completely balanced tree. O(N), completely unbalanced tree. 
