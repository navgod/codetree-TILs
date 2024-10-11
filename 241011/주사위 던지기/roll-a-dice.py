n,m,r,c = map(int, input().split())

dir = input().split()
grid = [[0]*n for _ in range(n)]
dir_to_int = {'L':0, 'R':1 , 'U':2, 'D':3}
dxs ,dys = [-1,1,0,0], [0,0,-1,1]

def is_range(x,y):
    return 0<=x <n and 0<=y<n
def dice(now_dice,dir): # 위 앞 오
    if dir == 0:
        new_dice = [now_dice[2],now_dice[1],7-now_dice[0]]
    elif dir == 1:
        new_dice = [7-now_dice[2],now_dice[1],now_dice[0]]
    elif dir == 2:
        new_dice = [now_dice[1],7-now_dice[0],now_dice[2]]
    else:
        new_dice = [7-now_dice[1],now_dice[0],now_dice[2]]
    return new_dice

x,y = c-1, r-1
now_dice = [1,2,3]
grid[y][x] = 7-now_dice[0]
for i in range(m):
    now_dir = dir_to_int[dir[i]]
    nx, ny = x+dxs[now_dir] , y + dys[now_dir]
    if is_range(nx,ny):
        now_dice = dice(now_dice,now_dir)
        grid[ny][nx] = 7- now_dice[0]
        x,y = nx,ny
ans = 0
for row in grid:
    for col in row:
        ans += col

print(ans)