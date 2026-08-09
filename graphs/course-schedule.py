class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        count = 0
        indegree = [0] * numCourses
        dct = collections.defaultdict(list)

        for a, b in prerequisites:
            indegree[a] +=1
            dct[b].append(a)

        queue = collections.deque()
        for index, val in enumerate(indegree):
            if val == 0:
                queue.append(index)
        while queue:
            curr = queue.popleft()
            count +=1

            for nei in dct[curr]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)

        return count == numCourses
