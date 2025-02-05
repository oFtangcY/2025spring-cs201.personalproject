def dfs(chessboard, n, k, cur_row, used_col: set):
    res = 0

    if k == 0:
        return 1

    if n - cur_row < k:
        return 0

    for i in range(n):
        if i not in used_col and chessboard[cur_row][i] == 0:
            used_col.add(i)
            res += dfs(chessboard, n, k - 1, cur_row + 1, used_col)
            used_col.remove(i)

    res += dfs(chessboard, n, k, cur_row + 1, used_col)

    return res


while True:
    n, k = map(int, input().split())
    if n == -1 and k == -1:
        exit()

    board = [[-1] * n for _ in range(n)]
    for i in range(n):
        curr = input()
        for j in range(n):
            if curr[j] == '#':
                board[i][j] = 0

    res = 0
    used_col = set()
    print(dfs(board, n, k, 0, used_col))
