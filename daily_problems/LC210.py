# https://leetcode.cn/problems/course-schedule-ii/description/
# Kahn's Algorithm

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        in_degree = [0] * numCourses
        adj_table = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            in_degree[a] += 1
            adj_table[b].append(a)

        q = deque(i for i in range(numCourses) if in_degree[i] == 0)
        topological_order = []
        while q:
            u = q.popleft()
            topological_order.append(u)
            for v in adj_table[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)

        if len(topological_order) < numCourses:
            return []
        else:
            return topological_order