class Solution:
    def climbStairsRecursive(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairsRecursive(n - 1) + self.climbStairsRecursive(n - 2)

    def climbStairsMemoized(self, n: int) -> int:
        memo = {}
        if n in memo:
            return memo[n]
        if 1 <= n <= 2:
            return n

        result = self.climbStairsMemoized(n - 1) + self.climbStairsMemoized(n - 2)
        memo[n] = result
        return result

    def climbStairsTabulated(self, n: int) -> int:
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        return ways[n]

    def climbStairsOptimized(self, n: int) -> int:
        if 1 <= n <= 2:
            return n

        t1, t2 = 1, 2

        for _ in range(3, n + 1):
            t1, t2 = t2, t1 + t2

        return t2


sol = Solution()
print(sol.climbStairsRecursive(5))
print(sol.climbStairsMemoized(8))
print(sol.climbStairsTabulated(8))
print(sol.climbStairsOptimized(8))
