# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if self.hasPath(root, sum, 0):
            return True
        return False
    
    def hasPath(self, root, sum, total):
        if not root:
            return 
        if not root.left and not root.right:
            total += root.val
            print(sum,total )
            if sum == total:
                self.result = True
                return 
        self.hasPath(root.left, sum, total + root.val)
        self.hasPath(root.right, sum, total + root.val)