from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        current_odd, current_even = head, head.next
        even_head = current_even
        while current_even is not None and current_even.next is not None:
            current_odd.next = current_even.next
            current_odd = current_odd.next
            current_even.next = current_odd.next
            current_even = current_even.next
        current_odd.next = even_head
        return head
