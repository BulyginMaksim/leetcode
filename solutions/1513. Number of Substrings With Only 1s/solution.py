class Solution:
    def numSub(self, s: str) -> int:
        cur_len = 1
        cur_char = s[0]
        cnt = 0
        mod = 10 ** 9 + 7
        for i in range(1, len(s)):
            char = s[i]
            if char != cur_char:
                if cur_char == '1':
                    cnt += self.pr_sum(cur_len, mod_n=mod)
                cur_char = char
                cur_len = 1
            else:
                cur_len += 1
        if cur_char == '1':
            cnt += self.pr_sum(cur_len, mod_n=mod)
        return cnt % mod

    def pr_sum(self, n, mod_n=None):
        if mod_n is not None:
            return int(n * (n + 1) / 2) % mod_n
        return int(n * (n + 1) / 2)
