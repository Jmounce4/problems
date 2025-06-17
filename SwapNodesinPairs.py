# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if head is None:
            return head
        
        firstNode = head
        dummy = ListNode(0)
        dummy.next = head
        prevNode = dummy
        while prevNode.next and prevNode.next.next:
            firstNode = prevNode.next
            secondNode = prevNode.next.next
            prevNode.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            prevNode = firstNode



        return dummy.next
