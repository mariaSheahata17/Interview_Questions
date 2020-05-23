# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
My solution did't pass all test cases
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node = head
        if ( node == None) :
            return False
        elif (node.next == None):
            return False
        values = []
        values.append(node.val)
        while node.next != None:
            prev = node
            node = node.next            
            if (node.val in values):
                print(values)
                return True
            else:
                values.append(node.val)

"""

class Solution:
    #The "trick" is to not check all the time whether we have reached the end but to handle it via an exception.
    def hasCycle(self, head: ListNode) -> bool:
        try:    
            slow = head
            fast = head.next     
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


