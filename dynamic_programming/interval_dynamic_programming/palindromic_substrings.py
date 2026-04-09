from functools import lru_cache


class Solution:
    def palindromic_substrings(self, word: str) -> int:
        """
        Memoized Recursion (Top-Down)
        Time: O(n^2) — each (i, j) pair computed once
        Space: O(n^2) — cache stores all (i, j) results + recursion stack
        """
        size = len(word)
        count = 0

        for i in range(size):
            for j in range(i, size):
                if self.is_palindrome(word, i, j):
                    count += 1

        return count

    @lru_cache(maxsize=None)
    def is_palindrome(self, word: str, left: int, right: int) -> bool:
        if left >= right:
            return True

        if word[left] != word[right]:
            return False

        return self.is_palindrome(word, left + 1, right - 1)

    def palindromic_substrings_dp(self, word: str) -> int:
        """
        Interval DP — Boolean Table (Bottom-Up)
        Time: O(n^2) — fill every cell in the upper triangle
        Space: O(n^2) — the full n×n boolean grid
        """
        size = len(word)
        dp = [[False] * size for _ in range(size)]
        count = 0

        # Base case: single characters
        for i in range(size):
            dp[i][i] = True
            count += 1

        # Length 2: handled separately (inner interval would be in the lower triangle)
        for i in range(size - 1):
            if word[i] == word[i + 1]:
                dp[i][i + 1] = True
                count += 1

        # Length 3 and above
        for length in range(3, size + 1):
            for i in range(size - length + 1):
                j = i + length - 1
                if word[i] == word[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1

        return count

    def palindromic_substrings_center(self, word: str) -> int:
        """
        Expand Around Center (Space-Optimized)
        Time: O(n^2) — n centers × up to n expansions each
        Space: O(1) — no grid needed
        """
        size = len(word)
        count = 0

        for center in range(size):
            # Odd-length palindromes: single character at center
            left, right = center, center
            while left >= 0 and right < size and word[left] == word[right]:
                count += 1
                left -= 1
                right += 1

            # Even-length palindromes: gap between center and center+1
            left, right = center, center + 1
            while left >= 0 and right < size and word[left] == word[right]:
                count += 1
                left -= 1
                right += 1

        return count


sol = Solution()
print(sol.palindromic_substrings("madam"))           # Expected: 7
print(sol.palindromic_substrings("aaa"))              # Expected: 6

print(sol.palindromic_substrings_dp("madam"))         # Expected: 7
print(sol.palindromic_substrings_dp("aaa"))           # Expected: 6

print(sol.palindromic_substrings_center("madam"))     # Expected: 7
print(sol.palindromic_substrings_center("aaa"))       # Expected: 6
