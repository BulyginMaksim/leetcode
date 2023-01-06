from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_head = head
        while current_head is not None:
            while current_head.next is not None and current_head.val == current_head.next.val:
                current_head.next = current_head.next.next
            current_head = current_head.next
        return head
