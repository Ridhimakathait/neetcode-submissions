# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if node is None:
                return 0
            lefth=check(node.left)
            righth=check(node.right)
            if(lefth==-1 or righth==-1):
                return -1
            if(abs(lefth-righth)>1):
                return -1

            return max(lefth,righth)+1
        if check(root)==-1:
            return False
        return True
        