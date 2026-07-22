class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Counts the number of palindromic substrings in the given string.

        count = 0
        for i in range(len(s)):
            left, right = i, i
            while left >=0 and right < len(s) and s[left] == s[right]:
                count +=1
                left -=1
                right +=1

            left, right = i, i+1
            while left >=0 and right < len(s) and s[left] == s[right]:
                count +=1
                left -=1
                right +=1
        return count
        """

        count = 0
        n = len(s)

        # Initialize DP table
        dp = [[False for _ in range(n)] for _ in range(n)]

        # Base cases: single characters and pairs of characters
        for i in range(n):
            dp[i][i] = True
            count +=1

        # Base cases: pairs of characters
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count +=1

        # Dynamic programming: palindromes of length 3+
        for length in range(3, n+1):
            # Iterate over all possible starting indices for palindromes of length 'length'
            for start in range(n-length+1):
                end = start + length-1

                # If the characters at start and end are equal and the substring between them is a palindrome,
                # then the current substring is also a palindrome
                if s[start] == s[end] and dp[start+1][end-1]:
                    dp[start][end] = True
                    count +=1

        return count
