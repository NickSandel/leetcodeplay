# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from math import ceil
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        # Find the middle node
        middle = ceil(length // 2) + 1
        current = head
        pos = 0
        while current:
            pos += 1
            if pos == middle:
                return current
            current = current.next


test = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
solution = print(Solution().middleNode(test))