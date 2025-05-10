# https://leetcode.cn/problems/min-cost-to-connect-all-points/description/
# Kruskal Algorithm, see https://www.w3schools.com/dsa/dsa_algo_mst_kruskal.php
# disjoint set to judge circles

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        def find(parent, node):
            if parent[node] == node:
                return node
            return find(parent, parent[node])

        def union(parent, rank, x, y):
            x_root = find(parent, x)
            y_root = find(parent, y)

            if x_root == y_root:
                return

            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1
            return

        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((weight, i, j))
        edges.sort()

        cost = 0
        parent = list(range(n))
        rank = [0] * n
        for w, u, v in edges:
            u_root = find(parent, u)
            v_root = find(parent, v)
            if u_root != v_root:
                cost += w
                union(parent, rank, u_root, v_root)

        return cost