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
        result = ListNode()
        while head is not None:
            result.val = head.val
            if head.next is not None:
                new_head = ListNode()
                new_head.next = result
                result = new_head
            head = head.next
        return result
