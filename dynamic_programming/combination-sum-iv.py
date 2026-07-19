from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        dp[i] = represents total number of ways to get sum i
        0 1 2 3 4
        1 1 2 4 0

        3 (111) (12) (21) (3)
        """
        dp = [0] * (target+1)
        dp[0] = 1

        for sm in range(1, target+1):
            for num in nums:
                if sm >= num:
                    dp[sm] += dp[sm-num]

        return dp[target]
