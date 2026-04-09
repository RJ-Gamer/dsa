class Solution:
    def min_distance(self, first_word: str, second_word: str) -> int:
        m, n = len(first_word), len(second_word)

        grid = [
            [0 for _ in range(m + 1)] for _ in range(n + 1)
        ]  # create a grid of size (n+1) x (m+1)

        for i in range(m + 1):
            grid[0][i] = i  # fill the first row with the column index

        for i in range(n + 1):
            grid[i][0] = i  # fill the first column with the row index

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if first_word[j - 1] == second_word[i - 1]:
                    grid[i][j] = grid[i - 1][
                        j - 1
                    ]  # if characters match, take the diagonal value
                else:
                    grid[i][j] = 1 + min(
                        grid[i - 1][j],
                        grid[i][j - 1],
                        grid[i - 1][
                            j - 1
                        ],  # if characters don't match, take the minimum of the three adjacent values and add 1
                    )
        return grid[n][m]  # the bottom-right cell contains the minimum distance


sol = Solution()
print(sol.min_distance("horse", "ros"))  # Output: 3
print(sol.min_distance("intention", "execution"))  # Output: 5
