from collections import deque

n,m = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(n)]
step = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
step[n-1][m-1] = -1
q = deque()

def can_go(x,y):
    return (0<=x<m) and (0<=y<n) and not visited[y][x] and area[y][x]

def bfs():
    dxs , dys = [1,-1,0,0] , [0,0,1,-1]
    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx , ny = x+dx , y+dy
            if can_go(nx,ny):
                visited[ny][nx] = 1
                step[ny][nx] = step[y][x] +1
                q.append((nx,ny))
                if ny == n-1 and nx == m-1:
                    return

q.append((0,0))
visited[0][0] = 1
bfs()

print(step[n-1][m-1])