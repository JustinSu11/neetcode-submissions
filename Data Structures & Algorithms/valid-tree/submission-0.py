"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
"""

"""
Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]

Output: true
"""

"""
Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]

Output: false
"""

"""
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

"""
So since this is a graph problem, we know that this is a DFS or BFS problem
Since it is only asking if this is a valid graph we can use DFS here
We are checking for cycles
What we need:
    1. We can iterate through range(n)
    2. a visited set()
    3. build an adjacency list
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        "build adjacency list"
        adjList = dict()
        for edge in edges:
            x, y = edge
            "undirected edges so add both ways"
            adjList.setdefault(x, []).append(y)
            adjList.setdefault(y, []).append(x)
        "state dict with the node as the key and a visiting/visited value"
        state = dict()
        "pass node and prevNode to dfs so that we prevent going backwards since these are undirected edges and we added both to the adjList i.e. [0, 1] and [1, 0] we dont want to go back to 0 and be get a False positive for the first condition"
        def dfs(node, prevNode):
            "if currently visiting state[node] then there is a loop; return False"
            if node in state and state[node] == "visiting":
                return False
            "No need to re-check if it was visited before and it was good; return True"
            if node in state and state[node] == "visited":
                return True
            "Mark state[node] as visiting"
            state[node] = "visiting"
            "iterate through the neighbors in the adjList"
            for neighbor in adjList.get(node, []):
                "if we just came from the neighbor, no need to go back it's because of the undirected edges that it could pop up as a neighbor. Just skip this neighbor."
                if neighbor == prevNode:
                    continue
                "if the dfs check on the neighbor is false return False"
                if not dfs(neighbor, node):
                    return False
            "At this point we check the neighbors and this node is good; mark it as visited"
            state[node] = "visited"
            return True
        "start the DFS at 0 and pass None as the prevNode and in the case of a disconnected graph, we need to check that the number of nodes that we visited is the same as the number of nodes (n) that the problem gave us."
        if not dfs(0, None) or len(state) != n:
            return False
        return True