from typing import Optional


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = None

    def insert_begininng(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def __repr__(self) -> None:
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.value))
            current = current.next
        return " -> ".join(nodes) + " -> None"


sll = SinglyLinkedList()

sll.insert_begininng(7)
sll.insert_begininng(6)
sll.insert_begininng(5)
sll.insert_begininng(4)
sll.insert_begininng(3)
sll.insert_begininng(2)
sll.insert_begininng(1)

print("---------- Linked List -----------")
print(sll)
print("----------------------------------\n")

"""
Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.
"""


def return_middle_node(head: Node) -> int:
    if head is None:
        return None

    curr = head
    slow = fast = curr
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    print(head.value)

    return slow.value


# print(return_middle_node(sll.head))

"""
# 141. Easy
# https://leetcode.com/problems/linked-list-cycle/description/
"""


class Solution:
    def hasCycle(self, head: Optional[Node]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


"""
Given the head of a linked list and an integer k, return the the kth node from the end.
"""


def return_kth_from_end(head: Node, k: int) -> int:
    if head is None:
        return None

    slow = fast = head

    for i in range(k):
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow.value


# print(return_kth_from_end(sll.head, 2))
