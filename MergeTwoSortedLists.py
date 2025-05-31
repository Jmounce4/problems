# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        myList = ListNode()
        current = myList

        while list1 and list2:
            if list1.val <= list2.val and list1 is not None:
                current.next = list1
                list1 = list1.next
                current = current.next
            elif list2.val < list1.val and list2 is not None:
                current.next = list2
                list2 = list2.next
                current = current.next
            
        
        if list1 is None:
            current.next = list2
        else:
            current.next = list1
        return myList.next
