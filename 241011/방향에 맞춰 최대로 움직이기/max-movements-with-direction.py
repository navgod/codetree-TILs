n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]
direction = [list(map(int,input().split())) for _ in range(n)]
dxs, dys = [0,0,1,1,1,0,-1,-1,-1] , [0,-1,-1,0,1,1,1,0,-1]
r,c = map(int,input().split())

x,y = c-1, r-1

ans = 0
move_list = []
def is_range(x,y):
    return 0<=x<n and 0<=y<n
def move(x,y):
    global ans

    ans = max(ans, len(move_list))

    dir = direction[y][x]

    dx , dy = dxs[dir] , dys[dir]
    val = grid[y][x]
    nx, ny = x +dx, y+dy
    while is_range(nx,ny):
        if val < grid[ny][nx]:
            move_list.append((nx,ny))
            move(nx,ny)
            move_list.pop()
        x,y = nx ,ny
        nx, ny = x +dx, y+dy

move_list.append((x,y))
move(x,y)

print(ans)