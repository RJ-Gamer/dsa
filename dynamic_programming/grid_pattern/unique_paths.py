class Solution:
    def unique_paths_brute_force(self, m: int, n: int) -> int:
        """
        Space Complexity: O(m*n) for the grid
        Time Complexity: O(m*n) to fill the grid
        """
        grid = [[0] * n for _ in range(m)]

        for i in range(n):
            grid[0][i] = 1 # First row can only be reached from the left

        for i in range(m):
            grid[i][0] = 1 # First column can only be reached from above

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1] # Paths from above + paths from the left

        return grid[-1][-1]
    
    def unique_paths_single_row(self, m: int, n: int) -> int:
        """
        Space Complexity: O(n) for the row
        Time Complexity: O(m*n) to fill the row
        """
        row = [1] * n # Initialize the first row with 1s

        for i in range(1, m):
            for j in range(1, n):
                row[j] = row[j] + row[j-1] # Update the current cell with paths from above + paths from the left

        return row[-1]

sol = Solution()
print(sol.unique_paths_brute_force(3, 7)) # Output: 28
print(sol.unique_paths_brute_force(3, 2)) # Output: 3
print(sol.unique_paths_brute_force(7, 3)) # Output: 28
print(sol.unique_paths_brute_force(3, 3)) # Output: 6
print(sol.unique_paths_single_row(3, 7)) # Output: 28
print(sol.unique_paths_single_row(3, 2)) # Output: 3
print(sol.unique_paths_single_row(7, 3)) # Output: 28
print(sol.unique_paths_single_row(3, 3)) # Output: 6