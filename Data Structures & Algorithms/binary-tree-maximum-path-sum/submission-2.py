# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=[-float('inf')]
        def f(node,maxi):
            if node is None:
                return 0
            leftsum=max(0,f(node.left,maxi))
            rightsum=max(0,f(node.right,maxi))
            maxi[0]=max(maxi[0],node.val+leftsum+rightsum)
            return node.val+max(leftsum,rightsum)
            
        f(root,maxi)
        return maxi[0]
