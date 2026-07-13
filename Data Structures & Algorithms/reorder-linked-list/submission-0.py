# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #now slow at middle of list
        #reverse back end of list
        first = None
        second = slow.next
        slow.next = None #CUT THIS OFF BEFORE THE SECOND HALF REVERSAL!!!
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp

        #reorder
        curr = head
        curr2 = first
        while curr and curr2:
            temp = curr.next
            curr.next = curr2
            temp2 = curr2.next
            curr2.next = temp 
            curr = temp
            curr2 = temp2
