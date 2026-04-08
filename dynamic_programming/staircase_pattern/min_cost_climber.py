class Solution:
    def min_cost_climber(self, costs: list[int]) -> int:
        if not costs:
            return 0
        if len(costs) <= 2:
            return min(costs)

        t0, t1 = costs[0], costs[1]
        for i in range(2, len(costs)):
            t0, t1 = t1, costs[i] + min(t0, t1)
            print(f"t0: {t0}, t1: {t1}, i: {i}")

        return min(t0, t1)
    
    def min_cost_climber_tabulated(self, costs: list[int]) -> int:
        if not costs:
            return 0
        if len(costs) <= 2:
            return min(costs)

        dp = [0] * len(costs)
        dp[0], dp[1] = costs[0], costs[1]

        for i in range(2, len(costs)):
            dp[i] = costs[i] + min(dp[i - 1], dp[i - 2])
            print(f"dp[{i}]: {dp[i]}, i: {i}")

        return min(dp[-1], dp[-2])
    
sol = Solution()
print(sol.min_cost_climber([10, 15, 20, 4, 6, 8]))
print(sol.min_cost_climber_tabulated([10, 15, 20, 4, 6, 8]))
