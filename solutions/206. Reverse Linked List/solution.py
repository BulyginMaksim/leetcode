from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        current_head = head
        head = head.next
        current_head.next = None
        while head is not None:
            copied_tail = head
            head = head.next
            copied_tail.next = current_head
            current_head = copied_tail
        return current_head
