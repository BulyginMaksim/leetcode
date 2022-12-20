from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        used = [False] * n
        self.counter = n
        self.dfs(rooms, 0, used)
        return not self.counter

    def dfs(self, rooms: List[List[int]], idx: int, used: List[bool]):
        used[idx] = True
        self.counter -= 1
        for jdx in rooms[idx]:
            if not used[jdx]:
                self.dfs(rooms, jdx, used)
