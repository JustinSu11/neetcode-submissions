"""
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.
"""

"""
Example 1:
Input: numCourses = 2, prerequisites = [[0,1]]

Output: true
"""
"""
Example 2:
Input: numCourses = 2, prerequisites = [[0,1],[1,0]]

Output: false
"""

"""
Graph problem = DFS/BFS
Only asking if it is possible = DFS
Also need to know what connects to X = Adjacency list
We need :
    1. a frontier structure, since this is DFS we'll use a stack and for this problem we can use the prerquisites list
    2. a state dict() since each course can have multiple prereqs
    3. neighbor step through to check validity: not state, and satisfies movement condition
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        "Build adjacencylist to see connections"
        adjacencyList = dict()
        for prereq in prerequisites:
            course, nextCourse = prereq
            adjacencyList.setdefault(course, []).append(nextCourse)
        "state dictionary with the course as the key and visiting/visited as the value"
        state = dict()
        
        def dfs(course):
            "if the course is already in the state dict and it is set to visiting that means there is a cycle because we are currently navigating it's prerequisites and we ran into it again so return False."
            if course in state and state[course] == "visiting":
                return False
            "If we already navigated it's prerequisites and we determined that this path is fine, there is no need to re-check so return True"
            if course in state and state[course] == "visited":
                return True
            "set state of this course as visitng before iterating through its neighbors/prerequisites"
            state[course] = "visiting"
            "step through it's prerequisites/neighbors from the adjacencylist"
            for neighbor in adjacencyList.get(course, []):
                if not dfs(neighbor):
                    return False
            "set the value of the course in state to visited so we know its fine"
            state[course] = "visited"
            "this course is good"
            return True
        "iterate through the number of courses to find if we can complete the required courses."
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
