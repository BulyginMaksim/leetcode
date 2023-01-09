class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last, pred_last = cost[1], cost[0]
        for idx in range(2, len(cost)):
            new_last = cost[idx] + min(pred_last, last)
            pred_last = last
            last = new_last
        return min(last, pred_last)
