class Solution:
    def frequencySort(self, s: str) -> str:
        frequencies = dict()
        for char in s:
            if char not in frequencies:
                frequencies[char] = 0
            frequencies[char] += 1
        ans = []
        for char, freq in sorted(
            frequencies.items(),
            key=lambda pair: pair[1],
            reverse=True
        ):
            for _ in range(freq):
                ans.append(char)
        return ''.join(ans)
