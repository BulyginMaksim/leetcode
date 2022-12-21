from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.used = [False for _ in range(n)]
        self.is_left_part = [True for _ in range(n)]
        self.adjency = self.get_adjency_lists(n, dislikes)
        self.flag = True
        for idx in range(n):
            if not self.used[idx]:
                self.dfs(idx)
        return self.flag

    def get_adjency_lists(self, n: int, dislikes: List[List[int]]) -> List[List[int]]:
        adjency = [[] for _ in range(n)]
        for pair in dislikes:
            person_from, person_to = pair
            adjency[person_from - 1].append(person_to - 1)
            adjency[person_to - 1].append(person_from - 1)
        return adjency

    def dfs(self, person: int):
        self.used[person] = True
        neighbours_part_status = not self.is_left_part[person]
        for person_to in self.adjency[person]:
            if not self.used[person_to]:
                self.is_left_part[person_to] = neighbours_part_status
                self.dfs(person_to)
            else:
                got_status = self.is_left_part[person_to]
                if got_status != neighbours_part_status:
                    self.flag = False
