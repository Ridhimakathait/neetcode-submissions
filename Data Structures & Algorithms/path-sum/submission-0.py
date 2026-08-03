# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def ps(node,sum):
            if node is None:
                return False
            if (node.left is None and node.right is None):
                return node.val==sum
            sum-=node.val
            
            return ps(node.left,sum) or ps(node.right,sum)
        return ps(root,targetSum)
        