# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        first = l1
        second = l2
        sortedList = ListNode(0)
        sortedListNode = sortedList
        while first != None or second != None : 
            if(first == None) :
                sortedListNode.next = second
                second = second.next
                sortedListNode = sortedListNode.next
            elif(second == None) :
                sortedListNode.next = first
                first = first.next 
                sortedListNode = sortedListNode.next
            elif (first.val <= second.val) :
                sortedListNode.next = first
                first = first.next
                sortedListNode = sortedListNode.next
            else:
                sortedListNode.next = second
                second = second.next
                sortedListNode = sortedListNode.next
        return sortedList.next
            