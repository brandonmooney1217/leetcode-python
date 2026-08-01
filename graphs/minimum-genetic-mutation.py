
from typing import List
import collections

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        seen = set(bank)
        chars = ["A", "C", "G", "T"]

        queue = collections.deque()
        queue.append((startGene, 0))
        visited = set()
        visited.add(startGene)

        while queue:
            gene, count = queue.popleft()
            if gene == endGene:
                return count

            for i in range(len(gene)):
                for c in chars:
                    tmp = gene[:i] + c + gene[i+1:len(gene)]

                    if tmp in seen and tmp not in visited:
                        visited.add(tmp)
                        queue.append((tmp, count+1))
        return -1



        """
        AACCGGTT
        ->
        AACCGGTA
        AAACGGTA

        ["AACCGGTA","AACCGCTA","AAACGGTA"]

        """
