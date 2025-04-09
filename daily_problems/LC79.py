#https://leetcode.cn/problems/word-search/description/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        R, C, l = len(board), len(board[0]), len(word)
        visited = [[0 for _ in range(C)] for __ in range(R)]

        def is_valid(visited, x, y):
            if 0 <= x < R and 0 <= y < C and visited[x][y] == 0:
                return True

        def dfs(board, x, y, i):
            if i == l:
                return True

            for dx, dy in d:
                x_cur, y_cur = x + dx, y + dy
                if is_valid(visited, x_cur, y_cur) and board[x_cur][y_cur] == word[i]:
                    visited[x_cur][y_cur] = 1
                    if dfs(board, x_cur, y_cur, i + 1):
                        return True
                    visited[x_cur][y_cur] = 0

            return False

        if R * C < l:
            return False

        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    if dfs(board, i, j, 1):
                        return True
                    visited[i][j] = 0

        return False