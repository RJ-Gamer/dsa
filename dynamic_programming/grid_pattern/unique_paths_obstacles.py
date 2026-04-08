class Solution:
    def unique_paths_obstacles(self, obstacles_grid: list[list[int]]) -> int:
        """
        Space Complexity: O(n) for the array
        Time Complexity: O(m*n) to fill the array
        """
        if (
            obstacles_grid[0][0] == 1
        ):  # If the starting cell has an obstacle, then there are no paths
            return 0

        rows, cols = len(obstacles_grid), len(obstacles_grid[0])

        array = [0] * cols
        array[0] = 1  # Start with 1 path to the starting cell

        for i in range(rows):
            for j in range(cols):
                if obstacles_grid[i][j] == 1:
                    array[j] = 0  # If there's an obstacle, set paths to 0

                elif j > 0:
                    array[j] += array[
                        j - 1
                    ]  # Update paths to current cell by adding paths from the left
                    print(f"array[{j}]: {array[j]}, i: {i}, j: {j}")
        return array[cols - 1]  # Return the number of paths to the bottom-right corner


sol = Solution()
print(sol.unique_paths_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # Output: 2
print(sol.unique_paths_obstacles([[0, 1], [0, 0]]))  # Output: 1
print(sol.unique_paths_obstacles([[1, 0], [0, 0]]))  # Output: 0
print(sol.unique_paths_obstacles([[0, 0], [1, 0]]))  # Output: 0
print(
    sol.unique_paths_obstacles(
        [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    )
)
