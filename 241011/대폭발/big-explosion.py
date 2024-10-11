n,m,r,c = map(int, input().split())
grid = [[0]*n for _ in range(n)]
x,y =c-1 ,r -1
t =0
bombs = []
bombs.append((x,y))
grid[y][x] = 1
def is_range(x,y):
    return 0<=x<n and 0<=y<n

def explode():
    global t
    if t >= m:
        return
    dxs, dys = [1,-1,0,0] , [0,0,1,-1]
    temp_bombs = []
    for x, y in bombs:
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx*2**t , y+dy*2**t
            if is_range(nx,ny) and not grid[ny][nx]:
                temp_bombs.append((nx,ny))
                grid[ny][nx] =1
    for bomb in temp_bombs:
        bombs.append(bomb)
    t +=1
    explode()
    

explode()
print(len(bombs))