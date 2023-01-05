from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        while head is not None and head.val == val:
            head = head.next
        current_head = head
        while current_head is not None:
            next_node = current_head.next
            if current_head.next is not None and current_head.next.val == val:
                while next_node is not None and next_node.val == val:
                    next_node = next_node.next
                current_head.next = next_node
            current_head = next_node
        return head
