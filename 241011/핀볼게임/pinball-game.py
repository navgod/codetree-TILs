n = int(input())

grid = [list(map(int , input().split())) for _ in range(n)]

def is_range(x,y):
    return 0<=x<n and 0<=y<n


case1 = {
    0:2,
    1:3,
    2:0,
    3:1
}
case2 = {
    0:3,
    1:2,
    2:1,
    3:0
}

ans = 0

def simul(x,y,dir):
    # [u d r l]
    dxs, dys = [0,0,1,-1] , [-1,1,0,0]
    t =0
    while True:
        nx, ny = x + dxs[dir] , y + dys[dir]
        t+=1
        if not is_range(nx,ny):
            break
        if grid[ny][nx] ==1:
            dir = case1[dir]
        elif grid[ny][nx] ==2:
            dir = case2[dir]
        x,y = nx,ny
    return t

for x in range(n):
    for y in range(n):
        if x ==0:
            ans = max(ans, simul(-1,y,2))
        if y ==0:
            ans = max(ans, simul(x,-1,1))
        if x == n-1:
            ans = max(ans, simul(n,y,3))
        if y == n-1:
            ans = max(ans, simul(x,n,0))
print(ans)