# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:

    def serialize(self, root):
        s=[]
        q=deque()
        q.append(root)
        while q:
            node=q.popleft()
            if node is None:
                s.append('#')
            else:
                s.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ','.join(s)

    def deserialize(self, data):
        if data == '#':
            return None
        n=data.split(',')
        root=TreeNode(int(n[0]))
        q=deque([root])
        i=1
        while q:
            node=q.popleft()
            if n[i]!='#':
                node.left=TreeNode(int(n[i]))
                q.append(node.left)
            i+=1

            if n[i]!='#':
                node.right=TreeNode(int(n[i]))
                q.append(node.right)
            i+=1
        return root
