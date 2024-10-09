from collections import deque
import sys
n,k = map(int , input().split())

q = deque()

area = [list(map(int , input().split()))for _ in range(n)]
visited = [[0]*n for _ in range(n)]
step = [[-1]*n for _ in range(n)]

walls = []

selected_walls = []
ans = sys.maxsize

for x in range(n):
    for y in range(n):
        if area[y][x] == 1:
            walls.append((x,y))

r1, c1 = map(int , input().split())
r2, c2 = map(int , input().split())

def can_go(x,y):
    return 0<= x<n and 0<=y <n and not visited[y][x] and area[y][x] ==0

def push(x,y,s):
    visited[y][x] = 1
    step[y][x] = s
    q.append((x,y))

def bfs():
    dxs,dys = [1,-1,0,0] , [0,0,1,-1]

    while q:
        x, y = q.popleft()
        for dx , dy in zip(dxs,dys):
            nx , ny = x+dx , y +dy
            if can_go(nx,ny):
                push(nx,ny,step[y][x]+1)
                if nx == c2-1 and ny == r2-1:
                    q.clear()
                    return
    
def calc():
    for i in range(n):
        for j in range(n):
            visited[j][i] = 0
            step[j][i] = -1
    
    for x, y in selected_walls:
        area[y][x] = 0
    
    x, y = c1-1 ,r1-1

    push(x,y,0)

    bfs()

    for x, y in selected_walls:
        area[y][x] = 1
    
    return step[r2-1][c2-1]

tof = False
def find_max(idx,cnt):
    global ans, tof
    if cnt > k or idx == len(walls):
        if cnt == k:
            tmp = calc()
            if tmp != -1:
                tof = True
                ans = min(ans, tmp)
        return
    
    selected_walls.append(walls[idx])
    find_max(idx+1,cnt+1)
    selected_walls.pop()
    find_max(idx+1,cnt)

find_max(0,0)
print(ans if tof else -1)