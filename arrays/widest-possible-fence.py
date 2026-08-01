from typing import List
import collections
from collections import Counter


class Solution:
    def maximumWidth(self, planks: list[int]) -> int:

        """
        1 1 1 5 5 5 6

        (51) (51) (51) (6) = 4
        """
        freq = Counter(planks)
        values = list(freq.keys())
        pair_count = collections.defaultdict(int)

        for i in range(len(values)):
            x = values[i]
            if freq[x] >=2:
                pair_count[2*x] += freq[x] //2

            for j in range(i+1, len(values)):
                y = values[j]
                pair_count[x+y] += min(freq[y], freq[x])

        res = max(freq.values()) if freq else 0

        for val, counter in pair_count.items():
            curr_count = counter
            if val in freq:
                curr_count += freq[val]
            res = max(res, curr_count)
        return res
