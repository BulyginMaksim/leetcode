from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_length = self.get_list_length(head)
        if not k or list_length <= 1 or not k % list_length:
            return head
        k %= list_length
        slow, fast = head, head

        for _ in range(k):
            fast = fast.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        new_head = slow
        slow = slow.next
        new_head.next = None
        new_head = slow

        while slow.next is not None:
            slow = slow.next
        slow.next = head
        return new_head

    def get_list_length(self, head: Optional[ListNode]):
        counter = 0
        while head is not None:
            head = head.next
            counter += 1
        return counter
