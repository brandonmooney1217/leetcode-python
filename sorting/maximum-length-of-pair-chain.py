from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        count = 1

        prev_end = pairs[0][1]

        for i in range(1, len(pairs)):
            curr_start, curr_end = pairs[i]

            if curr_start > prev_end:
                prev_end = curr_end
                count +=1

        return count
