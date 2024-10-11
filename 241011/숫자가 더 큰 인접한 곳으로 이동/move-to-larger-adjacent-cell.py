n,r,c = map(int , input().split())

grid = [list(map(int , input().split())) for _ in range(n)]

def is_range(x,y):
    return 0<=x < n and 0<= y < n

def simul():
    global x, y
    tof = False
    dxs, dys = [0,0,-1,1] , [-1,1,0,0]
    for dx, dy in zip(dxs,dys):
        nx, ny = x+dx , y+dy
        curr_val = grid[y][x]
        if is_range(nx,ny) and grid[ny][nx] > curr_val:
            print(grid[ny][nx], end=' ')
            x, y = nx, ny
            tof = True
            break
    if tof:
        simul()
x, y = c-1 ,r-1
print(grid[y][x], end = ' ')
simul()