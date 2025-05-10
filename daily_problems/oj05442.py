import  sys
from collections import defaultdict

def add_edges(adj_table: dict[str: dict], edges: list):
    node = edges[0]
    adj_table[node] = {}
    m = int(edges[1])
    for i in range(2, 2 * m + 2, 2):
        adj_table[node][edges[i]] = int(edges[i + 1])
        adj_table[edges[i]][node] = int(edges[i + 1])

def prim_algorithm(adj_table, n):
    if n == 0 or n == 1:
        return 0

    cost = 0
    connected_nodes = set()
    path = defaultdict(lambda :float('inf'))
    path['A'] = 0
    while len(connected_nodes) < n:
        v = min((node for node in path.keys() if node not in connected_nodes), key=lambda node:path[node])
        w = path[v]

        cost += w
        connected_nodes.add(v)
        for key, value in adj_table[v].items():
            if key not in connected_nodes:
                path[key] = value
        print(v, w)

    return cost


def main():
    n = int(input())
    adj_table = defaultdict(dict)
    for _ in range(n - 1):
        info = sys.stdin.readline().split()
        add_edges(adj_table, info)

    res = prim_algorithm(adj_table, n - 1)
    print(res)

if __name__ == "__main__":
    main()
