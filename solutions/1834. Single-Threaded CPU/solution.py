import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        updated_tasks = sorted([(task[0], task[1], idx) for idx, task in enumerate(tasks)])
        result, heap = [], []
        idx = 0
        current_time = updated_tasks[idx][0]
        while len(result) < len(tasks):
            while idx < len(tasks) and updated_tasks[idx][0] <= current_time:
                heapq.heappush(heap, (updated_tasks[idx][1], updated_tasks[idx][2]))
                idx += 1
            if heap:
                processing_time, orginal_idx = heapq.heappop(heap)
                current_time += processing_time
                result.append(orginal_idx)
            else:
                current_time = updated_tasks[idx][0]
        return result
