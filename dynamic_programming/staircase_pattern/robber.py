class Solution:
    def robber_tabulated(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        max_robbed = [0] * len(nums)
        max_robbed[0], max_robbed[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            max_robbed[i] = max(max_robbed[i-1], max_robbed[i-2] + nums[i])
            print(f"max_robbed[{i}]: {max_robbed[i]}")

        return max_robbed[-1]
    
    def robber_optimized(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        prev1, prev2 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            current = max(prev1 + nums[i], prev2)
            print(f"current: {current}, prev1: {prev1}, prev2: {prev2}, i: {i}")
            prev1, prev2 = prev2, current

        return prev2
    
sol = Solution()
print(sol.robber_tabulated([1, 2, 3, 1]))
print(sol.robber_tabulated([2, 7, 9, 3, 1]))
print(sol.robber_optimized([1, 2, 3, 1]))
print(sol.robber_optimized([2, 7, 9, 3, 1]))