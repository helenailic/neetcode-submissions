# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #reverse first k nodes in LL
        #reverse next k nodes
        #so on
        #singly linked list 
         #when reversing regular LL...
        def reverseLL(start: Optional[ListNode], k:int):
            first = None
            second = start
            i = 0
            while i < k and second:
                temp = second.next
                second.next = first
                first = second
                second = temp
                i += 1

            #JUST RETURN WHATS NEEDED
            return first, start, second #newHead, newTail, nextGroupStart

        def hasKNodes(node: Optional[ListNode], k:int) -> bool:
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        #on first one, prev is None, rest its the head return from before
        while hasKNodes(curr, k):
            newHead, newTail, nextGroupStart = reverseLL(curr, k)
            prev.next = newHead
            newTail.next = nextGroupStart

            #move pointers forward fro next group
            prev = newTail
            curr = nextGroupStart

        return dummy.next