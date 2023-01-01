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
        current_head = ListNode()
        dummy_node = current_head
        while list1 and list2:
            if list1.val < list2.val:
                current_head.next = list1
                current_head = list1
                list1 = list1.next
            else:
                current_head.next = list2
                current_head = list2
                list2 = list2.next
        if list1 or list2:
            current_head.next = list1 if list1 else list2
        return dummy_node.next
