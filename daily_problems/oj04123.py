#http://cs101.openjudge.cn/2025sp_routine/04123/

move = [(1, 2), (2, 1), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1)]
board = []
num_of_way = 0

def is_valid(board, n, m, x, y):
    if 0 <= x < n and 0 <= y < m and board[x][y] == 0:
        return True
    return False

def dfs(x_cur, y_cur, n, m, cnt = 1):
    global board

    if cnt == n * m:
        global num_of_way
        num_of_way += 1
        return

    for dx, dy in move:
        x, y = x_cur + dx, y_cur + dy
        if is_valid(board, n, m, x, y):
            board[x][y] = 1
            dfs(x, y, n, m, cnt + 1)
            board[x][y] = 0


t = int(input())
for _ in range(t):
    num_of_way = 0
    n, m, x_0, y_0 = map(int, input().split())
    board = [[0 for j in range(m + 1)] for i in range(n + 1)]
    board[x_0][y_0] = 1
    dfs(x_0, y_0, n ,m)

    print(num_of_way)
