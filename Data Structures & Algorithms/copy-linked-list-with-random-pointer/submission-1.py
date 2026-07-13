"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        my_dict = {}

        #make all copies
        curr = head
        while curr:
            copy = Node(curr.val)
            my_dict[curr] = copy
            curr = curr.next

        #set next and random pointers 
        curr = head
        while curr:
            my_dict[curr].next = my_dict.get(curr.next)
            my_dict[curr].random = my_dict.get(curr.random)
            curr = curr.next

        return my_dict.get(head)


        

        