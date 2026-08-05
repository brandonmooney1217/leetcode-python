class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        dct = collections.defaultdict(list)
        n = len(graph)
        for index, val in enumerate(graph):
            for v in val:
                dct[index].append(v)

        color = {}
        def dfs(node, c):
            color[node] = c
            for nei in dct[node]:
                if nei not in color:
                    tmp = dfs(nei, 1-c)
                    if not tmp:
                        return False
                elif color[nei] == c:
                    return False
            return True

        for node in range(n):
            if node not in color:
                if not dfs(node, 1):
                    return False
        return True
