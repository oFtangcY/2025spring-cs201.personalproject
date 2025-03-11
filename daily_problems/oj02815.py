#http://cs101.openjudge.cn/practice/02815/

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

m = int(input())
n = int(input())
castle_map = [[[] for _ in range(n)] for _ in range(m)]
for i in range(m):
    line = list(map(int, input().split()))
    for j in range(n):
        castle_map[i][j] = list(map(int, bin(line[j])[2:].rjust(4, '0'))) + [0]

def check(x, y, map):
    if 0 <= x < m and 0 <= y < n and map[x][y][-1] == 0:
        return True
    return False

def dfs(x, y, cnt=1):
    global castle_map

    for i in range(4):
        x_cur, y_cur = x + d[i][0], y + d[i][1]
        if check(x_cur, y_cur, castle_map) and castle_map[x][y][i] == 0:
            castle_map[x_cur][y_cur][-1] = 1
            cnt += dfs(x_cur, y_cur)

    return cnt

count, largest_room = 0, 0
for i in range(m):
    for j in range(n):
        if castle_map[i][j][-1] == 0:
            count += 1
            castle_map[i][j][-1] = 1
            largest_room = max(dfs(i, j), largest_room)

print(count)
print(largest_room)
