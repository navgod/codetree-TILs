n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
r,c = map(int, input().split())

x,y = c-1, r-1
dxs , dys = [1,-1,0,0] , [0,0,1,-1]
def is_range(x,y):
    return 0<= x <n and 0<=y <n

for dx,dy in zip(dxs,dys):
    for i in range(1,area[y][x]):
        nx, ny = x+dx*i , y+dy*i
        if is_range(nx,ny):
            area[ny][nx] = 0

area[y][x] =0
temp = [[0]*n for _ in range(n)]

def gravity():
    for col in range(n):
        temp_row = n-1
        for row in range(n-1,-1,-1):
            if area[row][col] !=0:
                temp[temp_row][col] = area[row][col]
                temp_row -=1
gravity()

area = temp

for row in area:
    for col in row:
        print(col, end =' ')
    print()