from collections import deque

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

Max_firewall = 3

min_area = -float('inf')

directions = [(1,0),(-1,0),(0,1),(0,-1)]

def is_range(r,c):
    return 0<=r<n and 0<= c<m

def cal_firearea(board):
    queue = deque()
    visited = [
        [
            False for _ in range(m)
            ] 
        for _ in range(n)
        ]
    new_board = [
        row[:] for row in board
        ]
    for row in range(n):
        for col in range(m):
            if new_board[row][col] == 2:
                queue.append((row,col))
                visited[row][col] = True
            elif new_board[row][col] == 1:
                visited[row][col] = True
    while queue:
        row , col = queue.popleft()
        for dr, dc in directions:
            nr, nc = row + dr , col + dc
            if is_range(nr,nc) and not visited[nr][nc] and new_board[nr][nc] == 0:
                visited[nr][nc] = True
                new_board[nr][nc] = 2
                queue.append((nr,nc))
    return sum([
        1
        for i in range(n)
        for j in range(m)
        if visited[i][j] == False
    ])

def dfs(cnt,board,added):
    if cnt == Max_firewall:
        global min_area
        min_area = max(min_area, cal_firearea(board))
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 and not ((i,j) in added):
                board[i][j] = 1
                dfs(cnt+1,board,added + [(i,j)])
                board[i][j] = 0

dfs(0,board,[])

print(min_area)