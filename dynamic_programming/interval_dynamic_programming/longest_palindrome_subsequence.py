class Solution:
    def longest_palindrome_subsequence(self, word: str) -> int:
        """
        Space Complexity: O(n^2) - we use a 2D grid to store the results of subproblems, where n is the length of the input string.
        Time Complexity: O(n^2) - we fill the grid by iterating through all possible substring lengths and starting indices, resulting in a quadratic number of operations.
        """
        size = len(word)
        grid = [[0] * size for _ in range(size)]

        for i in range(size):
            grid[i][i] = 1  # base case: single characters are palindromes of length 1

        for length in range(2, size + 1):  # length of the substring
            for i in range(size - length + 1):  # starting index of the substring
                j = i + length - 1  # ending index of the substring
                if word[i] == word[j]:
                    grid[i][j] = (
                        grid[i + 1][j - 1] + 2
                    )  # if characters match, add 2 to the result from the inner substring
                else:
                    grid[i][j] = max(
                        grid[i + 1][j], grid[i][j - 1]
                    )  # if characters don't match, take the maximum from either excluding the left character or the right character

        return grid[0][
            size - 1
        ]  # the result for the whole string is in the top-right corner of the grid

    def longest_palindrome_subsequence_optimized(self, word: str) -> int:
        size = len(word)

        curr_row = [0] * size
        prev_row = [0] * size

        for i in range(size - 1, -1, -1):
            curr_row[i] = (
                1  # base case: single characters are palindromes of length 1 which is a diagonal in the grid
            )
            for j in range(i + 1, size):
                if word[i] == word[j]:
                    curr_row[j] = (
                        prev_row[j - 1] + 2
                    )  # if characters match, add 2 to the result from the inner substring
                else:
                    curr_row[j] = max(
                        prev_row[j], curr_row[j - 1]
                    )  # if characters don't match, take the maximum from either excluding the left character or the right character

            prev_row, curr_row = (
                curr_row,
                prev_row,
            )  # swap the rows for the next iteration
        return prev_row[
            size - 1
        ]  # the result for the whole string is in the last cell of the previous row after the final swap


sol = Solution()
print(sol.longest_palindrome_subsequence("total"))
print(sol.longest_palindrome_subsequence("loop"))
print(sol.longest_palindrome_subsequence_optimized("total"))
print(sol.longest_palindrome_subsequence_optimized("loop"))
