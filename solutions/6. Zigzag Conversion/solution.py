class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        idx = 0
        add_value_idx = 1
        row_idx = 0
        while idx < len(s):
            if row_idx == 0:
                add_value_idx = 1
            elif row_idx == numRows - 1:
                add_value_idx = -1
            rows[row_idx].append(s[idx])
            idx += 1
            row_idx += add_value_idx
        return ''.join([''.join(row) for row in rows])
