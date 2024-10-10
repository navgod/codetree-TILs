n,m,k = map(int , input().split())
grid = [list(map(int , input().split())) for _ in range(n)]
temp = [[0]*n for _ in range(n)]

def copy_and_reset():
    for i in range(n):
        for j in range(n):
            grid[i][j] , temp[i][j] = temp[i][j] ,0

def gravity():
    for x in range(n):
        temp_y = n-1
        for y in range(n-1,-1,-1):
            if grid[y][x] !=0:
                temp[temp_y][x] = grid[y][x]
                temp_y -= 1
    copy_and_reset()

def rotate():
    for i in range(n):
        for j in range(n):
            temp[i][j] = grid[n -1 - j][i]
    copy_and_reset()

def explode():
    for x in range(n):
        keep_bomb = 0
        keep = []
        for y in range(n):
            temp[y][x] = grid[y][x]
            if keep_bomb and keep_bomb == grid[y][x]:
                keep.append(y)
            else:
                if len(keep)>=m:
                    for i in keep:
                        temp[i][x] = 0
                keep_bomb = grid[y][x]
                if keep_bomb:
                    keep = [y]
        if len(keep)>=m:
            for i in keep:
                temp[i][x] = 0
    copy_and_reset()

def counting_bomb():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                cnt +=1
    print(cnt)


def printing():
    for row in grid:
        for col in row:
            print(col, end = ' ')
        print()

for _ in range(k):
    explode()
    gravity()
    explode()
    rotate()
    gravity()
explode()
counting_bomb()