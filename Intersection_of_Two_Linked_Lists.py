# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# this solution exceeded the time limit on Leetcode because its N^2
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1 = headA
        node2 = headB
        condition = True
        try:
            while node1 != None:
                while node2 != None:
                    if (node1 == node2):
                        return node1
                    else:
                        node2 = node2.next
                node1 = node1.next
                node2 = headB
            return None
            
        except:
            return None