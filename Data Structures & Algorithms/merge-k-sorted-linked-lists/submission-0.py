# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode(-1)
            tail = dummy

            #add the lower value, update tail
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    tail = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    tail = list2
                    list2 = list2.next

            #add whatever list is longer's remaining nodes 
            if list1:
                tail.next = list1
            else:
                tail.next = list2

            return dummy.next

        if len(lists) == 0:
            return None

        for i in range(1, len(lists), 1):
            head = mergeTwoLists(self, lists[i-1], lists[i])
            lists[i] = head

        return lists[-1]