maxi = -1
def is_range(x,y):
    return 0<=x<n and 0<=y<n

def dp(x,y,cnt):
    global maxi

    dxs, dys = [1,-1,0,0],[0,0,1,-1]

    for dx , dy in zip(dxs,dys):
        nx ,ny = x+ dx , y+dy
        if is_range(nx,ny) and grid[ny][nx] > grid[y][x]:
            maxi = max(maxi,cnt+1)
            dp(nx,ny,cnt+1)
    
n = int(input())
grid = []

mini = 1000000000
for _ in range(n):
    tmp = list(map(int,input().split()))
    mini = min(min(tmp),mini)
    grid.append(tmp)


for row in range(n):
    for col in range(n):
        if grid[row][col] == mini:
            dp(row,col,1)

print(maxi)