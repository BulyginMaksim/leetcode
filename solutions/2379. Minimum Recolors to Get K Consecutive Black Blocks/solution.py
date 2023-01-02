class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        for idx in range(k):
            if blocks[idx] == 'W':
                white += 1
        min_colors = white
        for idx in range(k, len(blocks)):
            if blocks[idx - k] == 'W':
                white -= 1
            if blocks[idx] == 'W':
                white += 1
            min_colors = min(white, min_colors)
        return min(white, min_colors)
