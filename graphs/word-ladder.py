import collections
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord == beginWord:
            return 0
        if endWord not in wordList:
            return 0

        bank = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                tmp = word[:i] + "*" + word[i+1:]
                bank[tmp].append(word)

        queue = collections.deque()
        queue.append([beginWord, 1])
        seen = set()
        seen.add(beginWord)

        while queue:
            word, count = queue.popleft()

            if word == endWord:
                return count

            for i in range(len(word)):
                tmp_word = word[:i] + "*" + word[i+1:]
                if tmp_word in bank:

                    for b in bank[tmp_word]:
                        if b not in seen:
                            seen.add(b)
                            queue.append([b, count+1])

        return 0
