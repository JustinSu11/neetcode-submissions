"""
Problem Statement
You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.
"""

"""
Example 1:
Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]

Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
"""

"""
Example 2:
Input: heights = [[1],[1]]

Output: [[0,0],[1,0]]
"""
"""
2D grid/graph problem = DFS/BFS
Not asking for shortest path which means that we don't need to use BFS just asking if path exists (DFS)

DFS = O(depth)

Need for DFS:
    1. visited set()/2D array, if we run into a cell that is in visited we skip it to prevent infinite loops and redundant work
    2. A frontier structure.(DFS = stack, BFS = queue) *holds cells that need to be checked/processed
    3. A neighbor-expansion step with a validity check: in-bounds, not visited, and satisfies movement condition (here: neighor's height >= current height, since you're flowing water backwards up the hill (checking if neighbor has higher height to follow water flow to highest point))
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        "get the bounds of the grid: 0 to len(heights) = rows, 0 to len(heights[0]) = cols"
        rows = len(heights)
        cols = len(heights[0])
        "possible directions in relation to the current cell *see the dfs function for further detail"
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        "frontier structure for pacific: entire top row and left column"
        pacific_frontier = [(0, c) for c in range(cols)] + [(r, 0) for r in range(1, rows)]
        pacific = set()
        "frontier structure for atlantic: entire bottom row and right column"
        atlantic_frontier = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows - 1)]
        atlantic = set()

        def dfs(stack, visited):
            "While there are elements in the frontier/stack"
            while stack:
                "Retrieve the cell from the stack"
                r, c = stack.pop()
                "Check if cell is already visited *continue stops this iteration and goes back to the top of the while loop"
                if (r, c) in visited:
                    continue
                "add to visited if not in there already"
                visited.add((r, c))
                "Check neighboring cells"
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    "Safety checks: check if new cell is in the bounds and if they have been visited"
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        "check if new cell is greater than or equal, if it is then we know that water can flow down it"
                        if heights[nr][nc] >= heights[r][c]:
                            stack.append((nr, nc))

        dfs(pacific_frontier, pacific)
        dfs(atlantic_frontier, atlantic)

        return [[r, c] for r in range(rows) for c in range(cols) if (r, c) in pacific and (r, c) in atlantic]
