from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res = dict()
        for winner, loser in matches:
            res[winner] = res.get(winner, 0)
            res[loser] = res.get(loser, 0) + 1
        result = [[], []]
        for player, cnt_lost in res.items():
            # no loses
            if cnt_lost == 0:
                result[0].append(player)
                continue
            # one lose
            if cnt_lost == 1:
                result[1].append(player)
        result[0].sort()
        result[1].sort()
        return result
