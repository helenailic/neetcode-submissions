# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_num = []
        second_num = []

        curr1 = l1
        while curr1:
            first_num.append(str(curr1.val))
            curr1 = curr1.next

        curr2 = l2
        while curr2:
            second_num.append(str(curr2.val))
            curr2 = curr2.next

        first_num_fr = ""
        second_num_fr = ""
        for i in range(len(first_num)-1, -1, -1):
            first_num_fr += first_num[i]
        for i in range(len(second_num)-1, -1, -1):
            second_num_fr += second_num[i]

        sum_int = int(first_num_fr) + int(second_num_fr)
        sum_str = str(sum_int)
        dummy = ListNode(-1)
        curr = dummy
        for i in range(len(sum_str)-1, -1, -1):
            new_node = ListNode(int(sum_str[i]))
            curr.next = new_node
            curr = new_node

        return dummy.next
