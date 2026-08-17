class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_list = {i: [] for i in range(n)}
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        seen = [False] * n
        def dfs(node):
            for neighbor in adj_list[node]:
                if not seen[neighbor]:
                    seen[neighbor] = True
                    dfs(neighbor)

        count = 0
        for i in range(n):
            if not seen[i]:
                seen[i] = True
                dfs(i)
                count += 1

        return count
