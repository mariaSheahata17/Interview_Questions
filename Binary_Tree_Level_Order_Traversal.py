# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1. using BFS will travers each row, top down, and store each row in a list
2. append node children into a queue, then append  the node and the level
3. iterative approach
4. after traversing , we will return the inverted the list of rows
'''
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        queue.append((root, 0))
        rows = []
        row = []
        prevLevel = 0
        while queue:
            node, level = queue.popleft()
            if level > prevLevel:
                prevLevel = level
                values = []
                for i in row:
                    n = i[0]
                    values.append(n.val)
                rows.append(values)
                row.clear()
            row.append((node, level))
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        values = []
        for i in row:
            n = i[0]
            values.append(n.val)
        rows.append(values)
        return rows[::-1]
            