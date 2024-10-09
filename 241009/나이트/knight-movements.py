from collections import deque

n = int(input())
r1,c1,r2,c2 = map(int, input().split())

step = [[-1]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
q = deque()

def can_go(x,y):
    return (0<=x<n) and (0<=y<n) and not visited[y][x]

def bfs():
    dxs , dys = [1,2,2,1,-1,-2,-2,-1] , [-2,-1,1,2,2,1,-1,-2]
    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx , ny = x+dx , y+dy
            if can_go(nx,ny):
                visited[ny][nx] = 1
                step[ny][nx] = step[y][x] +1
                q.append((nx,ny))
                if nx == c2-1 and ny == r2-1:
                    return
                

q.append((c1-1,r1-1))
visited[r1-1][c1-1] = 1
step[r1-1][c1-1] = 0

bfs()

print(step[r2-1][c2-1])