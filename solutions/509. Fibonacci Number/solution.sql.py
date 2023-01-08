class Solution:
    def fib(self, n: int) -> int:
        last, pred_last = 1, 0
        if n == 0:
            return pred_last
        if n == 1:
            return last
        for _ in range(n - 1):
            new_last = last + pred_last
            pred_last = last
            last = new_last
        return last
