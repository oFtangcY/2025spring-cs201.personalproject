# http://cs101.openjudge.cn/2025sp_routine/09202/
# using stdin to read the input will cause MLE
# see sunnywhy 382, same as this problem

def dfs(node, graph, color):
    if color[node] == 1:
        return True
    if color[node] == 2:
        return False

    color[node] = 1
    for neighbor in graph[node]:
        if dfs(neighbor, graph, color):
            return True
    color[node] = 2
    return False

def main():
    t = int(input())
    res = []
    for _ in range(t):
        n, m = map(int, input().split())
        adj = [[] for i in range(n + 1)]
        for __ in range(m):
            u, v = map(int, input().split())
            adj[u].append(v)

        color = [0] * (n + 1)
        for node in range(1, n + 1):
            if dfs(node, adj, color):
                res.append('Yes')
                break
        else:
            res.append('No')

    print('\n'.join(res))

if __name__ == "__main__":
    main()