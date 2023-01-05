from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.moves = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]
        visited = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
        self.dfs(image, visited, sr, sc, color)
        return image

    def dfs(self, image: List[List[int]], visited: List[List[int]], sr: int, sc: int, color: int):
        visited[sr][sc] = 1
        for move in self.moves:
            idx, jdx = sr + move[0], sc + move[1]
            if not (0 <= idx < len(image) and 0 <= jdx < len(image[0])):
                continue
            if not visited[idx][jdx] and image[sr][sc] == image[idx][jdx]:
                self.dfs(image, visited, idx, jdx, color)
        image[sr][sc] = color
