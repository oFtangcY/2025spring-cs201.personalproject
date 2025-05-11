# https://leetcode.cn/problems/network-delay-time/description/
# Dijkstra

import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj_table = defaultdict(dict)
        for u, v, w in times:
            adj_table[u][v] = w

        def dijkstra(table, n, start_node):
            connected_nodes = {start_node}
            heap = []
            for v, w in table[start_node].items():
                heapq.heappush(heap, (w, v))

            while heap:
                t, node = heapq.heappop(heap)
                if node in connected_nodes:
                    continue

                t_tot = t
                connected_nodes.add(node)
                for v, w in table[node].items():
                    if v in connected_nodes:
                        continue
                    heapq.heappush(heap, (t + w, v))

            if len(connected_nodes) < n:
                return -1
            return t_tot

        t = dijkstra(adj_table, n, k)
        return t