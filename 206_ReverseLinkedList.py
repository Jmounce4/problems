# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head is None:
            return head

        
        current = head
        

        def helperFunction(current):
            if current.next:
                reversedHead = helperFunction(current.next)
                current.next.next = current
                current.next = None
                return reversedHead
            else:
                reversedHead = current
                return reversedHead


        return helperFunction(head)
