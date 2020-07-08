# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1. recusively calculate the depth of each node
2. keep track of the minimum depth variable
3. 
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.depth(root)
    
    def depth(self, root):
        if root == None:
            return float('inf')
        if not root.left and not root.right:
            return 1
        return 1 + min(self.depth(root.left), self.depth(root.right))
        

        