class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        diff = dict()
        for char in s1:
            if char not in diff:
                diff[char] = 0
            diff[char] += 1

        diff_counter = len(diff)
        for idx in range(n):
            if s2[idx] not in diff:
                continue
            if diff[s2[idx]] == 0:
                diff_counter += 1
            diff[s2[idx]] -= 1
            if diff[s2[idx]] == 0:
                diff_counter -= 1

        idx = n
        while idx < m:
            if not diff_counter:
                return True
            # remove the leftmost element from diff
            char_to_remove = s2[idx - n]
            if char_to_remove in diff:
                if diff[char_to_remove] == 0:
                    diff_counter += 1
                diff[char_to_remove] += 1
                if diff[char_to_remove] == 0:
                    diff_counter -= 1
            # add the rightmost element to diff
            char_to_add = s2[idx]
            if char_to_add in diff:
                if diff[char_to_add] == 0:
                    diff_counter += 1
                diff[char_to_add] -= 1
                if diff[char_to_add] == 0:
                    diff_counter -= 1
            idx += 1
        return not diff_counter
