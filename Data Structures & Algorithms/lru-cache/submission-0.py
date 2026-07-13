class LRUCache:

    class ListNode:
        def __init__(self, key=0, val=0, prev=None, next=None):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.my_dict = {}  # key: node address

        # dummy head and tail
        self.head = self.ListNode()
        self.tail = self.ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.my_dict:
            addr = self.my_dict[key]

            # remove from current position
            addr.prev.next = addr.next
            addr.next.prev = addr.prev

            # move to tail (MRU)
            addr.prev = self.tail.prev
            addr.next = self.tail
            self.tail.prev.next = addr
            self.tail.prev = addr

            return addr.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.my_dict:
            addr = self.my_dict[key]
            addr.val = value

            # move to tail
            addr.prev.next = addr.next
            addr.next.prev = addr.prev
            addr.prev = self.tail.prev
            addr.next = self.tail
            self.tail.prev.next = addr
            self.tail.prev = addr

        else:
            if self.size == self.capacity:
                # remove LRU node (head.next)
                lru = self.head.next
                self.head.next = lru.next
                lru.next.prev = self.head
                del self.my_dict[lru.key]
                self.size -= 1

            # add new node at tail
            new_node = self.ListNode(key, value)
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            self.tail.prev.next = new_node
            self.tail.prev = new_node

            self.my_dict[key] = new_node
            self.size += 1
