# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=0
        def d(node):
            nonlocal maxi
            if node is None:
                return 0
            
            lefth=d(node.left)
            righth=d(node.right,)
            maxi=max(maxi,lefth+righth)
            return 1+max(lefth,righth)
        
        d(root)
        return maxi
        