class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_to_start(self, value=None):
        if value:
            new_node = Node(value)
            if not self.head:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head = new_node

    def print_list(self, node=None):
        ll = []
        curr = node if node else self.head
        while curr:
            ll.append(curr.value)
            curr = curr.next
        print(ll)


# Instantiate the linked list and add nodes
sll = SinglyLinkedList()
sll.add_to_start(5)
sll.add_to_start(4)
sll.add_to_start(3)
sll.add_to_start(2)
sll.add_to_start(1)
print("Original List:")
sll.print_list()  # Output: [1, 2, 3, 4, 5]

"""
# 24. Medium
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
"""


def func1(head: Node) -> Node:
    if not head or not head.next:
        return head

    dummy = Node(0)
    dummy.next = head
    prev, curr = dummy, head

    while curr and curr.next:
        next_pair = curr.next.next
        second = curr.next

        second.next = curr
        curr.next = next_pair
        prev.next = second

        prev = curr
        curr = next_pair

    return dummy.next


swapped_head = func1(sll.head)
sll.print_list(swapped_head)
