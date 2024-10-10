n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
temp = [[0]*n for _ in range(n)]

def gravity():
    global grid
    for x in range(n):
        temp_y = n-1
        for y in range(n-1,-1,-1):
            if grid[y][x] !=0:
                temp[temp_y][x] = grid[y][x]
                temp_y -=1
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]
    reset_temp()

def reset_temp():
    for i in range(n):
        for j in range(n):
            temp[i][j] = 0

def is_range(x,y):
    return 0<=x<n and 0<=y<n

def explode(x,y):
    global grid
    val = grid[y][x]
    dxs , dys = [1,-1,0,0] , [0,0,1,-1]
    for dx , dy in zip(dxs, dys):
        for i in range(1,val):
            nx, ny = x +dx*i , y +dy*i
            if is_range(nx,ny):
                grid[ny][nx] = 0
    grid[y][x] = 0

def action(col):
    x = col-1
    for y in range(n):
        if grid[y][x] !=0:
            explode(x,y)
            gravity()
            return

for _ in range(m):
    action(int(input()))

for row in grid:
    for col in row:
        print(col, end=' ')
    print()