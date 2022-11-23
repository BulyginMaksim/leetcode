import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx in range(len(lists)):
            if lists[idx] is not None:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        if not heap:
            return None
        head = ListNode()
        current_node = head
        while heap:
            value, idx = heapq.heappop(heap)
            current_node.val = value
            if lists[idx] is not None:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
            if len(heap):
                next_node = ListNode()
                current_node.next = next_node
                current_node = next_node
        return head
