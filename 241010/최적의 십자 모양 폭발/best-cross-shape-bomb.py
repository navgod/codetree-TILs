import copy

n = int(input())

grid_ori = [list(map(int, input().split())) for _ in range(n)]

grid = copy.deepcopy(grid_ori)

new_grid = [[0]*n for _ in range(n)]

def gravity():
    for x in range(n):
        new_y = n-1
        for y in range(n-1,-1,-1):
            if grid[y][x] != 0:
                new_grid[new_y][x] = grid[y][x]
                new_y -= 1
    for i in range(n):
        for j in range(n):
            grid[i][j] , new_grid[i][j] = new_grid[i][j] , 0

def is_range(x,y):
    return 0<=x<n and 0<=y <n

def explode(x,y):
    dxs , dys = [1,-1,0,0], [0,0,1,-1]
    for dx , dy in zip(dxs,dys):
        for i in range(1,grid[y][x]):
            nx , ny = x+ dx*i , y + dy*i
            if is_range(nx,ny):
                grid[ny][nx] = 0
    grid[y][x] = 0

def counting():
    cnt = 0
    for x in range(n):
        keep_bomb = 0
        keep = []
        for y in range(n):
            if keep_bomb and keep_bomb == grid[y][x]:
                keep.append(y)
            else:
                if len(keep) == 2:
                    cnt +=1
                keep_bomb = grid[y][x]
                if keep_bomb:
                    keep = [y]
        if keep and len(keep) == 2:
            cnt +=1
    for y in range(n):
        keep_bomb = 0
        keep = []
        for x in range(n):
            if keep_bomb and keep_bomb == grid[y][x]:
                keep.append(y)
            else:
                if len(keep) == 2:
                    cnt +=1
                keep_bomb = grid[y][x]
                if keep_bomb:
                    keep = [y]
        if keep and len(keep) == 2:
            cnt +=1
    return cnt


ans = 0
for i in range(n):
    for j in range(n):
        explode(i,j)
        gravity()
        tmp = counting()
        grid = copy.deepcopy(grid_ori)
        ans = max(ans,tmp)

print(ans)