from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue1 = collections.deque()
        queue2 = collections.deque()
        result = [root.val]
        queue1.append(root)   
        while queue1:
            current = queue1.popleft()
            if current.right:
                queue2.append(current.right)
            if current.left:
                queue2.append(current.left)
            if not queue1:
                if queue2:                    
                    rightNode = queue2.popleft()
                    queue2.appendleft(rightNode)
                    result.append(rightNode.val)
                queue1 = queue2
                queue2 = collections.deque()
        return result
                
  