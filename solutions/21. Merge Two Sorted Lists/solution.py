from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        head = ListNode()
        current = head
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.val = list1.val
                list1 = list1.next
            else:
                current.val = list2.val
                list2 = list2.next
            if list1 is not None or list2 is not None:
                new = ListNode()
                current.next = new
                current = current.next
        while list1 is not None:
            current.val = list1.val
            list1 = list1.next
            if list1 is not None:
                new = ListNode()
                current.next = new
                current = current.next
        while list2 is not None:
            current.val = list2.val
            list2 = list2.next
            if list2 is not None:
                new = ListNode()
                current.next = new
                current = current.next
        return head
