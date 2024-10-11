n = int(input())
r,c = map(int ,input().split())

x , y = c-1, r-1

grid = [list(input()) for _ in range(n)]

time = 0

def is_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return is_range(x,y) and grid[y][x]== '.' and not visited[y][x]

def right_block(x,y):
    return grid[y][x] == '#'

dxs ,dys = [1,0,-1,0] , [0,-1,0,1]

dir = 0

tof = True
visited = [[0]*n for _ in range(n)]
visited[y][x] = 1
while tof:
    time +=1
    nx, ny = x + dxs[dir] , y + dys[dir]
    if not is_range(nx,ny):
        break
    else:
        if can_go(nx,ny):
            x, y = nx , ny
            visited[y][x] = 1
            if not right_block(x+dxs[(dir-1)%4],y+dys[(dir-1)%4]):
                dir = (dir -1)%4
        else:
            first = dir
            while not can_go(x+dxs[dir],y+dys[dir]):
                if not is_range(x+dxs[dir],y+dys[dir]):
                    tof = False
                    break
                dir = (dir +1)%4
                if dir == first:
                    tof = False
                    time = -1
                    break
            if can_go(x+dxs[dir],y+dys[dir]):
                x, y = x+dxs[dir], y+dys[dir]
                visited[y][x] = 1


print(time)