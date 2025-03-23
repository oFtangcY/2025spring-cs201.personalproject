from collections import deque

while True:
    n, p, m = map(int, input().split())
    if n == 0 and p == 0 and m == 0:
        break

    q = deque([])
    for i in range(n):
        q.append((i + p + n - 1) % n + 1)

    ans = []
    while len(q) > 0:
        for i in range(m - 1):
            x = q.popleft()
            q.append(x)

        ans.append(q.popleft())

    print(','.join(map(str, ans)))
