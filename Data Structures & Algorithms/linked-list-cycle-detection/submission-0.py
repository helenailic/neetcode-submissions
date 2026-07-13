# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_dict = {} #ListNode : #
        curr = head
        while curr.next != None:
            my_dict[curr] = 1
            if curr.next in my_dict:
                return True
            curr = curr.next
        
        return False