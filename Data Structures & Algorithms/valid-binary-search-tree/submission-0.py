# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minval,maxval=-float('inf'),float('inf')
        def f(node,minval,maxval):
            if node is None:
                return True
            if node.val<=minval or node.val>=maxval:
                return False
            
            return f(node.left,minval,node.val) and           f(node.right,node.val,maxval)
        return f(root,minval,maxval)
