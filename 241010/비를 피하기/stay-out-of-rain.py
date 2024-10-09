from collections import deque
n, h, m = map(int ,input().split())

area= [list(map(int ,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
step = [[-1]*n for _ in range(n)]
ans = [[0]*n for _ in range(n)]
q = deque()

def can_go(x,y):
    return (0<= x < n) and (0<= y < n) and not visited[y][x] and area[y][x] != 1

def bfs():
    dxs , dys = [1,-1,0,0] , [0,0,1,-1]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx , ny = x+dx , y+dy
            if can_go(nx,ny):
                visited[ny][nx] =1
                step[ny][nx] = step[y][x] +1
                q.append((nx,ny))
                if area[ny][nx] == 3:
                    q.clear()
                    return step[ny][nx]

def calc(x,y):
    if area[y][x] !=2:
        return 0
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0
            step[i][j] = -1
    q.append((x,y))
    visited[y][x] = 1
    step[y][x] =0
    tmp = bfs()

    return tmp if tmp else -1

for x in range(n):
    for y in range(n):
        ans[y][x] = calc(x,y)
for row in ans:
    for col in row:
        print(col, end= ' ')
    print()