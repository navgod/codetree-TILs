from collections import deque

BLANK, BLOCK, EXIT, RED, BLUE = 0, 1, 2, 3, 4

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

def move(x, y, dir, board):
    move_cnt = 0
    while True:
        if board[x+dx[dir]][y+dy[dir]] == BLOCK:
            break
        x += dx[dir]
        y += dy[dir]
        move_cnt += 1
        if board[x][y] == EXIT:
            break
    return x, y, move_cnt

n, m = map(int, input().split())
board = []
for i in range(n):
    row = list(input())
    board.append(row)
    for j in range(m):
        if row[j] == 'R':
            rx, ry = i, j
        if row[j] == 'B':
            bx, by = i, j

new_board = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == '#':
            new_board[i][j] = BLOCK
        elif board[i][j] == '.':
            new_board[i][j] = BLANK
        elif board[i][j] == 'O':
            new_board[i][j] = EXIT
        else:
            new_board[i][j] = BLANK

q = deque()
q.append((rx, ry, bx, by, 0))
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
visited[rx][ry][bx][by] = True

answer = -1
while q:
    rx, ry, bx, by, cnt = q.popleft()
    if cnt >= 10:
        break
    for dir in range(4):
        nrx, nry, r_move = move(rx, ry, dir, new_board)
        nbx, nby, b_move = move(bx, by, dir, new_board)
        # 파란 구슬이 구멍에 빠지면 이 방향은 실패
        if new_board[nbx][nby] == EXIT:
            continue
        # 빨간 구슬만 구멍에 빠졌으면 정답
        if new_board[nrx][nry] == EXIT:
            answer = cnt + 1
            q.clear()
            break
        # 두 구슬이 겹쳤으면 더 멀리 이동한 구슬을 한 칸 뒤로 보낸다
        if nrx == nbx and nry == nby:
            if r_move > b_move:
                nrx -= dx[dir]
                nry -= dy[dir]
            else:
                nbx -= dx[dir]
                nby -= dy[dir]
        if not visited[nrx][nry][nbx][nby]:
            visited[nrx][nry][nbx][nby] = True
            q.append((nrx, nry, nbx, nby, cnt + 1))
print(answer)