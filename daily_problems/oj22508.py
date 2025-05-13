# http://cs101.openjudge.cn/practice/22508/
# Kahn's Algorithm, see https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/#

from collections import deque

n, m = map(int, input().split())
adj_table = [[] for _ in range(n)]
in_degree = [0] * n
bonus = [100] * n
for _ in range(m):
    a, b = map(int, input().split())
    in_degree[a] += 1
    adj_table[b].append(a)

q = deque([i for i in range(n) if in_degree[i] == 0])
while q:
    u = q.popleft()
    for v in adj_table[u]:
        in_degree[v] -= 1
        bonus[v] = max(bonus[v], bonus[u] + 1)
        if in_degree[v] == 0:
            q.append(v)

w = sum(bonus)
print(w)