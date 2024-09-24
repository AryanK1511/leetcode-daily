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
# sll.add_to_start(5)
sll.add_to_start(3)
sll.add_to_start(2)
sll.add_to_start(2)
sll.add_to_start(4)
print("Original List:")
sll.print_list()  # Output: [1, 2, 3, 4, 5]

"""
# Practicing how to reverse a linked list
"""


def reverse_linked_list(head: Node) -> Node:
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


# sll.print_list(reverse_linked_list(sll.head))

"""
# 92. Medium
# https://leetcode.com/problems/reverse-linked-list-ii/description/
"""


def func1(head: Node, left: int, right: int) -> Node:
    if not head.next or left == right:
        return head

    curr = head
    prev = None
    dummy = Node(0)

    for _ in range(left - 1):
        prev = curr
        curr = curr.next

    dummy.next = curr
    prev_node = dummy

    for _ in range(right - left + 1):
        next_node = curr.next
        curr.next = prev_node
        prev_node = curr
        curr = next_node

    dummy.next.next = curr

    if prev:
        prev.next = prev_node
    else:
        head = prev_node

    return head


# sll.print_list(func1(sll.head, 2, 4))

"""
# 2130. Medium
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
"""


def func2(head: Node) -> int:
    if not head.next.next:
        return head.value + head.next.value

    slow_ptr, fast_ptr = head, head.next.next
    while fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    prev = None
    slow_ptr = slow_ptr.next
    while slow_ptr:
        next_node = slow_ptr.next
        slow_ptr.next = prev
        prev = slow_ptr
        slow_ptr = next_node

    first_ptr, second_ptr = head, prev

    max_sum = 0
    while second_ptr:
        max_sum = max(max_sum, first_ptr.value + second_ptr.value)
        first_ptr = first_ptr.next
        second_ptr = second_ptr.next

    return max_sum


# print(func2(sll.head))
