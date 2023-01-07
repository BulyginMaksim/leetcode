from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = sorted([(sum(row), idx) for idx, row in enumerate(mat)])
        return [rows[idx][1] for idx in range(k)]
