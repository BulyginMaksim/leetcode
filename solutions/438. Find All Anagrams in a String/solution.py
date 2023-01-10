class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        diff = dict()
        for char in p:
            if char not in diff:
                diff[char] = 0
            diff[char] += 1
        counter = len(diff)
        n_elements = len(p)
        for idx in range(n_elements):
            if s[idx] not in diff:
                continue
            diff[s[idx]] -= 1
            if diff[s[idx]] == 0:
                counter -= 1
            if diff[s[idx]] == -1:
                counter += 1
        result = [0] if counter == 0 else []
        for idx in range(n_elements, len(s)):
            if s[idx - n_elements] in diff:
                diff[s[idx - n_elements]] += 1
                if diff[s[idx - n_elements]] == 1:
                    counter += 1
                if diff[s[idx - n_elements]] == 0:
                    counter -= 1
            if s[idx] in diff:
                diff[s[idx]] -= 1
                if diff[s[idx]] == 0:
                    counter -= 1
                if diff[s[idx]] == -1:
                    counter += 1
            if counter == 0:
                result.append(idx - n_elements + 1)
        return result
