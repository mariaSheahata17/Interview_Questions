import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
1.travers the tree using BFS using a queue
2. when we get to a left node, check if its a leaf
3. add its value to the sum

'''
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int: 
        total = 0 
        if not root:
            return total
        
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
            current = queue.popleft()
            if current.left != None:
                queue.append(current.left)
                if self.isLeaf(current.left):
                    total = total + current.left.val                
            if current.right != None:
                queue.append(current.right)
        return total
    
                
    def isLeaf(self, node):
        if node == None:
            return False
        if node.left == None and node.right == None:
            return True
        return False
        