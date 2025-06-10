import sys
import copy
sys.setrecursionlimit(10000)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def move(board, dir):
    new_board = [row[:] for row in board] # 복사
    if dir == 0:  # up
        for j in range(n):
            merged = [False]*n
            for i in range(1, n):
                if new_board[i][j]:
                    r = i
                    while r > 0 and new_board[r-1][j] == 0:
                        new_board[r-1][j], new_board[r][j] = new_board[r][j], 0
                        r -= 1
                    if r > 0 and new_board[r-1][j] == new_board[r][j] and not merged[r-1]:
                        new_board[r-1][j] *= 2
                        new_board[r][j] = 0
                        merged[r-1] = True
    elif dir == 1:  # down
        for j in range(n):
            merged = [False]*n
            for i in range(n-2, -1, -1):
                if new_board[i][j]:
                    r = i
                    while r < n-1 and new_board[r+1][j] == 0:
                        new_board[r+1][j], new_board[r][j] = new_board[r][j], 0
                        r += 1
                    if r < n-1 and new_board[r+1][j] == new_board[r][j] and not merged[r+1]:
                        new_board[r+1][j] *= 2
                        new_board[r][j] = 0
                        merged[r+1] = True
    elif dir == 2:  # left
        for i in range(n):
            merged = [False]*n
            for j in range(1, n):
                if new_board[i][j]:
                    c = j
                    while c > 0 and new_board[i][c-1] == 0:
                        new_board[i][c-1], new_board[i][c] = new_board[i][c], 0
                        c -= 1
                    if c > 0 and new_board[i][c-1] == new_board[i][c] and not merged[c-1]:
                        new_board[i][c-1] *= 2
                        new_board[i][c] = 0
                        merged[c-1] = True
    else:  # right
        for i in range(n):
            merged = [False]*n
            for j in range(n-2, -1, -1):
                if new_board[i][j]:
                    c = j
                    while c < n-1 and new_board[i][c+1] == 0:
                        new_board[i][c+1], new_board[i][c] = new_board[i][c], 0
                        c += 1
                    if c < n-1 and new_board[i][c+1] == new_board[i][c] and not merged[c+1]:
                        new_board[i][c+1] *= 2
                        new_board[i][c] = 0
                        merged[c+1] = True
    return new_board

def get_max(board):
    return max(max(row) for row in board)

def dfs(board, count):
    global answer
    if count == 5:
        answer = max(answer, get_max(board))
        return
    for dir in range(4):
        next_board = move(board, dir)
        dfs(next_board, count+1)

dfs(board, 0)
print(answer)