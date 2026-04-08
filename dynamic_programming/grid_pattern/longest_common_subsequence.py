class Solution:
    def longest_common_subsequence_mxn(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        grid = [
            [0] * (n + 1) for _ in range(m + 1)
        ]  # why n+1 and m+1? to account for the empty string case

        for j in range(1, n):
            grid[0][
                j
            ] = 0  # first row is all 0s because an empty string has no common subsequence with any string

        for i in range(1, m):
            grid[i][
                0
            ] = 0  # first column is all 0s because an empty string has no common subsequence with any string

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    grid[i][j] = (
                        1 + grid[i - 1][j - 1]
                    )  # if the characters match, we can extend the common subsequence by 1
                else:
                    grid[i][j] = max(
                        grid[i - 1][j], grid[i][j - 1]
                    )  # if the characters don't match, we take the maximum of the two possibilities: excluding the current character from either text1 or text2

        return grid[m][
            n
        ]  # the bottom-right cell contains the length of the longest common subsequence

    def longest_common_subsequence_optimal(self, first: str, second: str) -> int:
        m = len(first)
        n = len(second)

        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if first[i - 1] == second[j - 1]:
                    curr[j] = (
                        1 + prev[j - 1]
                    )  # if the characters match, we can extend the common subsequence by 1
                else:
                    curr[j] = max(
                        prev[j], curr[j - 1]
                    )  # if the characters don't match, we take the maximum of the two possibilities: excluding the current character from either first or second

            prev, curr = curr, prev  # swap the references to the arrays
            curr = [0] * (n + 1)  # reset the current array for the next iteration
        return prev[
            n
        ]  # the last element of the prev array contains the length of the longest common subsequence


sol = Solution()
print(sol.longest_common_subsequence_mxn("abcde", "ace"))  # Output: 3
print(sol.longest_common_subsequence_mxn("september", "december"))  # Output: 6
print(sol.longest_common_subsequence_optimal("abcde", "ace"))  # Output: 3
print(sol.longest_common_subsequence_optimal("september", "december"))  # Output: 6
