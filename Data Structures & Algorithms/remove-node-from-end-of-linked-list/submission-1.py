# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #edge case empty list
        if head == None:
            return head

        #edge case 1 node 
        if head.next == None:
            return None

        list_length = 0
        curr = head
        while curr:
            curr = curr.next
            list_length += 1

        dist = list_length - n
        curr = head
        prev = None
        for i in range(dist):
            prev = curr
            curr = curr.next

        #edge case removing head
        if dist == 0:
            return curr.next
        else:
            #now remove the node
            temp = curr.next
            curr.next = None
            prev.next = temp

        return head