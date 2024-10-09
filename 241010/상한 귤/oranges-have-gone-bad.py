from collections import deque
n, k = map(int, input().split())
visited = [[0]*n for _ in range(n)]
step = [[-1]*n for _ in range(n)]
area = [list(map(int, input().split())) for _ in range(n)]

def push(x,y,s):
    visited[y][x] = 1
    step[y][x] = s
    q.append((x,y))

def can_go(x,y):
    return 0<=x<n and 0<=y<n and not visited[y][x] and area[y][x]

def bfs():
    dxs ,dys = [1,-1,0,0] , [0,0,-1,1]
    while q:
        x , y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx , ny = x+ dx, y + dy
            if can_go(nx,ny):
                push(nx,ny,step[y][x]+1)
q = deque()
for x in range(n):
    for y in range(n):
        if area[y][x] == 2:
            push(x,y,0)
bfs()
for x in range(n):
    for y in range(n):
        if area[y][x] == 1 and visited[y][x] ==0 :
            step[y][x] = -2
for row in step:
    for col in row:
        print(col, end= ' ')
    print()