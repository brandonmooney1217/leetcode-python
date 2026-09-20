class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """

        """
        queue = collections.deque()
        queue.append(0)
        n = len(s)
        furthest = 0

        while queue:
            curr = queue.popleft()
            low = curr + minJump
            high = min(curr + maxJump, n-1)

            for i in range(max(low, furthest), high+1):
                if s[i] == "0":
                    if i == n-1:
                        return True
                    queue.append(i)
            furthest = max(furthest, high)
        return False
