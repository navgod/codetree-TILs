from collections import deque

n, m = map(int , input().split())
grid = [[deque() for _ in range(n)]  for _ in range(n)]
for row in range(n):
    col = list(map(int , input().split()))
    for idx,val in enumerate(col):
        grid[row][idx].append(val)
moves = map(int , input().split())

def is_range(x,y):
    return 0<=x<n and 0<=y<n

def find_rocation(i):
    for y in range(n):
        for x in range(n):
            if i in grid[y][x]:
                return (x,y)

def move(i):
    x,y = find_rocation(i)
    dxs,dys = [1,1,1,0,-1,-1,-1,0], [-1,0,1,1,1,0,-1,-1]
    maxi = 0
    for dx, dy in zip(dxs,dys):
        nx,ny = x+dx , y+dy
        if is_range(nx,ny) and grid[ny][nx] and max(grid[ny][nx]) > maxi:
            maxi = max(grid[ny][nx])
            nxx,nyy = nx,ny
    if maxi:
        cnt = grid[y][x].index(i)
        tmp= deque()
        for i in range(cnt+1):
            tmp.appendleft(grid[y][x].popleft())
        for i in range(cnt+1):
            grid[nyy][nxx].appendleft(tmp.popleft())

for i in moves:
    move(i)
for row in range(n):
    for col in range(n):
        if grid[row][col]:
            for i in grid[row][col]:
                print(i, end=' ')
        else:
            print("None", end='')
        print()