from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for idx in range(len(board)):
            if not self.check_row(board, idx):
                return False
            if not self.check_column(board, idx):
                return False
            if not self.check_square(board, idx):
                return False
        return True

    def check_row(self, board: List[List[str]], idx: int) -> bool:
        chars_set = set()
        for char in board[idx]:
            if char in chars_set:
                return False
            if char != '.':
                chars_set.add(char)
        return len(chars_set) <= 9

    def check_column(self, board: List[List[str]], jdx: int) -> bool:
        chars_set = set()
        for idx in range(len(board)):
            if board[idx][jdx] in chars_set:
                return False
            if board[idx][jdx] != '.':
                chars_set.add(board[idx][jdx])
        return len(chars_set) <= 9

    def check_square(self, board: List[List[str]], nth: int) -> bool:
        # 0, 1, 2 -> (1, 1), (1, 4), (1, 5)
        quotient = nth // 3
        remainder = nth % 3
        idx_center, jdx_center = quotient * 3 + 1, remainder * 3 + 1
        chars_set = set()
        for idx in range(idx_center - 1, idx_center + 2):
            for jdx in range(jdx_center - 1, jdx_center + 2):
                if board[idx][jdx] in chars_set:
                    return False
                if board[idx][jdx] != '.':
                    chars_set.add(board[idx][jdx])
        return len(chars_set) <= 9
