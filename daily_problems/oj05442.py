# http://cs101.openjudge.cn/2025sp_routine/05442/
# Prim Algorithm, see https://www.w3schools.com/dsa/dsa_algo_mst_prim.php
# also can use kruskal's algorithm

import sys
import heapq
from collections import defaultdict

def add_edges(adj_table, edges):
    node = edges[0]
    m = int(edges[1])
    for i in range(2, 2 * m + 2, 2):
        adj_table[node][edges[i]] = int(edges[i + 1])
        adj_table[edges[i]][node] = int(edges[i + 1])

def prim_algorithm(adj_table, n):
    if n == 0 or n == 1:
        return 0

    cost = 0
    connected_nodes = {'A'}
    heap = []
    for key, value in adj_table['A'].items():
        heapq.heappush(heap, (value, key))
    while len(connected_nodes) < n:
        w, v = heapq.heappop(heap)
        if v in connected_nodes:
            continue

        cost += w
        connected_nodes.add(v)
        for key, value in adj_table[v].items():
            if key not in connected_nodes:
                heapq.heappush(heap, (value, key))

    return cost


def main():
    n = int(input())
    adj_table = defaultdict(dict)
    for _ in range(n - 1):
        info = sys.stdin.readline().split()
        add_edges(adj_table, info)

    res = prim_algorithm(adj_table, n)
    print(res)

if __name__ == "__main__":
    main()
